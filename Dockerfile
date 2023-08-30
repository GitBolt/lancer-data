FROM python:3.9


WORKDIR /root


RUN pip install uvicorn python-dotenv requests SQLAlchemy fastapi mysql-connector-python


COPY /server /root/server


CMD uvicorn server.main:app --host 0.0.0.0 --port $PORT