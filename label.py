import cv2
import os
import shutil

src = "./src/"
outputDir = "./output/"
dst1 = "./output/VALID/"
dst2 = "./output/INVALID/"
dst3 = "./output/OTHERS/"
lastLabelImage = ""

# check Folder
folders = [src, outputDir, dst1, dst2, dst3]
for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)

def label(image_name, image):    
    global lastLabelImage
    temp = cv2.resize(image,(1024, 768))
    cv2.imshow(image_name, temp)
    
    while True:
        key = cv2.waitKey(0)
        if key & 0xFF == ord('q') or key & 0xFF == ord('y') or key & 0xFF == ord('n') or key & 0xFF == ord('o') or key & 0xFF == ord('4') or key & 0xFF == ord('d') or key & 0xFF == ord('z'):
            break
            
    if key & 0xFF == ord('q'):
        cv2.destroyWindow(image_name)
        return -1
    
    # 违法
    elif key & 0xFF == ord('y'):
        cv2.destroyWindow(image_name)
        shutil.move(os.path.join(src, image_name), os.path.join(dst1, image_name))
        lastLabelImage = os.path.join(dst1, image_name)
        
    # 未违法
    elif key & 0xFF == ord('n'):
        cv2.destroyWindow(image_name)
        shutil.move(os.path.join(src, image_name), os.path.join(dst2, image_name))
        lastLabelImage = os.path.join(dst2, image_name)
        
    # others，其他情况
    elif key & 0xFF == ord('o'):
        cv2.destroyWindow(image_name)
        shutil.move(os.path.join(src, image_name), os.path.join(dst3, image_name))
        lastLabelImage = os.path.join(dst3, image_name)

    # 撤回上一步操作 
    if key & 0xFF == ord('z'):
        cv2.destroyWindow(image_name)
        return 0


'''
show number of images to label
'''
images = os.listdir(src)
print("==> {} images to label".format(len(images)))
for img in images:
    result = label(img, cv2.imread(src+img))
    if result == -1: 
        break

    # 有撤销操作，重新读取上一张图片
    elif result == 0: 
        # 将上一张图放回src文件夹中
        des = src + lastLabelImage.split('/')[-1]
        shutil.move(lastLabelImage, des)
        lastLabelImage = des

        if(label(lastLabelImage.split('/')[-1], cv2.imread(lastLabelImage)) == -1): 
            break

images = os.listdir(src)
print("==> {} images left".format(len(images)))


import glob
count = 0
valid = len(glob.glob("./output/VALID/*"))
invalid = len(glob.glob("./output/INVALID/*"))
others = len(glob.glob("./output/OTHERS/*"))
count = valid + invalid + others

print("==> total count: ", count)
print("==> valid:{}  invalid:{}  others:{}".format(valid, invalid, others))
