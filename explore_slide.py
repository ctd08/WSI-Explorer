import openslide
import sys

def save_thumbnail(slide, output_filename="thumbnail.png", size=(512, 512)):
                        #slide = openslide.OpenSlide(slide_path)
                        thumbnail = slide.get_thumbnail(size)
                        thumbnail.save(output_filename)
                        print(f"Thumbnail saved successfully as {output_filename}")



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

		
		save_thumbnail(slide)

		slide.close()
	except Exception as e:
		print(f"Error opening slide: {e}")


if __name__=="__main__":
	if len(sys.argv) > 1:
		explore_wsi(sys.argv[1])
	else:
		print("Please provide a path to a slide file.")
