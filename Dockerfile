# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /requirements.txt

# 
RUN pip install -r requirements.txt

# 
COPY ./app /code/app

# 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
