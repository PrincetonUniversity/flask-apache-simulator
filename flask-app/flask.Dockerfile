FROM python:3.7-buster

RUN pip install flask

VOLUME "/opt/libraries"

WORKDIR /opt/libraries

ENTRYPOINT ["python"]
CMD ["helloworld.py"]
