FROM python:3.8
WORKDIR /newsreels-challenge
COPY . .
CMD ["python","to_do_list.py"]
