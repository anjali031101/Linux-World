def distance():
    # Implementation of the first program/functionality
    import cv2
    import math

    cap=cv2.VideoCapture(0)

    while True:
        status , photo = cap.read()

# Load the face cascade classifier
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load and preprocess the image
        image = cv2.imread('photo')
        gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Calculate the face distance and display it on the image
        if len(faces) > 0:
        # Assuming only one face is detected
            (x, y, w, h) = faces[0]
    # Calculate the distance between two points on the face (e.g., distance between eyes)
            eye_distance = math.sqrt((x + w//2)**2 + (y + h//2)**2)

    # Draw the face bounding box
            cv2.rectangle(photo, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the face distance on the image
            cv2.putText(photo, f"Face distance: {eye_distance}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Show the image with face distance
            cv2.imshow("my photo",photo) 
            if cv2.waitKey(1) == 27:
                break
    cv2.destroyAllWindows()
#


