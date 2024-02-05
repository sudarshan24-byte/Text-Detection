import cv2
import easyocr
import numpy as np

# Load the image
image_path = 'Images/licence-plate-3.jpg'
image = cv2.imread(image_path)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'], gpu=False)  # You can specify the language as needed

# Perform OCR on the image
result = reader.readtext(image)
# print(result)

# Extract text and bounding box coordinates
for detection in result:
    text = detection[1]
    bounding_box = detection[0]

    if len(text) >= 10:
    # Extract points from bounding box
        points = bounding_box[:4]
        points = [(int(x), int(y)) for x, y in points]

        # Convert the list of tuples to a NumPy array
        points = np.array(points, dtype=np.int32)

        # Reshape the array to a 2D array
        points = points.reshape((-1, 1, 2))

        # Draw the bounding box on the image
        cv2.polylines(image, [points], isClosed=True, color=(255, 0, 0), thickness=2)
    
        print(len(text))
    # Print the extracted text
        print(f"Text: {text}")

# Display the image with bounding boxes
cv2.imshow('Image with Bounding Boxes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
