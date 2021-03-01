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
# In the case of a proxy (located at say 192.168.13.14:3128), do:
#
#   export PROXY=192.168.13.14:3128
#   docker build --build-arg http_proxy=$PROXY --build-arg UID=$UID -t local/pfapi.
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

ENV DEBIAN_FRONTEND=noninteractive APPLICATION_MODE="production"

WORKDIR /usr/local/src

COPY requirements.txt .
RUN apt-get update && apt-get upgrade
RUN pip install -r requirements.txt

COPY . .
RUN pip install .
EXPOSE 4005

# CMD ["pfapi", "--help"]

CMD ["uvicorn", "pfapi.main:app", "--host", "0.0.0.0", "--port", "4005"]
