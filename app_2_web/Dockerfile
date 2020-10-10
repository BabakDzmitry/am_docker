FROM python:3.8
RUN pip install pipenv
RUN mkdir -p /tmp
COPY Pipfile* /tmp
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN cd /
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

CMD ["python", "app.py"]