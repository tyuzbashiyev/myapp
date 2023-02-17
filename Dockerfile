FROM python:3

COPY bin/server.py /root/myapp/bin/server.py
COPY files/index.html /root/myapp/files/index.html

EXPOSE 8080

ENTRYPOINT ["python3", "/root/myapp/bin/server.py"]