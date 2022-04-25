from fastapi.testclient import TestClient

# local imports
from app.main import app

api_url = "/api/v1/"
client = TestClient(app)

def test_create_extract() -> None:
    doc_path = "/app/src/Doc2.pdf"
    response = client.post(f"{api_url}extract?doc_path={doc_path}")
    assert response.status_code == 200
    content = response.json()
    keys = content[1].keys()
    assert True == content[0][0]
    assert "Vendor_Name" in keys
    assert "Fiscal_Number" in keys
    assert "Contract" in keys
    assert "Start_Date" in keys
    assert "End_Date" in keys
    assert "Comments" in keys
    assert "Doc_Path" in keys


def test_create_extract_no_path() -> None:
    response = client.post(f"{api_url}extract")
    assert response.status_code == 400
    content = response.json()
    assert "doc_path is required" == content["detail"]


def test_create_extract_file_not_exist() -> None:
    response = client.post(f"{api_url}extract?doc_path=error.pdf")
    assert response.status_code == 500


def test_read_extracts() -> None:
    response = client.get(f"{api_url}db_data?table_name=extract")
    assert response.status_code == 200
    content = response.json()
    obj  = content[0]
    assert "id" in obj
    assert "vendor_name" in obj
    assert "fiscal_number" in obj
    assert "contract" in obj
    assert "start_date" in obj
    assert "end_date" in obj
    assert "comments" in obj
    assert "doc_path" in obj


def test_read_extracts_no_table_name() -> None:
    response = client.get(f"{api_url}db_data")
    assert response.status_code == 400
    content = response.json()
    assert "table_name is required" == content["detail"]


