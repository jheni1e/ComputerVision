from typing import List
from Kernel import Kernel, init

def filter_function(image: List[List[int]], kernel: List[List[int]]):
    filt = image.copy()

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            newimage = 0 #soma dos valores do kernel (equivalente a normalização)
            total = 0 #soma das multiplicações pixel × kernel

            for k in range(len(kernel)):
                for l in range (len(kernel[k])):
                    if i+k >= len(image) or j+l >= len(image[0]): #checa se está nos limites da imagem
                        continue
                    total += (image[i+k][j+l] * kernel[k][l]) #soma o produto entre pixel e peso do kernel
                    newimage += (kernel[k][l]) #soma apenas os pesos do kernel (normalização)

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