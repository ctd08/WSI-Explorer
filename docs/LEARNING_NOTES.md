# Learning Notes: Whole-Slide Imaging

## 1. What is WSI?

Whole-slide imaging (WSI) is the digitization of an entire microscope slide into a high-resolution digital image.

WSI files can be very large. Many formats store several resolution levels so that viewers can display an overview and load more detailed regions when the user zooms in.

## 2. QuPath

QuPath is an application for viewing and analyzing digital pathology images.

During this project, I used QuPath to open a public sample slide, navigate the image at different zoom levels, inspect image properties, and create annotations.

## 3. OpenSlide

OpenSlide is a library for reading supported whole-slide image formats.

I used its Python interface to inspect a slide without loading the entire image into a conventional image editor.

## 4. Image Dimensions and Resolution Levels

- **Level 0 dimensions:** the width and height at the highest available resolution.
- **Resolution levels:** alternative resolutions provided by the slide format.
- **Downsample factors:** indicate how much smaller each level is compared with level 0.
- **Level dimensions:** the width and height of each resolution level.

These properties help explain how a viewer can navigate very large images efficiently.

## 5. Microns per Pixel (MPP)

MPP describes the physical distance represented by one pixel, typically in micrometers.

OpenSlide may provide separate X and Y values. These values can help interpret image scale when the metadata is available.

## 6. Thumbnail Generation

A thumbnail is a smaller overview image generated from the original slide.

In this project, OpenSlide's `get_thumbnail()` method creates a thumbnail that can be saved as a standard image file.

The thumbnail makes it easier to preview the slide without opening the full-resolution image.

## 7. Development Environment

The project was developed in Debian under WSL on Windows, using a Python virtual environment.

The Python interface and the underlying OpenSlide native library are separate dependencies. Both must be available for the script to work.

## 8. What I Learned

- How to use QuPath to explore a whole-slide image.
- How to create and activate a Python virtual environment.
- How to install and troubleshoot OpenSlide dependencies.
- How to read image dimensions, resolution levels, and metadata.
- How to generate a thumbnail programmatically.
- How to use Git to track source code and documentation.
- Why large image files and generated outputs should generally be excluded from source control.
