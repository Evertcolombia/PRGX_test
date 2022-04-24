from io import BytesIO
from PIL import Image
import re
import pytesseract


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


def format_comments(exp, extract, res={}):
    """"""
    values = get_mo(exp, extract)
    if values != None:
        k = values[0].replace(":", "")
        del values[0]
        v = " ".join(values)
        res[k] = v
    else:
        res["Comments"] = None
    return res


def get_regex():
    """"""
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