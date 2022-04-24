FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app/
COPY ./app /app

RUN apt-get update -y && apt-get upgrade -y 
RUN apt-get install -y poppler-utils tesseract-ocr libtesseract-dev

# prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1


RUN pip3 install -r /app/requirements.txt
ENV PYTHONPATH=/app

#RUN /start.sh