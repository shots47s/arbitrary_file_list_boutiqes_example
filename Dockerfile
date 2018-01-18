from centos:latest
RUN yum update -y && \
    yum install python -y

ADD arb_file_example.py /bin/
RUN chmod a+x /bin/arb_file_example.py