FROM python:3
ENV PYTHONUNBUFFERED True
# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
# Install production dependencies.
RUN pip install -r requirements.txt
RUN pip install gunicorn

CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 app:app

# updated requirements.txt
# engine 
# deleted db_config