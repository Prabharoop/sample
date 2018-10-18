FROM python:3
WORKDIR /usr/src/app
ADD requirements.txt /user/src/app
ADD . /usr/src/app
RUN pip install -r ./requirements.txt

