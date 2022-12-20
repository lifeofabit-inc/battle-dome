FROM python:3.9
LABEL Matt Downs <lifeofabit.com>

ENV PYTHONIOENCODING=utf-8
ENV LANG C.UTF-8

ARG SCRAPE_USER_HOME=/usr/local/scrape

RUN apt-get update -y 

RUN apt-get install -y --no-install-recommends \
    vim \
    make \
    python3-dev \ 
    python3-pip

RUN apt-get install -y --no-install-recommends \
    libxml2-dev \ 
    libxslt1-dev \
    zlib1g-dev \
    libffi-dev \
    libssl-dev

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add dependencies to the container and install 
ADD requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip setuptools
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt

# Create user and scrapy project
COPY scripts/deploy.sh /deploy.sh
RUN useradd -mU scrape
RUN chmod +x /deploy.sh

USER scrape
WORKDIR ${SCRAPE_USER_HOME}
ENTRYPOINT ["/deploy.sh"]
