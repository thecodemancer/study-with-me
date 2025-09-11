import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

beam_options = PipelineOptions(
    runner='DirectRunner',
)
pipeline = beam.Pipeline(options=beam_options)

with beam.Pipeline() as p:
  # build your pipeline here
  #pass
  output = p | beam.Create([None]) | beam.Map(lambda x: print("hello world"))


