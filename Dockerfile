# 
FROM python:3.9

# 
WORKDIR /raphanow

# 
COPY raphanow/requirements.txt ./requirements.txt

# 
RUN pip install -r requirements.txt

# 
COPY ./raphanow /raphanow/app

# 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
