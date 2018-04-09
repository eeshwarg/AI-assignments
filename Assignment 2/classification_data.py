import os
import cv2
import numpy as np

def some_func(dir1, dir2, output_dir):
    for file in os.listdir(dir1):
        img1 = cv2.imread(dir1+file)
        img2 = cv2.imread(dir2+file[:-4]+'.png')
        img2[img2 > 0] = 1
        img2[img2 < 0] = 0
        result = np.multiply(img1,img2)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        cv2.imwrite(output_dir+file, result)


some_func('Segmentation data/others_scaled/','Segmentation data/others_scaled_bin/', 'others_scaled_class/')
