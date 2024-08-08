gcloud dataflow flex-template run "df-work2-`date +%Y%m%d-%H%M%S`" \
 --template-file-gcs-location "gs://$BUCKET/df_test.json" \
 --project $PROJECT \
 --region $REGION \
 --network "${NETWORK}" \
 --subnetwork "${SUBNETWORK}" \
 --additional-experiments="use_runner_v2,use_network_tags=http-server" \
 --parameters output=$BUCKET,sdk_container_image=${REGION}-docker.pkg.dev/${PROJECT}/process-audio/df-worker
