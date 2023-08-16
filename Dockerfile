FROM python:3.7.5-slim

WORKDIR /bot
COPY . /bot

RUN pip install -r requirements.txt

CMD [ "python3", "app.py" ]