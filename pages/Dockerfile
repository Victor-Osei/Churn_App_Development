FROM ubuntu:latest 

WORKDIR /usr/app/src

ARG LANG="en_US.UTF-8"

# Downloads and installations
RUN apt-get update\ && apt-get install -y --no-install-recommends \
apt -utils \
Locales \
python3-pip \
python3-yaml \
rsyslog systemd systemd-cron sudo\ && apt-get clean


COPY requirements.txt ./
RUN pip3 install --upgrade pip \ && pip3 install -r requirements.txt

COPY ./ ./

# Tell the image what to do
CMD ["streamlit", "run", "app.py"]