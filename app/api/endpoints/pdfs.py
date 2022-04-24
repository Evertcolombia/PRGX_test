import imp
from fastapi import APIRouter, Depends, HTTPException
from pdf2image import convert_from_path
from sqlmodel import Session

# local imports
from api.helpers.post_helpers import *
from api.db.init_db import get_session
from api.models.pdfs import ExtractCreate


router = APIRouter()

@router.post("/extract")
async def extract_data(
    *,
    session: Session = Depends(get_session),
    doc_path: str = None
):
    """
    """ 
    if doc_path is None:
        raise HTTPException(status_code=400, detail="doc_path is required")

    try: # convert the pdf to image
        images = convert_from_path(doc_path)
    except:
        raise HTTPException(status_code=500,
            detail="image from {} can't be extracted or does not exist".format(doc_path))
    
    # get list of regex 
    regex = get_regex()

    obj = {
        "Vendor_Name": "", 
        "Fiscal_Number": "",
        "Contract": "",
        "Start_Date": "",
        "End_Date": "",
    }

    # extract text from image
    extract = [read_img(images[0])]
    # get and format the data for the first part os res
    obj = format_init(regex[0], extract[0], obj)
    # get and format the data for the comments part
    obj = format_comments(regex[1], extract[0], obj)
    obj["Doc_Path"] = doc_path
    
    db_obj = ExtractCreate.from_orm(obj)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)

    
    res = [
        [db_obj.id, True],
        obj
    ]
    return res




        