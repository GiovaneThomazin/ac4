FROM python:3.6.1-alpine
RUN pip install flask
COPY fibo.py /fibo.py
CMD ["python","fibo.py"]
