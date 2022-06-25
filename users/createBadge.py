import cv2
import urllib.request
import numpy as np


def loadImage():
    # ! We need to load a png image.
    badgeLoaded = urllib.request.urlopen(
        'https://res.cloudinary.com/dxx9kwg6t/image/upload/v1655923410/media/badge/5718640_onq5oj.jpg')
    badgeArray = np.asarray(bytearray(badgeLoaded.read()), dtype=np.uint8)
    badge = cv2.imdecode(badgeArray, cv2.IMREAD_COLOR)
    badge = cv2.resize(badge, (800, 800))
    h, w = badge.shape[:2]
    badgePng = np.zeros((h, w, 4), dtype=np.uint8)
    mainX = 117
    mainY = 249
    for i in range(h):
        for j in range(w):
            r, g, b = badge[i][j][:3]
            badgePng[i][j] = (r, g, b, 255)

    # ! The user image should be a function parameter.
    userPhotoLoaded = urllib.request.urlopen(
        'https://res.cloudinary.com/dxx9kwg6t/image/upload/v1655843826/media/images_users/userDefault_xzdedb.png')
    userPhotoArray = np.asarray(
        bytearray(userPhotoLoaded.read()), dtype=np.uint8)
    userPhoto = cv2.imdecode(userPhotoArray, cv2.IMREAD_COLOR)
    preferedUserPhotoSize = 215
    userPhoto = cv2.resize(
        userPhoto, (preferedUserPhotoSize, preferedUserPhotoSize))

    radius = preferedUserPhotoSize//2
    height, width = userPhoto.shape[:2]
    xCenter = width//2
    yCenter = height//2

    circularMask = np.zeros_like(userPhoto)
    circularMask = cv2.circle(
        circularMask, (xCenter, yCenter), radius, (255, 255, 255), -1)

    some = cv2.bitwise_and(userPhoto, circularMask)

    circularMask = cv2.cvtColor(circularMask, cv2.COLOR_BGR2GRAY)
    x, y, w, h = cv2.boundingRect(circularMask)
    circularUserPhoto = some[y: y + h, x: x + w]
    circularMask = circularMask[y: y + h, x: x + w]
    circularUserPhoto[circularMask == 0] = (255, 255, 255)

    h, w = circularUserPhoto.shape[:2]
    transparentImage = np.zeros((h, w, 4), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if circularMask[i][j] != 0:
                r, g, b = circularUserPhoto[i][j][:3]
                transparentImage[i][j] = (r, g, b, 255)
                badgePng[mainY + i][mainX + j] = (r, g, b, 255)
            else:
                transparentImage[i][j] = (255, 255, 255, 0)

    cv2.imshow('Mask', circularMask)
    cv2.imshow('Image User', circularUserPhoto)
    cv2.imshow('Image User PNG', transparentImage)
    cv2.imshow('Bagde with User PNG', badgePng)
    while cv2.waitKey(1) != ord('q'):
        x = 12
    cv2.destroyAllWindows()

    cv2.imwrite('circularImage.png', transparentImage)


loadImage()
