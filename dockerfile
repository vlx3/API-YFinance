FROM python:3.11.6

WORKDIR /app

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY . /app/

CMD [ "fastapi", "dev", "src/main.py","--host","0.0.0.0" , "--port", "8000"]