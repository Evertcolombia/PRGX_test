import imp
from fastapi import APIRouter, Depends, HTTPException
from pdf2image import convert_from_path
from sqlmodel import Session
from sqlalchemy import select, desc

# local imports
from api.helpers.post_helpers import *
from api.db.init_db import get_session
from api.models.pdfs import Extractions


router = APIRouter()

@router.post("/extract")
async def extract_data(
    *,
    session: Session = Depends(get_session),
    doc_path: str = None
):
    """
    Create an extraction from a file
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
    
    # extract text from image
    extract = [read_img(images[0])]
    # get and format the data for the first part os res
    obj = format_init(regex[0], extract[0])
    # get and format the data for the comments part
    obj = format_comments(regex[1], extract[0], obj)
    obj["Doc_Path"] = doc_path

    try:
        db_obj = Extractions(
            vendor_name=obj["Vendor_Name"],
            fiscal_number=obj["Fiscal_Number"],
            contract=obj["Contract"],
            start_date=obj["Start_Date"],
            end_date=obj["End_Date"],
            comments=obj["Comments"],
            doc_path=obj["Doc_Path"])
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
    except:
        raise HTTPException(status_code=500, detail="can't save o new extract on db")

    res = [
        [True, db_obj.id],
        obj
    ]
    return res


@router.get("/db_data", response_model=list)
async def get_data(
    *,
    session: Session = Depends(get_session),
    table_name: str = None
):
    """
    Get the list of rows from a table idenfied by table_name
    """
    if table_name is None:
        raise HTTPException(status_code=400, detail="table_name is required")

    result = session.execute(select(Extractions).order_by(desc(Extractions.id)))
    result = result.scalars().all()
    res = []
    for el in result:
        ex = Extractions(
            vendor_name=el.vendor_name,
            id=el.id,
            start_date=el.start_date,
            comments=el.comments,
            doc_path=el.doc_path,
            contract=el.contract,
            fiscal_number=el.fiscal_number,
            end_date=el.end_date)
        res.append(ex)
    return res
