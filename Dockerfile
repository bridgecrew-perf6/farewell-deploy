# 
FROM python:3.9

# 
WORKDIR /raphanow

# 
COPY ./requirements.txt raphanow/requirements.txt

# 
RUN pip install -r requirements.txt

# 
COPY ./raphanow /raphanow/app

# 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
