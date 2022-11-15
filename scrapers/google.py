# Import OS library
import os
# Import sys library
import sys
# Import random function.
from random import randrange
# Import Google image search library
from google_images_search import GoogleImagesSearch
# Import dotenv library
from dotenv import load_dotenv

# Load the .env into memory.
load_dotenv()

# Login using our .env variables.
gis = GoogleImagesSearch(os.getenv('KEY'), os.getenv('CX'))

# Let the user know that we are scraping for the desired amount of images.
print("Scraping images for : " + sys.argv[1] + " and downloading " + sys.argv[2] + " image(s)")

# The search params.
_search_params = {
    'q': sys.argv[1],
    'num': int(sys.argv[2]),
    'fileType': 'png|jpg'
}

# Here we actually search for the images and set the custom file name to a random integer to prevent illegal names.
gis.search(search_params=_search_params, path_to_dir='download/' + sys.argv[1] + '/', custom_image_name=str(randrange(100000, 999999)))