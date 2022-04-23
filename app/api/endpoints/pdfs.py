from fastapi import APIRouter
from pdf2image import convert_from_path
from io import BytesIO
from PIL import Image
import pytesseract

router = APIRouter()

@router.get("/")
async def root():
    
    pages = convert_from_path("/app/src/Doc2.pdf")
    extract = []
    
    print()
    if len(pages) > 1:
        for page in pages:
            extract.append(read_img(page))
    else:
        extract.append(read_img(pages[0]))

    print(extract)
    return {"message": "Hello World"}


def read_img(page):
    with BytesIO() as f:
        page.save(f, format="jpeg")
        f.seek(0)
        img = Image.open(f)
        text = pytesseract.image_to_string(img, lang = 'eng')
        return text