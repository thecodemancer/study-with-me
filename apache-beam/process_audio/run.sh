gcloud dataflow flex-template run "df-work2-`date +%Y%m%d-%H%M%S`" \
 --template-file-gcs-location "gs://$BUCKET/df_test.json" \
 --parameters output=$BUCKET,sdk_container_image=us.gcr.io/$PROJECT/df-worker:latest \
 --region $REGION \
 --project $PROJECT

 