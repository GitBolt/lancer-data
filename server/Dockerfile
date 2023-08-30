FROM python:3.8


WORKDIR .

RUN pip install uvicorn python-dotenv requests SQLAlchemy fastapi mysql-connector-python

CMD uvicorn main:app --host 0.0.0.0 --port $PORT