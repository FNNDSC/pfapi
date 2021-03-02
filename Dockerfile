# Docker file for heatmap ChRIS plugin app
#
# Build with
#
#   docker build -t <name> .
#
# For example if building a local version, you could do:
#
#   docker build -t local/pfapi .
#
# In the case of a proxy (located at say 10.41.13.4:3128), do:
#
#   export PROXY=http://10.41.13.4:3128
#   docker build --build-arg http_proxy=$PROXY --build-arg UID=$UID -t local/pfapi .
#
# To run an interactive shell inside this container, do:
#
#   docker run -ti --entrypoint /bin/bash local/pfapi
#
# To debug code within this container, do
#
#   docker run -ti  --entrypoint /bin/bash local/pfapi
#


FROM python:3.9.1-slim-buster
LABEL maintainer="FNNDSC devs <dev@babymri.org>"
LABEL DEBUG="\
    docker run -ti --rm                                                         \
        -v $PWD/pfapi:/usr/local/lib/python3.9/site-packages/pfapi:ro           \
        local/pfapi pfapi                                                       \
        --ipSelf localhost                                                      \
        --portSelf 4005                                                         \
        --swiftIP localhost                                                     \
        --swiftPort 8080                                                        \
        "

# Set some env variables...
ENV DEBIAN_FRONTEND=noninteractive APPLICATION_MODE="production" UID=$UID
ENV WORKDIR=/usr/local/src
ENV USER=app
ENV APP_HOME=/home/app/web

WORKDIR $WORKDIR

# Misc updating...
RUN pip install --upgrade pip
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install sudo
RUN apt-get -y install python3-uvicorn
RUN apt-get -y install python3-httptools
RUN apt-get -y install python3-websockets
RUN apt-get -y install gcc

# Install core requirements into container space...
COPY ./requirements.txt $WORKDIR/requirements.txt
RUN pip install -r requirements.txt

# Add the (non root) user that will "run" the service...
RUN adduser --system --group $USER
# RUN echo -e "app1234\napp1234" | passwd  $USER
RUN mkdir $APP_HOME

WORKDIR ${APP_HOME}
COPY . ${APP_HOME}
RUN chown -R ${USER}:${USER} $APP_HOME
RUN pip install .

USER $USER

ENTRYPOINT [ "gunicorn" ]
EXPOSE 4005

# Start server
CMD [ "--bind", "0.0.0.0:4005", "-w", "7", "-t", "7400", "pfapi.__main__:main" ]

# RUN pip install .
# EXPOSE 4005
# CMD ["pfapi", "--help"]
# CMD ["uvicorn", "pfapi.__main__:main", "--host", "0.0.0.0", "--port", "4005"]
