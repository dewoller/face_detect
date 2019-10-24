import cv2
import sys
import os
directory = '.'
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
rootDir='/mnt/video'


####################################################################################################
def size_faces( imagePath ) :
    # Read the image
    try:
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        size=0
        for (top, right, bottom, left)in faces:
            w, h = abs(right-left), abs(top-bottom)
            size = size + (w*h)
    except:
        size=-1
    return(size)
####################################################################################################
def iterateImages(key):

    #('/mnt/video/2019/10/images/24/20191024224838-20191024224838-03.jpg', 0)
    year=key[0:4]
    month=key[4:6]
    day=key[6:8]
    baseDir = "{0}/{1}/{2}/images/{3}/".format(rootDir, year, month, day)

    images = []
    for filename in os.listdir(baseDir):
        if filename.endswith(".jpg") and filename.startswith(key):
            images.append(baseDir + filename)

    return(images)

####################################################################################################
key = sys.argv[1]
biggest_file=''
max_size=40
for file in iterateImages(key):
    size = size_faces( file )
    if size > max_size:
        biggest_file = file
        max_size = size


if biggest_file != '':
    print biggest_file


    

