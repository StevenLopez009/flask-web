FROM python:3.12.0

RUN apt-get update && apt-get install -y build-essential

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]