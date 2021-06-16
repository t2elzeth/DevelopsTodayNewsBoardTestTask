FROM python:3.9

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt && pip install gunicorn==20.0.4

COPY . .

ENTRYPOINT ["sh", "entrypoint.sh"]