FROM python:3.9


WORKDIR /root


COPY /server /root/server

RUN pip install uvicorn python-dotenv requests SQLAlchemy fastapi mysql-connector-python

CMD uvicorn server.main:app --host 0.0.0.0 --port $PORT