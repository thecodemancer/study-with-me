gcloud dataflow flex-template build gs://$BUCKET/df_test.json \
 --image="${REGION}-docker.pkg.dev/${PROJECT}/process-audio/df-template:latest" \
 --network="${NETWORK}" \
 --subnetwork="${SUBNETWORK}" \
 --sdk-language="PYTHON" \
 --metadata-file="metadata.json"
