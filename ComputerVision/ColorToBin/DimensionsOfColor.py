import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
from PIL import Image


def makeBins(binMax, binWidth, binMin = np.float32(0)):
    bins = []

    while binMin < binMax:
        if binMin+binWidth > binMax:
            binWidth = binMax - binMin
        bins.append( (binMin,binMin+binWidth) )
        binMin += np.float32(binWidth)


    return bins

def binaryDimensions(img, bins = makeBins(1, .10)):

    imgShape = img.shape
    imgVec = img.flatten()

    variants = []

    for bin in bins:
        imgCpy = imgVec.copy().reshape(-1, img.shape[-1])
        counter = 0
        while counter < imgCpy.shape[0]:
            if (imgCpy[counter][0] >= bin[0] and imgCpy[counter][0] < bin[1]) or (
                    imgCpy[counter][1] >= bin[0] and imgCpy[counter][1] < bin[1]) or (
                    imgCpy[counter][2] >= bin[0] and imgCpy[counter][2] < bin[1]):
                # Make pixel white
                imgCpy[counter] = [1, 1, 1]
            else:
                # Make pixel black.
                imgCpy[counter] = [0, 0, 0]
            counter += 1

        variants.append(imgCpy.reshape(img.shape))

    return variants

srcPhotoExt = ".jpg"
#srcPhoto = "Source/34"
#srcPhoto = "Source/me"
srcPhoto = "Source/ad3"
#srcPhoto = "Source/tomato2"


im = Image.open(srcPhoto+srcPhotoExt)
im.save(srcPhoto+".png")
img=mpimg.imread(srcPhoto+".png")
plt.subplots_adjust(wspace=0, hspace=0)

variants = binaryDimensions(img)
nVariants = len(variants)
plt.subplots_adjust(wspace=0, hspace=0)

fig = plt.figure(figsize = (20,10))
plt.subplots_adjust(wspace=0, hspace=0)

ax1 = fig.add_subplot(2,5,10)
ax1.set_aspect('equal')
ax1.imshow( variants[0] )
plt.axis('off')
plt.subplots_adjust(wspace=0, hspace=0)

ax1 = fig.add_subplot(2,5,9)
ax1.set_aspect('equal')
ax1.imshow( variants[1] )
plt.axis('off')
plt.subplots_adjust(wspace=0, hspace=0)

ax1 = fig.add_subplot(2,5,8)
ax1.set_aspect('equal')
ax1.imshow( variants[2] )
plt.axis('off')
plt.subplots_adjust(wspace=0, hspace=0)

ax1 = fig.add_subplot(2,5,7)
ax1.set_aspect('equal')
ax1.imshow( variants[3] )
plt.axis('off')
plt.subplots_adjust(wspace=0, hspace=0)

ax1 = fig.add_subplot(2,5,6)
ax1.set_aspect('equal')
ax1.imshow( variants[4] )
plt.axis('off')
plt.subplots_adjust(wspace=0, hspace=0)

ax1 = fig.add_subplot(2,5,5)
ax1.set_aspect('equal')
ax1.imshow( variants[5] )
plt.axis('off')
plt.subplots_adjust(wspace=0, hspace=0)

ax1 = fig.add_subplot(2,5,4)
ax1.set_aspect('equal')
ax1.imshow( variants[6] )
plt.axis('off')
plt.subplots_adjust(wspace=0, hspace=0)

ax1 = fig.add_subplot(2,5,3)
ax1.set_aspect('equal')
ax1.imshow( variants[7] )
plt.axis('off')
plt.subplots_adjust(wspace=0, hspace=0)

ax1 = fig.add_subplot(2,5,2)
ax1.set_aspect('equal')
ax1.imshow( variants[8] )
plt.axis('off')
plt.subplots_adjust(wspace=0, hspace=0)

ax1 = fig.add_subplot(2,5,1)
ax1.set_aspect('equal')
ax1.imshow( variants[9] )
plt.axis('off')

plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout()

plt.show()