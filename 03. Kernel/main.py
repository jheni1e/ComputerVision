from typing import List
from Kernel import Kernel, init

def filter_function(image: List[List[int]], kernel: List[List[int]]):
    stride = (1,1)
    filt = [lin.copy() for lin in image]

    lenY = len(image)
    lenX = len(image[0])

    top = len(kernel) // 2
    left = len(kernel[0]) // 2

    for i in range(0, lenY, stride[0]):
        for j in range(0, lenX, stride[1]):
            newimage = 0 #soma dos valores do kernel (equivalente a normalização)
            total = 0 #soma das multiplicações pixel × kernel

            for k in range(len(kernel)):
                for l in range (len(kernel[k])):
                    y = i - top + k
                    x = j - left + l
                    newimage += kernel[k][l] #soma apenas os pesos do kernel (normalização)
                    
                    if y < 0 or y >= lenY or x < 0 or x >= lenY: #checa se está nos limites da imagem
                        continue
                    total += (image[y][x] * kernel[k][l]) #soma o produto entre pixel e peso do kernel

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