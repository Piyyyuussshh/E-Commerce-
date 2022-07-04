FROM python

WORKDIR /djangoApp

COPY requirments.txt requirments.txt

RUN pip install -r requirments.txt

COPY . .

CMD = ["python","manage.py","runserver","0.0.0.0:8000"]