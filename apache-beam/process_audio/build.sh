gcloud dataflow flex-template build gs://$BUCKET/df_test.json \
 --image "us.gcr.io/$PROJECT/df-template:latest" \
 --sdk-language "PYTHON" \
 --metadata-file "metadata.json" \
 --project $PROJECT