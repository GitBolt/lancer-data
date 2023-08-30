FROM python:3.9

COPY /server /root

COPY /server/new_data.json /root

WORKDIR /root

RUN pip install uvicorn python-dotenv requests SQLAlchemy fastapi mysql-connector-python

CMD uvicorn main:app --host 0.0.0.0 --port $PORT