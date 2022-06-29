# Step 1: Use official lightweight Python image as base OS.
FROM python:3.7-slim

# Step 2. Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

EXPOSE 8080:8080

# Step 3. Install production dependencies.
RUN pip install -r requirements.txt

# Step 4: Run the web service on container startup using gunicorn webserver.
CMD [ "python", "app.py" ]