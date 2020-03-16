FROM python:3.7

WORKDIR /usr/src/

COPY ./ ./

RUN apt-get update \
    && apt-get install -y python-pip

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD python src/__main__.py
