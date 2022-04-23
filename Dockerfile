FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app/
COPY ./app /app

RUN apt-get update -y && apt-get upgrade -y 
RUN apt-get install -y poppler-utils tesseract-ocr libtesseract-dev
# RUN apt-get install -y tesseract-ocr libtesseract-dev -y

RUN pip3 install -r /app/requirements.txt
ENV PYTHONPATH=/app