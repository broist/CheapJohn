FROM mcr.microsoft.com/playwright/python:v1.47.0-jammy

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends cron \
    && rm -rf /var/lib/apt/lists/*

COPY src/ ./src/
COPY cron/crontab /etc/cron.d/cheapjohn-cron
RUN chmod 0644 /etc/cron.d/cheapjohn-cron \
    && crontab /etc/cron.d/cheapjohn-cron \
    && touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log
