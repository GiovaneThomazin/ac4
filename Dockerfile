FROM python:3.6.1-alpine
RUN pip install flask
COPY fibonacci.py /fibonacci.py
CMD ["python","fibonacci.py"]
