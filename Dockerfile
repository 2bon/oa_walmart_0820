FROM python:3.8

WORKDIR /hi_walmart

COPY src/* ./
RUN pip install -r requirements.txt
EXPOSE 8080
CMD [ "python3", "hi_walmart.py" ]