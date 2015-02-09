from centos:centos7

RUN yum install -y rpm-build

ADD builder.sh /usr/bin/builder.sh
ENTRYPOINT ["builder.sh"]
