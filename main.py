import os
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
# Define the width and height for the webcam capture and the slide display
width, height = 1280, 720
folderPath = 'Presentation'

# Initialize webcam capture
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Get the list of presentation images, sorted by their filenames
pathImages = sorted(os.listdir(folderPath), key=len)
print(pathImages)

# variables
imgNumber = 0
buttonCounter=0
gestureThreshold = 400
buttonPressed = False
hs, ws = int(120 * 1), int(213 * 1)
buttonDelay = 30
annotations =[[]]
annotationNumber =0
annotationStart = False



#hand detector
detector = HandDetector(detectionCon=0.8,maxHands=1)
while True:
    # Capture the webcam image
    success, img = cap.read()
    #fip the image , mirror image
    img = cv2.flip(img, 1)
    # Load the current slide image
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)


    hands, img = detector.findHands(img)
    cv2.line(img, (0, gestureThreshold), (width,gestureThreshold), (0,255,0), 10)
    print(annotationNumber)


    if hands and buttonPressed is False:
        # get landmarks of the hands and the number of fingers
        hand= hands[0]
        fingers =  detector.fingersUp(hand)
        cx,cy = hand['center']
        #print(fingers)
        lmList = hand['lmList']

        #constrain values for easier drawing

    #    indexFinger = lmList[8][0], lmList[8][1]
        xVal = int(np.interp(lmList[8][0], [width//2, w], [0,width]))
        yVal = int(np.interp(lmList[8][1], [150, height-150], [0, height]))
        indexFinger = xVal, yVal



        if cy <=gestureThreshold: # if hand is at the height of the face
            # put your hand above yuor face : gester 1,2
            annotationStart = False
            # gesture 1 - left
            if fingers==[1,0,0,0,0]:
                print("left")
                annotationStart = False

                if imgNumber >0:
                    buttonPressed = True
                    # the drawing done in before slide should not continue to the next slide
                    annotations = [[]]
                    annotationNumber = 0
                    imgNumber-=1

            # gesture 2 - right
            if fingers == [0, 0, 0, 0, 1]:
                annotationStart = False

                print("right")
                if imgNumber<len(pathImages)-1:
                    buttonPressed = True
                    # the drawing done in before slide should not continue to the next slide
                    annotations = [[]]
                    annotationNumber = 0
                    imgNumber+=1

        # gesture 3 -  show pointer
        if fingers == [0,1,1,0,0]:
            cv2.circle(imgCurrent,indexFinger, 12, (0,0,255), cv2.FILLED)
            annotationStart = False
        #gesture 4- draw
        if fingers == [0,1,0,0,0]:
            if annotationStart is False:
                annotationStart = True
                annotationNumber +=1
                # keep adding points to this list
                annotations.append([])
            cv2.circle(imgCurrent,indexFinger, 12, (0,0,255), cv2.FILLED)
            annotations[annotationNumber].append(indexFinger)
        else:
            annotationStart =  False
        # gesture 5- erase
        if fingers ==[0,1,1,1,0]:
            if annotations:
                if annotationNumber>1:
                    annotations.pop(-1)
                    annotationNumber -=1
                    buttonPressed = True
    else:
        annotationStart: False



    #button pressed iterations
    if buttonPressed:
        buttonCounter +=1
        if buttonCounter> buttonDelay:
            buttonCounter = 0
            buttonPressed = False


    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j !=0:
                cv2.line(imgCurrent, annotations[i][j-1], annotations[i][j], (0,0,200), 12)

    # Resize the webcam image to fit the desired dimensions
    imgSmall = cv2.resize(img, dsize= (ws, hs))

    # Get the dimensions of the current slide image
    h, w, _ = imgCurrent.shape

    # Place the small webcam image on the top-right corner of the slide
    imgCurrent[0:hs, w - ws:w] = imgSmall

    # Display the webcam feed and the modified slide
    cv2.imshow("Webcam Feed", img)
    cv2.imshow("Slides", imgCurrent)

    # Check for key press to move to the next slide or quit
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('n'):
        imgNumber = (imgNumber + 1) % len(pathImages)
    elif key == ord('p'):
        imgNumber = (imgNumber - 1) % len(pathImages)

# Release the webcam and close the windows
cap.release()
cv2.destroyAllWindows()

'''import os

import cv2

width, height = 1280, 720
folderPath = 'Presentation'

cap =cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

# get the list of presentation imgs
pathImages = sorted(os.listdir(folderPath), key=len)
print(pathImages)

#variables
imgNumber = 0
hs, ws = int(120 *1),int(213*1)

while True:
    success, img = cap.read()
    pathFullImage = os.path.join(folderPath,pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    # addoing webcam image on the slides
    imgSmall = cv2.resize(img,(ws,hs))
    h,w , _ = imgCurrent.shape
    imgCurrent[0:hs, w-ws:w] = imgSmall


    cv2.imshow("Image", img)
    cv2.imshow("Slides", imgCurrent)

    key = cv2.waitKey(1)
    if key ==ord('q'):
        break'''