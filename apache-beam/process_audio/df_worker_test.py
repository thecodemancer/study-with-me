import argparse
import logging
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class ProcessAudio(beam.DoFn):
    def process(self, element, *args, **kwargs):
        from google.cloud import storage
        import io
        from pydub import AudioSegment

        # Initialize GCS client and download the file
        client = storage.Client()
        bucket = client.get_bucket(element['bucket'])
        blob = bucket.get_blob('rock_and_roll.mp3')
        audio_data = blob.download_as_bytes()

        # Use PyDub to process the audio
        audio = AudioSegment.from_file(io.BytesIO(audio_data), format="mp3")
        processed_audio = audio.set_channels(1).set_frame_rate(16000)  # Example processing

        # Write the processed audio to an in-memory file
        output_buffer = io.BytesIO()
        processed_audio.export(output_buffer, format="mp3")
        output_buffer.seek(0)

        yield {'bucket': element['bucket'], 'name': 'rock_and_roll_processed.mp3', 'data': output_buffer.read()}

class WriteToGCS(beam.DoFn):
    def process(self, element, output_bucket, *args, **kwargs):
        from google.cloud import storage
        client = storage.Client()
        bucket = client.get_bucket(output_bucket)
        blob = bucket.blob(f"/output/{element['name']}")
        blob.upload_from_string(element['data'], content_type="audio/mp3")
        logging.info(f"Processed file written to: gs://{output_bucket}/output/{element['name']}")

def run(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--sdk_container_image', required=True)

    known_args, pipeline_args = parser.parse_known_args(argv)
    #pipeline_options = PipelineOptions(pipeline_args)

        #sdk_location="container"
        #sdk_container_image="us-south1-docker.pkg.dev/evidentemvp/evidente/dataflow/insights_interpreter:latest"
    pipeline_options = PipelineOptions(
        streaming=False,
        save_main_session=True,
        sdk_location="container",
        sdk_container_image=known_args.sdk_container_image
    )
    logging.info(pipeline_options)
    #options.setSdkContainerImage(known_args.sdk_container_image)
    #logging.info(options)

    with beam.Pipeline(options=pipeline_options) as p:
        # Read the input file from GCS
        input_file = (p 
                      | "Create file list" >> beam.Create([{'bucket': known_args.output}])
                      )

        # Process the audio file
        processed_audio = (input_file
                           | "Process audio" >> beam.ParDo(ProcessAudio())
                           )

        # Write the processed audio back to GCS
        (processed_audio
         | "Write to GCS" >> beam.ParDo(WriteToGCS(), output_bucket=known_args.output)
         )

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()
