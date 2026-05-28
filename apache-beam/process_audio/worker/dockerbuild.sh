docker build -t df-worker:latest .
docker tag df-worker:latest ${REGION}-docker.pkg.dev/${PROJECT}/process-audio/df-worker:latest
docker push ${REGION}-docker.pkg.dev/${PROJECT}/process-audio/df-worker:latest
