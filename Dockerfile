FROM python:3.8.6


RUN pip install -r requirements.txt

RUN python app.py