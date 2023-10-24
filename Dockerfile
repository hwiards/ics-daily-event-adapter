FROM python:3.11
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY main.py /app/
COPY locales /app/locales/

ENV LANG=en_US.UTF-8

CMD ["python", "main.py"]