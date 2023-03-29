from python:3.8-slim

run apt update && apt install nginx -y

copy ./nginx/default.conf /etc/nginx/conf.d/default.conf

copy . .

run pip install -r requirements.txt

workdir /titan
copy run.sh .

run chmod +x run.sh

cmd ["./run.sh"]