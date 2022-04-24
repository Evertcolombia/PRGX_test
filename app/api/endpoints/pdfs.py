from fastapi import APIRouter
from pdf2image import convert_from_path
from io import BytesIO
from PIL import Image
import re

import pytesseract

router = APIRouter()

@router.get("/")
async def root():
    
    pages = convert_from_path("/app/src/Doc2.pdf")
    extract = [read_img(pages[0])]

    # \D+   -> any non digit and more
    # (.*)  -> 0 to many characters
    # \s    -> Any space, tab, or newline character
    # \S    -> Any character that is not a space, tab, or newline
    # *     -> * matches zero or more of the preceding group
    expresions = [
        r'vendor name: \D+(.*) (.*)\s\D+(.*) (.*)\s\D+\s\S+\s\D+\S+',
        r'\scomments:(\s*\D+(\.\n))'
    ]

    res = [
        [],
        {
            "Vendor_Name": "", 
            "Fiscal_Number": "",
            "Contract": "",
            "Start_Date": "",
            "End_Date": "",
        }
    ]
  
    res[1] = format_init(expresions[0], extract[0], res[1])
    print(res)

    return {"message": "Hello World"}


def read_img(page):
    with BytesIO() as f:
        page.save(f, format="jpeg")
        f.seek(0)
        img = Image.open(f)
        text = pytesseract.image_to_string(img, lang = 'eng')
        return text


def get_mo(exp, extract):
    """"""
    mo = re.search(exp, extract, re.IGNORECASE)
    if mo is not None:
        value = mo.group().split("\n")
        value = (list(filter(bool, value)))
        return value
    return None


def format_init(exp, extract, res={}):
    """
    """ 
    values = get_mo(exp, extract)

    if values != None:
        for k  in res.keys():
            idx = [idx for (idx, s) in enumerate(values) if k[0:3] in s][0]

            value = values[idx].split(":")[1]

            if value == "":
                res[k] = values[idx + 1]
            else:
                if value[0] == " ":
                    value = value[1:]
                res[k] = value
    return res

def format_comments():
    """"""
    pass


        