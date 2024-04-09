
# Dockerfile
FROM python:3.10
ENV PYTHONUNBUFFERED 1

#RUN adduser --disabled-password --gecos '' django
ENV PATH=${PATH}:/plotly_doc/home/.local/bin
#USER django
WORKDIR /plotly_doc/home/
COPY ./chromedriver .local/bin
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

CMD ["python","./manage.py", "runserver", "0.0.0.0:8222"]
