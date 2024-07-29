# Stage 1: Base image
FROM python:3.10-slim as base

RUN apt-get update \
    && apt-get install libavcodec-extra ffmpeg -y

# Install Apache Beam SDK and other dependencies
RUN pip install --no-cache-dir \
    apache-beam[gcp]==2.57.0 \
    boto3==1.26.90 \
    firebase_admin==6.1.0 \
    gcsfs \
    pydub \
    google-cloud-storage

# Copy files from the official SDK image, including script/dependencies
COPY --from=apache/beam_python3.10_sdk:2.57.0 /opt/apache/beam /opt/apache/beam

# Set the entrypoint to Apache Beam SDK launcher
ENTRYPOINT ["/opt/apache/beam/boot"]
