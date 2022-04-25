from typing import Optional
from sqlmodel import Field, SQLModel, String, create_engine


class ExtractBase(SQLModel):
    vendor_name: Optional[str] = Field(default=None)
    fiscal_number: Optional[str] = Field(default=None)
    contract: Optional[str] = Field(default=None)
    start_date: Optional[str] = Field(default=None)
    end_date: Optional[str] = Field(default=None)
    comments: Optional[str] = Field(default=None)
    doc_path: Optional[str] = Field(default=None)

    
class Extractions(ExtractBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
