FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY weather_query_project .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runerver", "0.0.0.0:8000"]