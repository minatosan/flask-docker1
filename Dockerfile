FROM python:3.7

WORKDIR /app

ADD . /app

COPY /app/requirements.txt ./
ADD app/requirements.txt $project_dir

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

