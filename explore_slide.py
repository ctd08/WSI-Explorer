import openslide
import sys

# words in a property name that suggest it may identify a patient, case, person or scanner
# (a keyword check for learning, not a complete de-identification check)
IDENTIFYING_KEYWORDS = ("date", "time", "user", "filename", "imageid", "scanscope id",
	"description", "comment", "barcode", "patient")

# associated images that are photos of the glass slide and can show its label
LABEL_IMAGES = ("label", "macro")

def save_thumbnail(slide, output_filename="thumbnail.png", size=(512, 512)):
                        #slide = openslide.OpenSlide(slide_path)
                        thumbnail = slide.get_thumbnail(size)
                        thumbnail.save(output_filename)
                        print(f"Thumbnail saved successfully as {output_filename}")


def print_all_properties(slide):
	print(f"\n---All Properties ({len(slide.properties)}) ---")
	for key in sorted(slide.properties):
		print(f"{key} = {slide.properties[key]}")


def save_associated_images(slide):
	# extra images stored next to the main image, e.g. label, macro, thumbnail
	print("\n---Associated Images ---")
	if not slide.associated_images:
		print("None")
	for name, image in slide.associated_images.items():
		output_filename = f"associated_{name}.png"
		image.save(output_filename)
		print(f"{name} {image.size} saved as {output_filename}")


def print_privacy_check(slide):
	print("\n---Privacy Check (keyword-based, not complete) ---")
	identifying_keys = [key for key in sorted(slide.properties)
		if any(word in key.lower() for word in IDENTIFYING_KEYWORDS)]
	label_images = [name for name in slide.associated_images if name in LABEL_IMAGES]

	if identifying_keys:
		print("Properties that may identify a patient, case, person or scanner:")
		for key in identifying_keys:
			print(f"  {key} = {slide.properties[key]}")
	else:
		print("No properties matched the keywords.")

	if label_images:
		print(f"Images that may show the slide label: {', '.join(label_images)}")
	else:
		print("No label or macro images found.")



def explore_wsi(slide_path):

	try:
		slide= openslide.OpenSlide(slide_path)
		print(f"---Successfully loaded: {slide_path}---")

		# dimensions at level 0 (highest resolution)
		dimensions = slide.dimensions
		print(f"Level 0 Dimensions (Width, Height) : {dimensions}")

		# resolution levels
		level_count = slide.level_count
		print(f"Number of Resolution Levels: {level_count}")
		print(f"Level Downsamples: {slide.level_downsamples}")
		print(f"Level Dimensions: {slide.level_dimensions}")

		#metadata 
		#mpp = micrometers per pixel
		print("\n---Metadata ---")
		vendor = slide.properties.get(openslide.PROPERTY_NAME_VENDOR, "Unknown")
		mpp_x = slide.properties.get(openslide.PROPERTY_NAME_MPP_X, "Unknown")
		mpp_y = slide.properties.get(openslide.PROPERTY_NAME_MPP_Y, "Unknown")

		print(f"Scanner Vendor: {vendor}")
		print(f"Microns Per Pixel (X): {mpp_x}")
		print(f"Microns Per Pixel (Y) : {mpp_y}")

		print_all_properties(slide)

		save_thumbnail(slide)
		save_associated_images(slide)

		print_privacy_check(slide)

		slide.close()
	except Exception as e:
		print(f"Error opening slide: {e}")


if __name__=="__main__":
	if len(sys.argv) > 1:
		explore_wsi(sys.argv[1])
	else:
		print("Please provide a path to a slide file.")
