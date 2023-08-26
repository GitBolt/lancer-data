FROM python:3.8-slim

COPY /server /root
COPY /server/new_data.json /root

WORKDIR /root

RUN pip install uvicorn python-dotenv requests SQLAlchemy fastapi mysql-connector-python

COPY . /app

CMD python get_language_info.py