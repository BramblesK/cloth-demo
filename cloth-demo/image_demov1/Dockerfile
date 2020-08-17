FROM python:3.6

FROM daocloud.io/daocloud/tensorflow:latest

MAINTAINER qtt raqtt0307@126.com

WORKDIR /

COPY . /

#ADD ./image_test /Users/qtt/Documents/image_demo/image_test

ADD sources.list /etc/apt

RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple

#RUN pip install tensorflow -i https://pypi.tuna.tsinghua.edu.cn/simple/

RUN pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple/

RUN pip install keras -i https://pypi.tuna.tsinghua.edu.cn/simple/

RUN pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple/

#RUN pip install tensorflow -i https://pypi.tuna.tsinghua.edu.cn/simple/

EXPOSE 80

CMD ["/bin/bash"]

#ENTRYPOINT [ "python" ]

#CMD [ "image_test/app.py" ]



