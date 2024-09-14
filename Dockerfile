FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 80

CMD ["python","main.py","runserver","0.0.0.0:8082"