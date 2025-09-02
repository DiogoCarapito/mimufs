FROM python:3.12.5-slim

WORKDIR /code

COPY . /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["python", "main.py"]
