docker build -t local:test .
docker tag local:test $REGION-docker.pkg.dev/$PROJECT/process-audio/df-template:latest
docker push $REGION-docker.pkg.dev/$PROJECT/process-audio/df-template:latest