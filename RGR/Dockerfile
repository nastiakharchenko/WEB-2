FROM python:3.9
WORKDIR /onlinestore
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY online_store .
ADD online_store/onlinestore /onlinestore/