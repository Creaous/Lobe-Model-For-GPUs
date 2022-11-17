from lobe import ImageModel
from PIL import Image
import pathlib

predicted = []

def CheckImgs(s):
    # Create a new model to the exported model.
    model = ImageModel.load('import_to_python')

    # Open the image.
    img = Image.open(s)
    # Predict what it is.
    result = model.predict(img)

    # Tell user what we detected it as.
    print(f"\nDetected as : {result.prediction}")
    # Tell user what file we used.
    print(f"File is named {s}\n")

    # Just to split up results.
    print("Predictions:")

    for label, confidence in result.labels:
        # Print all the precentages.
        print(f"{label}: {confidence*100}%")

    # Appened the file name and prediction.
    predicted.append(f"{s} - {result.prediction}")

    # Visualize how the model figured it out.
    #heatmap = model.visualize(img)
    #heatmap.show()

# Create a new path to the test images
path = pathlib.Path('images\\py_testimgs')
# For everything in the path.
for entry in path.iterdir():
    # Check if it's a file.
    if entry.is_file():
        # Tell user we are checking for that file.
        print(f"\nChecking: {entry}")
        # Check the image.
        CheckImgs(entry)

# Tell user we are finished.
print("\nFinished:")

# Print the array of predicted images.
print(*predicted, sep='\n')