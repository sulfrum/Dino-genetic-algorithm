from PIL import Image
import numpy as np
from colr import color
img_pil = Image.open("./assets/dino.png")
#a = np.asarray(img_pil)
pix_val = list(img_pil.getdata())

def printImage(image_vector, dimensions=[28,28], bg=False):
    for index, pixel in enumerate(image_vector, start=1):
        if bg:
            back = (pixel[3], pixel[3], pixel[3])
        else:
            back = (255-pixel[3], 255-pixel[3], 255-pixel[3])
        if(index%dimensions[0]==0):
            print(color(' ', fore=back, back=back))
        else:
            print(color(' ', fore=back, back=back), end="")

printImage(pix_val, [48, 50])

def reduceImageTo(image_list, originalDimension, reduceRatio):
    new_height = int(originalDimension[1]/reduceRatio)
    new_width = int(originalDimension[0]/reduceRatio)
    print("h: ", new_height)
    print("w: ", new_width)
    new_image = [0 for x in range(0, new_height*new_width)]

    line_count = 0
    # iterates over the entire new image
    for i in range(0, len(new_image)):
        # iterates over the pixel on original image that represents
        # the pixel at i position on new_image
        if(i>0 and (i%new_width)==0):
            line_count+=1
        for j in range(0, reduceRatio):
            if(new_image[i] == 1):
                break
            original_pixel_pos = (i*reduceRatio)+j + ((line_count)*originalDimension[0])
            if(image_list[original_pixel_pos][3] == 255):
                new_image[i] = 1
                break
            # searchs in depht a black pixel 
            for k in range(1, reduceRatio):
                original_pixel_pos_depht = (originalDimension[0]*k)+original_pixel_pos
                if(image_list[original_pixel_pos_depht][3] == 255):
                    new_image[i] = 1
                break
    return new_image
resized_image = reduceImageTo(pix_val, [48, 50], 2)
print(len(resized_image))

def printBinaryImage(image_vector, dimensions=[28,28], bg=False):
    for index, pixel in enumerate(image_vector, start=1):
        if bg:
            back = (pixel*255, pixel*255, pixel*255)
        else:
            back = (255-(pixel*255), 255-(pixel*255), 255-(pixel*255))
        if(index%dimensions[0]==0):
            print(color(' ', fore=back, back=back))
        else:
            print(color(' ', fore=back, back=back), end="")

printBinaryImage(resized_image, [28, 10])