from typing import List
from Kernel import Kernel, init

def safe(image, i, j):
    if 0 <= i < image.shape[0] and 0 <= j < image.shape[1]:
        return image[i][j]
    return 0

def filter_function(image: List[List[int]], kernel: List[List[int]]):
    filt = image.copy()

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            newimage = 0
            total = 0

            for k in range(len(kernel)):
                for l in range (len(kernel[k])):
                    if i+k >= len(image) or j+l >= len(image[0]):  #
                        continue
                    total += (image[i+k][j+l] * kernel[k][l])
                    newimage += (kernel[k][l])  
            if newimage != 0:
                total = total / newimage

            ksum = sum(sum(k) for k in kernel)
            if ksum == 0:
                ksum = 1

            s = total / ksum
            
            if s > 255:
                s = 255
            if s < 0:
                s=0
            filt[i][j] = s

    return filt

K = Kernel("minion.png", filter_function)

init()