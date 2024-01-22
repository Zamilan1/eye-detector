import dlib
import cv2

# Initialize face and eye detectors
face_detector = dlib.get_frontal_face_detector()
eye_detector = dlib.get_frontal_face_detector()  # This should be changed to dlib.get_frontal_face_detector()

# Capture video from your webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for face and eye detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_detector(gray)
    
    for face in faces:
        # Extract the eye ROI from the face
        (x, y, w, h) = (face.left(), face.top(), face.width(), face.height())
        eyes_roi = gray[y:y + h, x:x + w]

        # Detect eyes in the eye ROI
        eyes = eye_detector(eyes_roi)  # This line should use the eye_detector
        for eye in eyes:
            # Process eye tracking here
            pass

    cv2.imshow("Eye Tracker", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
