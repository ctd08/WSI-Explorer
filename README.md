# WSI Explorer — Beginner Project

A beginner-friendly project exploring Whole Slide Imaging (WSI) and digital pathology using **QuPath**, **Python**, and **OpenSlide**.

## What You'll Build & Learn
* **Digital Pathology Basics:** Visualizing gigapixel multi-resolution image pyramids in QuPath.
* **Environment Configuration:** Setting up a Python virtual environment (`venv`) alongside system/binary dependencies (`openslide-bin`) in WSL.
* **Metadata Extraction:** Programmatically reading dimensions, resolution levels, vendor info, and micrometers-per-pixel (MPP) metadata.
* **Thumbnail Generation:** Extracting and saving downsampled overviews of massive slides.
* **Privacy Check:** Listing every metadata field, saving the label and macro images, and flagging data that could identify a patient or case.
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
   ```

## Browser-Based WSI Viewer

To view a slide in the browser, locally or in Docker, see [WSI viewer and Docker](docs/WSI_VIEWER.md).
