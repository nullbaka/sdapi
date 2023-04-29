# Use the official Python runtime as a parent image
FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install libgomp1
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
