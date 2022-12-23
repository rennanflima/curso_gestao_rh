FROM python:3.10-slim

ENV TZ America/Rio_Branco
ENV LANG pt_BR.UTF-8

RUN apt-get clean && apt-get update && apt-get install -y git locales tzdata && \
  rm -rf /var/lib/apt/lists/* && \
  ln -sf /usr/share/zoneinfo/America/Rio_Branco /etc/localtime && \
  locale-gen pt_BR.UTF-8 && \
  dpkg-reconfigure -f noninteractive locales && \
  dpkg-reconfigure -f noninteractive tzdata

ENV LC_ALL pt_BR.UTF-8

RUN useradd -ms /bin/bash python

RUN pip install pipenv

USER python

WORKDIR /home/python/app

ENV PIPENV_VENV_IN_PROJECT=True

CMD ["./.docker/start_dev.sh"]
