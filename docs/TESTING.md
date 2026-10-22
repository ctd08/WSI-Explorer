# Testing: WSI Explorer

## Test Environment

- Operating system: Debian under WSL on Windows
- Language: Python
- Image library: OpenSlide Python
- Sample image: `CMU-1.svs`

## Test Cases

### Test 1: Valid WSI file

**Input:** Path to `CMU-1.svs`

**Procedure:**
1. Run the script with the sample slide path.
2. Check that the script prints the image dimensions.
3. Check the number of resolution levels and level dimensions.
4. Check the available metadata.
5. Check that the thumbnail is generated.

**Expected result:** The image is opened, available properties are printed, and a thumbnail is saved.

**Actual result:** All steps are followed.

**Status:** DONE

### Test 2: Missing file

**Input:** A path to a file that does not exist.

**Procedure:**

```bash
python explore_slide.py missing-slide.svs
```

**Expected result:** The script displays an error message instead of terminating with an unhandled exception.

**Actual result:** Error opening slide: Unsupported or missing image file

**Status:** DONE

### Test 3: Unsupported file

**Input:** An existing file that OpenSlide cannot read as a supported slide format.

**Procedure:** Run the script with the path to an existing plain-text file.

**Expected result:** The script displays an error message for the unsupported input.

**Actual result:** Error opening slide: Unsupported or missing image file.

**Status:** DONE

### Test 4: All properties, associated images and privacy check

**Input:** Path to `CMU-1.svs`

**Procedure:**
1. Run the script with the sample slide path.
2. Check that every property is printed under "All Properties".
3. Check that each associated image is saved as `associated_<name>.png`.
4. Check the "Privacy Check" section.

**Expected result:** All properties are printed. The label, macro and thumbnail images are saved. The privacy check lists the date, time, user, filename, image ID and scanner ID fields, plus the two fields that repeat them (`openslide.comment`, `tiff.ImageDescription`), and names the label and macro images.

**Actual result:** 52 properties printed. `associated_label.png`, `associated_macro.png` and `associated_thumbnail.png` saved. 8 properties flagged, as expected, and the label and macro images named. The label image shows "CMU-1" handwritten on the sticker; the macro image shows the whole glass slide, but not its label. Tests 2 and 3 were re-run afterwards and still give the same error message.

**Status:** DONE

## Observations

Record the output, any unexpected behavior, and any changes made to resolve errors.

## Limitations

The current script catches exceptions and prints a general error message. It does not yet distinguish between a missing file, an unsupported file format, and other failures.

The privacy check only looks at property names, not their values. A field with an unexpected name, such as one from another scanner vendor, is not flagged even if it contains a patient name. It is a learning aid, not a de-identification tool.

The tests in this document should be marked as passed only after their results have been observed.
