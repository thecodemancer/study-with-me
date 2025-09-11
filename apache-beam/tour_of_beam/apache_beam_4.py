import argparse
import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions

def main(argv=None, save_main_session=True):

    parser = argparse.ArgumentParser()
    parser.add_argument('--input',dest='input', default='apache_beam_3.py',
        help='Input file to process.')
    known_args, pipeline_args = parser.parse_known_args(argv)

    pipeline_options = PipelineOptions(pipeline_args)

    with beam.Pipeline(options=pipeline_options) as p:

        lines = p   | 'Read' >> ReadFromText(known_args.input)
        
        output = lines | 'Write' >> beam.Map(lambda line: print(line))

if __name__ == '__main__':
    main()

# Run the following from the command-line
# python apache_beam_4.py \
# --runner='PortableRunner' \
# --job_endpoint='localhost:8099' \
# --environment_type='LOOPBACK'    