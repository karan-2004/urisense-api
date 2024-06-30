import cv2
import numpy as np
from django.conf import settings

def extract_chemical_colors(image_path):
    # List of chemical names in the same order as they appear on the strip
    chemicals = [
        "Leukocytes",
        "Nitrite",
        "Urobilinogen",
        "Protein",
        "pH",
        "Blood",
        "Specific Gravity",
        "Ketone",
        "Bilirubin",
        "Glucose"
    ]

    # Load the image
    image_path = settings.BASE_DIR/f'media/{image_path}'
    image = cv2.imread(image_path)
    # Resize the image to make it easier to process (optional)
    scale_percent = 50  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    # Convert the image to grayscale
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve contour detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply adaptive thresholding to get a binary image
    binary = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort the contours by their position (top to bottom)
    contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[1])

    # Ensure we only process the expected number of contours
    contours = contours[:len(chemicals)]

    # Extract RGB values of each contour
    chemical_colors = []
    for contour in contours:
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)
        
        # Extract the ROI
        roi = resized[y:y+h, x:x+w]
        
        # Calculate the average color of the ROI
        average_color = cv2.mean(roi)[:3]
        chemical_colors.append({
            "chemical": chemicals[len(chemical_colors)],
            "rgb": (int(average_color[2]), int(average_color[1]), int(average_color[0]))  # Convert BGR to RGB
        })

    return chemical_colors


