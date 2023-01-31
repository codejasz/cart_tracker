FROM python:3.11

ENV BACKEND_PATH /backend
ENV WEB_PATH ${BACKEND_PATH}/src

WORKDIR ${BACKEND_PATH}

RUN pip install --upgrade pip
ADD . ${BACKEND_PATH}
RUN pip install -r src/requirements.txt --no-cache-dir

WORKDIR ${WEB_PATH}/tracker
