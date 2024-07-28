FROM gcr.io/dataflow-templates-base/python310-template-launcher-base

ENV FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE="/template/requirements.txt"
ENV FLEX_TEMPLATE_PYTHON_PY_FILE="/template/df_worker_test.py"

COPY . /template

RUN apt-get update \
    && apt-get install libavcodec-extra ffmpeg -y

# We could get rid of installing libffi-dev and git, or we could leave them.
RUN apt-get update \
    && rm -rf /var/lib/apt/lists/* \
    # Upgrade pip and install the requirements.
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r $FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE \
    # Download the requirements to speed up launching the Dataflow job.
    && pip download --no-cache-dir --dest /tmp/dataflow-requirements-cache -r $FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE

# Since we already downloaded all the dependencies, there's no need to rebuild everything.
ENV PIP_NO_DEPS=True

ENTRYPOINT ["/opt/google/dataflow/python_template_launcher"]
