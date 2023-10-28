# FROM python:3.9-slim

# #WORKDIR /app

# COPY version.txt version.txt
# RUN pip3 install -r version.txt

# COPY . app.py

# EXPOSE 5000

# RUN FLASK_APP=app.py

# CMD [ "flask", "run", "--host=0.0.0.0"]

FROM python:3.9-slim

WORKDIR /new

COPY . /new

RUN pip install flask 

EXPOSE 5000

######
CMD [ "python3", "./new.py" ]
