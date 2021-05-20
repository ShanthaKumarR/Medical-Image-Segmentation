import numpy as np
#import keras
import pandas as pd
image = np.array([10,11,12,13,14,15])

image_length = image.shape[0]
patch_length = 3
start_i = 3

valid_start_i = [i for i in range(image_length - patch_length + 1)]
#print(valid_start_i)

for _ in range(10):
    valid_start_i = np.random.randint(image_length - patch_length + 1)
    print(valid_start_i)