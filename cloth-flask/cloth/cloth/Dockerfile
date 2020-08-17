FROM python:3.6

FROM daocloud.io/daocloud/tensorflow:latest

MAINTAINER qtt raqtt0307@126.com

WORKDIR /

COPY . /

RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple

#RUN pip install tensorflow -i https://pypi.tuna.tsinghua.edu.cn/simple/

RUN pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple/

RUN pip install keras -i https://pypi.tuna.tsinghua.edu.cn/simple/

RUN pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple/

#RUN pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple/

RUN pip install pillow -i https://pypi.tuna.tsinghua.edu.cn/simple/

RUN pip install sklearn -i https://pypi.tuna.tsinghua.edu.cn/simple/

RUN pip install cassandra-driver -i https://pypi.tuna.tsinghua.edu.cn/simple/

CMD ["/bin/bash"]




