# Lobe Model For GPUs
The project includes 3 (technically 4) scripts. One to download images from the Brave search engine and one to download images from the Google search engine (needing credentials). Finally, the last script is the main one being the one that imports the exported Lobe model and checks it against some test images in its own directory. This directory is under ‘images/py_testimgs’ allowing any images under that path to be checked. When all predictions have been made it prints out a neat looking array (on separate lines) to tell you all the data at once.

This is a simple Lobe model to detect GPU types (only NVIDIA). This project was made for STEM at my school.

## Usage
1. Create a venv
 - `python3 -m venv .venv`
 - `.venv\Scripts\activate`
2. Install requirements
 - `pip install -r requirements.txt`
3. Start the model
 - `py __main__.py`