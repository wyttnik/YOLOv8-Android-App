FROM ubuntu:22.04

RUN apt-get update && \
   apt-get install --no-install-recommends -y python3 python3-pip

WORKDIR /usr/yolo_v8_app
COPY ./ultralytics ultralytics
RUN pip install --no-cache-dir -e ultralytics
COPY ./train.py train.py
COPY ./val.py val.py
COPY ./custom.yaml custom.yaml