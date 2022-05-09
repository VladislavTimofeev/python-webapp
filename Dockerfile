FROM python:3.10

WORKDIR /python/project/flask

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
#CMD ["python", "main.py" , "flask", "run", "localhost:5000"]
