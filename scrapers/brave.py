# SOURCE: https://serpapi.com/blog/scrape-brave-search-organic-results-with-python/\
# Edited to fit the needs of this project.

# Import important stuff
import os
from random import randrange
import sys
import requests, json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request

def scrape_brave_images():
    # https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls
    params = {
        'q': sys.argv[1], 		# Search query 
        'source': 'web',		# source 
        'size': 'All',			# size (Small, Medium, Large, Wallpaper) 
        '_type': 'All',			# type (Photo, Clipart, AnimatedGifHttps, Transparent) 
        'layout': 'All',		# layout (Square, Tall, Wide) 
        'color': 'All',			# colors (Monochrome, ColorOnly, Red etc) 
        'license': 'All',		# license (Public, Share, Modify etc)
        'offset': 0
    }

    # https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    # Create new data object.
    data = []
    # Create old page result object.
    old_page_result = []

    # While the scraper is running.
    while True:
        try:
            # Create download directory.
            os.mkdir("download")
        except FileExistsError:
            # Pass off the error.
            pass

        # Get API result of the search query and images (make json).
        html = requests.get('https://search.brave.com/api/images', headers=headers, params=params, verify=False).json()

        # Get the results from the request.
        new_page_result = html['results']

        # Ignore old page results.
        if new_page_result == old_page_result:
            break

        # Start new opener (for downloading).
        opener = urllib.request.build_opener()
        # Add user agent to minimise (not elimate) getting blocked for being a bot.
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')]
        # Install opener onto the requests.
        urllib.request.install_opener(opener)

        for result in new_page_result:
            try:
                # Create a folder in download with the name of the query.
                os.mkdir(os.path.join("download", sys.argv[1]))
            except FileExistsError:
                # Pass off the error.
                pass

            try:
                # Tell user what we are downloading.
                print("INFO: Downloading " + result.get('properties').get('url'))
                # Download the image with a random name and as a .jpg.
                urllib.request.urlretrieve(result.get('properties').get('url'), "download/" + sys.argv[1] + "/" + str(randrange(100000, 999999)) + ".jpg")
            except Exception:
                # Let the user know an error has happened.
                print("WARNING: An error occured while trying to download from " + result.get('properties').get('url'))
                # Pass off the error.
                pass

            # Append all of the data to the data object.
            data.append({
                'title': result.get('title'),
                'link': result.get('url'),
                'source': result.get('source'),
                'width': result.get('properties').get('width'),
                'height': result.get('properties').get('height'),
                'image': result.get('properties').get('url')
            })

        # Set the offset param.
        params['offset'] += 151
        # Set old page result to the new one.
        old_page_result = new_page_result

    # Return the data.
    return data


if __name__ == "__main__":
    # Create a new object for the function.
    brave_images = scrape_brave_images()
    # Print all of the json dumps for those images.
    print(json.dumps(brave_images, indent=2))