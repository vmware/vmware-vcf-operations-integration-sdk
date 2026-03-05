FROM python:3.11.12-slim-bookworm

# Apply latest security patches for Debian packages
RUN apt-get -q update && \
    apt-get -yq upgrade && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade system-level pip/setuptools to fix bundled CVEs
RUN pip3 install --no-cache-dir --upgrade pip setuptools wheel

# Ensure that the /var/log directory is writable by the server/adapter
RUN chmod 777 /var/log

# Create LPU and create/set work directory
RUN useradd --create-home --shell /bin/bash aria-ops-adapter-user
USER aria-ops-adapter-user
WORKDIR /home/aria-ops-adapter-user/src/app

# Copy project into container and install requirements
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 443
EXPOSE 8080

ENTRYPOINT ["python3"]
CMD ["-m", "swagger_server"]
