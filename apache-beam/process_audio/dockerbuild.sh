docker build -t local:test .
docker tag local:test us.gcr.io/$PROJECT/df-template:latest
docker push us.gcr.io/$PROJECT/df-template:latest