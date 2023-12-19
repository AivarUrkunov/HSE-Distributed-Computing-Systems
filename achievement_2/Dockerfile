FROM python:3.12

WORKDIR /

COPY requirements.txt /tmp/requirements.txt

RUN python3 -m pip install -r /tmp/requirements.txt
ADD ./templates ./templates
ADD main.py main.py
ADD requirements.txt requirements.txt

ENTRYPOINT ["python3"]
CMD ["task_3.py"]
