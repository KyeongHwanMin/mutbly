FROM python:3.9.9

WORKDIR /home/

RUN git clone https://github.com/KyeongHwanMin/mutbly.git

RUN pip install gunicorn

WORKDIR /home/backend-mission/missions/week2/back/

RUN pip install -r requirements.txt

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "backend-mission/missions/week2/back.wsgi", "--bind", "0.0.0.0:8000"]