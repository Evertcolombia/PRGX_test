from io import BytesIO
from PIL import Image
import re
import pytesseract


def read_img(page):
    """
        read image from a pdf file page
        args:
            @page: page to read
    """
    with BytesIO() as f:
        page.save(f, format="jpeg")
        f.seek(0)
        img = Image.open(f)
        text = pytesseract.image_to_string(img, lang = 'eng')
        return text


def get_mo(exp, extract):
    """
        generate a matc object using a regex

        - args:
            @exp: regex
            @extract: text of pdf file
    """
    mo = re.search(exp, extract, re.IGNORECASE)
    if mo is not None:
        value = mo.group().split("\n")
        value = (list(filter(bool, value)))
        return value
    return None


def format_init(exp, extract):
    """
        format the data from the extract
        - args:
            @exp: regex
            @extract: string content from pdf
    """ 
    obj = {
        "Vendor_Name": "", 
        "Fiscal_Number": "",
        "Contract": "",
        "Start_Date": "",
        "End_Date": "",
    }

    values = get_mo(exp, extract)

    if values != None:
        for k  in obj.keys():
            idx = [idx for (idx, s) in enumerate(values) if k[0:3] in s][0]
            value = values[idx].split(":")[1]
            
            if value == "":
                obj[k] = values[idx + 1]
            else:
                if value[0] == " ":
                    value = value[1:]
                obj[k] = value
    return obj


def format_comments(exp, extract, obj={}):
    """
        format the comments section from extract string
        - args:
            @exp: regex
            @extract: string content
            @obj: obj Extraction
    """
    values = get_mo(exp, extract)
    if values != None:
        k = values[0].replace(":", "")
        del values[0]
        v = " ".join(values)
        obj[k] = v
    else:
        obj["Comments"] = None
    return obj


def get_regex():
    """
        get regex list to use
    """
    # \D+   -> any non digit and more
    # (.*)  -> 0 to many characters
    # \s    -> Any space, tab, or newline character
    # \S    -> Any character that is not a space, tab, or newline
    # *     -> * matches zero or more of the preceding group
    expresions = [
        # [0] -> gest data for vendor, fiscal, contract, star and end date
        # [1] -> gets data for comments
        r'vendor name: \D+(.*) (.*)\s\D+(.*) (.*)\s\D+\s\S+\s\D+\S+',
        r'\scomments:(\s*\D+(\.\n))'
    ]

    return expresions