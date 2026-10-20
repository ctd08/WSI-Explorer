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

## Observations

Record the output, any unexpected behavior, and any changes made to resolve errors.

## Limitations

The current script catches exceptions and prints a general error message. It does not yet distinguish between a missing file, an unsupported file format, and other failures.

The tests in this document should be marked as passed only after their results have been observed.
