FROM python:3.11-slim

ARG POSTGRES_VERSION=42.6.0

ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH="${JAVA_HOME}/bin:${PATH}"
ENV PYSPARK_PYTHON=python3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl default-jdk-headless procps \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pyspark==3.5.0

RUN set -eux; \
    jars_dir="$(python -c "import pathlib, pyspark; print(pathlib.Path(pyspark.__file__).resolve().parent / 'jars')")"; \
    curl -fsSL \
      "https://repo1.maven.org/maven2/org/postgresql/postgresql/${POSTGRES_VERSION}/postgresql-${POSTGRES_VERSION}.jar" \
      -o "${jars_dir}/postgresql-${POSTGRES_VERSION}.jar"

WORKDIR /workspace

CMD ["python", "src/main/python/dataframes_basics.py"]
