FROM python:3.10
LABEL authors="bilgi"
ENV PYTHONUNBUFFERED=1
WORKDIR /plotly_doc
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8222
CMD ["python","manage.py","runserver"]