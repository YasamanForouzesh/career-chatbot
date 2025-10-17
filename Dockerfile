FROM python:3.13
WORKDIR /app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --progress-bar off -r requirements.txt


# Copy in the source code
COPY . /app
EXPOSE 8080

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]