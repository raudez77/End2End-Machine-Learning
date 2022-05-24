# This file is for Amazon Elastick Beanstalk
FROM python:3.7-slim-bullseye

WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY . /app
RUN pip install -r /app/requirements/requirements.txt

EXPOSE 5000

# Run the application:
CMD ["python", "/app/classification_model/application.py"]