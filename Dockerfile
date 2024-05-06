FROM python:alpine
LABEL mantainer="v.mazhuga"

RUN apk add --no-cache bash py3-pip && mkdir /opt/rocketchat_python && pip install requests

WORKDIR /opt/rocketchat_python

COPY rocketchat_block_iddle.py .
COPY entrypoint.sh .

ENTRYPOINT [ "/bin/bash","./entrypoint.sh" ]