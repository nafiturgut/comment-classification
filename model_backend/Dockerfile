FROM python:3.7

ENV PYTHONUNBUFFERED=1

WORKDIR /api

# In order to leverage caching of Docker, install requirements first
ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]