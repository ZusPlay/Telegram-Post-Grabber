# syntax=docker/dockerfile:1

FROM python:3.10-slim-bullseye

WORKDIR /grabber

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "grabber.py", "--host=0.0.0.0"]
