## Browser-Based WSI Viewer

### Goal

Explore whole-slide images (WSI) using OpenSlide's Deep Zoom example, served through a local web browser.

### Local setup

The viewer uses the example server from the [OpenSlide Python repository](https://github.com/openslide/openslide-python).

Activate the existing Python virtual environment:

```bash
source ~/uka/wsi_test/wsi-env/bin/activate
python -m pip install Flask
cd ~/uka/wsi_test/openslide-python
```

Start the viewer using the path to a local `.svs` file:

```bash
python examples/deepzoom/deepzoom_server.py \
  --listen 127.0.0.1 \
  --port 5000 \
  /path/to/slide.svs
```

Open `http://127.0.0.1:5000` in a browser. Press `Ctrl+C` in the terminal to stop the server.

### Docker deployment

The Dockerfile is in [`viewer/Dockerfile`](../viewer/Dockerfile). It:

- installs pinned versions of `openslide-python`, `openslide-bin`, Flask and Gunicorn;
- downloads the Deep Zoom example from the matching `openslide-python` release, so the local clone is not needed to build the image;
- runs the viewer with Gunicorn instead of Flask's development server;
- runs as an unprivileged user (`wsi`) instead of root.

Build the image:

```bash
cd ~/uka/wsi_test
sudo docker build -t wsi-viewer viewer/
```

Run the container, replacing the sample path with the actual slide path. If a container named `wsi-viewer` already exists from an earlier build, remove it first:

```bash
sudo docker rm -f wsi-viewer
sudo docker run -d \
  --name wsi-viewer \
  -p 127.0.0.1:5000:5000 \
  -v "$HOME/uka/wsi_test/CMU-1.svs:/data/slide.svs:ro" \
  wsi-viewer
```

The slide is mounted read-only, and the web interface is published on the local machine at port 5000.

Useful commands:

```bash
sudo docker ps
sudo docker logs wsi-viewer
sudo docker stop wsi-viewer
sudo docker start wsi-viewer
```

### Verification checklist

- [x] Local viewer starts successfully.
- [x] Slide can be opened and navigated in the browser.
- [x] Docker image builds successfully.
- [x] Container starts and the browser viewer works.
- [x] Container logs contain no unresolved errors.

### Results

- **Local viewer:** started with the Flask development server; `CMU-1.svs` opened and could be navigated in the browser.
- **2026-10-22, before Docker:** the pinned packages and the exact Gunicorn command from `viewer/Dockerfile` were run outside Docker against `CMU-1.svs`, with no home directory set. The viewer page, `slide.dzi` and sample tiles all returned HTTP 200, and the log showed no errors.
- **2026-10-22, Docker:** the image built from `viewer/Dockerfile`, and the container served `CMU-1.svs` in the browser. After a hard reload and zooming in, `docker logs` showed Gunicorn starting, then the browser's page and tile requests with no errors.

### Notes

- The slide file is stored outside the container and should not be committed to Git.
- To upgrade, change `OPENSLIDE_PYTHON_VERSION` in the Dockerfile; the package and the Deep Zoom example then move together.
- This is a learning prototype, not a production deployment.
