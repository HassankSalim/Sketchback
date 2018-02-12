import cv2
import numpy as np
from glob import glob

def dodgeNaive(image, mask):
    # determine the shape of the input image
    width,height = image.shape [:2] 

    # prepare output argument with same size as image
    blend = np.zeros((width,height), np.uint8)
    print("start")
    for c in xrange(width):
        for r in xrange(height):
            # do for every pixel  
            if mask[c,r] == 255:
                # avoid division by zero 
                blend[c,r] = 255
            else:
                # shift image pixel value by 8 bits
                # divide by the inverse of the mask
                tmp = (image[c,r] << 8) / (255-mask)

                # make sure resulting value stays within bounds
                if tmp.all() > 255:
                    tmp = 255
                    blend[c,r] = tmp
    print("end")
    return blend

def dodgeV2(image, mask):
  return cv2.divide(image, 255-mask, scale=256)

def make_sketch(filename, path = ""):
	img = cv2.imread(filename)

	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	img_gray_inv = 255 - img_gray

	img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(21, 21), sigmaX=0, sigmaY=0)

	img_blend = dodgeV2(img_gray, img_blur)
		
    # return img_blend        
    # cv2.imwrite(path + filename.split('/')[-1].split('.')[0] + "_sketch.jpg", img_blend)
	cv2.imwrite(path + filename.split('/')[-1].split('.')[0] + ".jpg", img_blend)


if __name__ == '__main__':
    import sys
    make_sketch(sys.argv[1])