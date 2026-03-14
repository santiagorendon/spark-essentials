FROM python:3.11-slim

ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH="${JAVA_HOME}/bin:${PATH}"
ENV PYSPARK_PYTHON=python3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends default-jdk-headless procps \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pyspark==3.5.0

WORKDIR /workspace

CMD ["python", "src/main/python/dataframes_basics.py"]
