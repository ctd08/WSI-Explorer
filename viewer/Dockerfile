FROM python:3.12-slim

# The Deep Zoom example below is taken from the same release as this package
ARG OPENSLIDE_PYTHON_VERSION=1.4.6

RUN python -m pip install --no-cache-dir \
        openslide-python==${OPENSLIDE_PYTHON_VERSION} \
        openslide-bin==4.0.1.2 \
        Flask==3.1.3 \
        gunicorn==26.2.0

WORKDIR /app

ADD https://github.com/openslide/openslide-python/archive/refs/tags/v${OPENSLIDE_PYTHON_VERSION}.tar.gz /tmp/openslide-python.tar.gz
RUN tar -xzf /tmp/openslide-python.tar.gz -C /app --strip-components=3 \
        openslide-python-${OPENSLIDE_PYTHON_VERSION}/examples/deepzoom \
    && rm /tmp/openslide-python.tar.gz

RUN useradd --system --no-create-home wsi
USER wsi

EXPOSE 5000

# The user has no home directory, so Gunicorn's control socket is turned off
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "4", \
     "--access-logfile", "-", "--no-control-socket", \
     "deepzoom_server:create_app(config={'DEEPZOOM_SLIDE': '/data/slide.svs'})"]
