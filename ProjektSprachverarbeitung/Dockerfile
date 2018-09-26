FROM python:3.5

LABEL "maintainer" "Felix Fröhlich"

WORKDIR app

# install dependencies
ADD requirements.txt .
ADD manage.py .
RUN pip3 install -r requirements.txt



# download ressources
RUN mkdir -p ./resources/word2vec && wget -O ./resources/word2vec/german.model http://cloud.devmount.de/d2bc5672c523b086/german.model

# copy sources
ADD . .

EXPOSE 8000

RUN chmod +x ./run.sh

CMD python3 ./manage.py runserver 0.0.0.0:8000
