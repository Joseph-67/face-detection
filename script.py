import cv2
# after trigering the webcam import the haracascades classiier built into open cv
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades+"haarcascade_frontalface_default.xml"
)
# setting up camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# setup dimensions
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# create the function to detect faces
def detect_faces(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize = (40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x+w, y+h), (255, 0, 0), 4)
    return faces
# setup mainloop
while True:
    # takes a return value and the frame
    ret, frame = cap.read()
    # use the return value to determine if it returned something and the 
    # and the frame to get the actual frame
    if ret:
        # pass
        # detect faces
        faces = detect_faces(frame)
        # display webcam
        cv2.imshow("My face detection project", frame)
        # if counter % 30 == 0:
        #     try:
    # get wait key
    key = cv2.waitKey(1)
    # if key is equal to the ordunal of q break out of the loop.
    if key == ord("9"):
        break
# destroy all windows when q is pressed
cap.release()
cv2.destroyAllWindows()
