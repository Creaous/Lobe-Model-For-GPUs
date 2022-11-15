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
        'q': sys.argv[1], 		# query 
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
        'content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    data = []
    old_page_result = []

    while True:
        try:
            os.mkdir("download")
        except FileExistsError:
            pass

        html = requests.get('https://search.brave.com/api/images', headers=headers, params=params, verify=False).json()

        new_page_result = html['results']

        if new_page_result == old_page_result:
            break

        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        for result in new_page_result:
            try:
                os.mkdir(os.path.join("download", sys.argv[1]))
            except FileExistsError:
                pass

            try:
                print("INFO: Downloading " + result.get('properties').get('url'))
                urllib.request.urlretrieve(result.get('properties').get('url'), "download/" + sys.argv[1] + "/" + str(randrange(100000, 999999)) + ".jpg")
            except Exception:
                print("WARNING: An error occured while trying to download from " + result.get('properties').get('url'))
                pass

            data.append({
                'title': result.get('title'),
                'link': result.get('url'),
                'source': result.get('source'),
                'width': result.get('properties').get('width'),
                'height': result.get('properties').get('height'),
                'image': result.get('properties').get('url')
            })

        params['offset'] += 151
        old_page_result = new_page_result

    return data


if __name__ == "__main__":
    brave_images = scrape_brave_images()
    print(json.dumps(brave_images, indent=2))