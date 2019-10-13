FROM python:3.7-stretch
LABEL maintainer="tinventory@jonathanweth.de"
LABEL org.label-schema.name="katharineum/tinventory"
LABEL org.label-schema.description="Inventory toolkit in order not to lose technology stuff anymore"
LABEL org.label-schema.vcs-url="https://github.com/Katharineum/tinventory"

ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
	libmariadbclient-dev && \
	pip3 install --upgrade pip && \
	pip3 install uwsgi mysqlclient && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt /home/docker/requirements.txt
COPY web /var/www/
COPY docker-setup/uwsgi-app.ini /etc/uwsgi/apps-enabled/uwsgi-app.ini
COPY docker-setup/init_and_run.sh /home/docker/init_and_run.sh
WORKDIR /home/docker/
RUN pip3 install -r requirements.txt
EXPOSE 3031
CMD ["/home/docker/init_and_run.sh"]
