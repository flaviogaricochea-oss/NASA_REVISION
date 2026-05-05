FROM python:3.11-slim-bullseye
WORKDIR /app
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*
COPY mission_telemetry.py .
VOLUME ["/app/data"]
ENTRYPOINT ["python", "mission_telemetry.py"]
