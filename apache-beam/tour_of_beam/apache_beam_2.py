import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

beam_options = PipelineOptions(
    runner='DataflowRunner',
    project='my-project-id',
    job_name='unique-job-name',
    region='us-central1',
    staging_location='gs://my-bucket/staging',
    temp_location='gs://my-bucket/temp',
)

pipeline = beam.Pipeline(options=beam_options)

with beam.Pipeline() as p:
  pass  # build your pipeline here

  # Run the following from the command-line
  # python apache_beam_2.py \
  # --project='my-project-id' \
  # --job_name='unique-job-name' \
  # --region='us-central1' \
  # --staging_location='gs://my-bucket/staging' \
  # --temp_location='gs://my-bucket/temp'