docker build -t df-worker:latest .
docker tag df-worker:latest us.gcr.io/$PROJECT/df-worker:latest
docker push us.gcr.io/$PROJECT/df-worker:latest
