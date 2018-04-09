import os

melanoma_list = []
for file in os.listdir('melanoma_scaled'):
    img_name = file[:-4]
    melanoma_list.append(img_name)

count = 1
if not os.path.exists('melanoma_scaled_bin'):
    os.makedirs('melanoma_scaled_bin')
if not os.path.exists('others_scaled_bin'):
    os.makedirs('others_scaled_bin')
for file in os.listdir('gt_scaled'):
    end_position = file.rfind('_')
    img_name = file[:end_position]
    if img_name in melanoma_list:
        os.rename('gt_scaled/'+file, 'melanoma_scaled_bin/'+img_name+'.png')
        # print img_name, count
        # count += 1
    else:
        os.rename('gt_scaled/'+file, 'others_scaled_bin/'+img_name+'.png')
