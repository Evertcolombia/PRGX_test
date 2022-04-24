from sqlmodel import create_engine
import os

# local imports
from api.models import pdfs

engine = create_engine(os.environ["DB_URL"], echo=True)
