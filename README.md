# WSI Explorer — Beginner Project

A beginner-friendly project exploring Whole Slide Imaging (WSI) and digital pathology using **QuPath**, **Python**, and **OpenSlide**.

## What You'll Build & Learn
* **Digital Pathology Basics:** Visualizing gigapixel multi-resolution image pyramids in QuPath.
* **Environment Configuration:** Setting up a Python virtual environment (`venv`) alongside system/binary dependencies (`openslide-bin`) in WSL.
* **Metadata Extraction:** Programmatically reading dimensions, resolution levels, vendor info, and micrometers-per-pixel (MPP) metadata.
* **Thumbnail Generation:** Extracting and saving downsampled overviews of massive slides.
* **Robust Error Handling:** Handling valid files, missing files, and unsupported file types gracefully.

---
## Documentation

- [Learning notes](docs/LEARNING_NOTES.md)
- [Testing notes](docs/TESTING.md)
- [WSI viewer and Docker](docs/WSI_VIEWER.md)


## Prerequisites & Installation

1. **WSL / Linux Environment:** Python 3 and virtual environments enabled.
2. **Install Dependencies:**
   ```bash
   python3 -m venv wsi-env
   source wsi-env/bin/activate
   pip install openslide-python openslide-bin

## Browser-Based WSI Viewer

### Goal

Explore whole-slide images (WSI) using OpenSlide's Deep Zoom example, served through a local web browser.

### Local setup

The viewer uses the example server from the [OpenSlide Python repository](https://github.com/openslide/openslide-python).

Activate the existing Python virtual environment:

```bash
source ~/uka/wsi_test/wsi-env/bin/activate
python -m pip install Flask
cd ~/uka/openslide-python
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

A prototype Dockerfile, `Dockerfile.wsi`, is located in the cloned OpenSlide Python repository.

Build the image:

```bash
cd ~/uka/openslide-python
sudo docker build -f Dockerfile.wsi -t wsi-viewer .
```

Run the container, replacing the sample path with the actual slide path:

```bash
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

- [ ] Local viewer starts successfully.
- [ ] Slide can be opened and navigated in the browser.
- [ ] Docker image builds successfully.
- [ ] Container starts and the browser viewer works.
- [ ] Container logs contain no unresolved errors.

Record the actual test results here after verification.

### Notes

- The slide file is stored outside the container and should not be committed to Git.
- The Dockerfile currently belongs to the cloned OpenSlide repository; keep its build context in mind when rebuilding the image.
- This is a learning prototype, not a production deployment.
