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
            node1 = safe(image, i-1, j-1) * kernel[0][0]
            node2 = safe(image, i-1, j)   * kernel[0][1]
            node3 = safe(image, i-1, j+1) * kernel[0][2]
            node4 = safe(image, i, j-1)   * kernel[1][0]
            node5 = safe(image, i, j)     * kernel[1][1]
            node6 = safe(image, i, j+1)   * kernel[1][2]
            node7 = safe(image, i+1, j-1) * kernel[2][0]
            node8 = safe(image, i+1, j)   * kernel[2][1]
            node9 = safe(image, i+1, j+1) * kernel[2][2]

            ksum = sum(sum(k) for k in kernel)
            if ksum == 0:
                ksum = 1

            s = (node1 + node2 + node3 + node4 + node5 + node6 + node7 + node8 + node9) / ksum
            
            if s > 255:
                s = 255
            if s < 0:
                s=0
            filt[i][j] = s

    return filt

K = Kernel("minion.png", filter_function)

init()