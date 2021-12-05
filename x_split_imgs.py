
import cv2 
import os
import numpy as np
from pathlib import Path

GANSIZE_EXP_NUM = 2
DEBUG_IMG = False

def _resize_to_aligned_img(img, gan_size, path_img, dir_dst):
    img_h = img.shape[0]
    img_w = img.shape[1]
 
    img_new = np.zeros((img_w, img_w, img.shape[2]))
    img_new = img[0:img_w, 0:img_w, :]

    img_new = cv2.resize(img_new, (gan_size * GANSIZE_EXP_NUM, gan_size * GANSIZE_EXP_NUM))
 
    print(f"process {path_img} image_org h {img_h} w {img_w} -> image_new h {img_new.shape[0]} w {img_new.shape[1]}")

    #if DEBUG_IMG:
    #    filename = str(Path(path_img).stem) + ".jpg"
    #    path_new = Path(dir_dst) / filename 
    #    cv2.imwrite(str(path_new), img_new)

    return img_new

def _scan_chunk_img(img_new, gan_size, path_img, dir_dst):
    cnt = 1
    for x in range(0, gan_size, 32):
        for y in range(0, gan_size, 32):
            img_chunk = np.zeros((gan_size, gan_size, img_new.shape[2]))
            img_chunk = img_new[x:x+gan_size, y:y+gan_size, :]
            filename = str(Path(path_img).stem) + "_{:02}.jpg".format(cnt)
            path_chunk = Path(dir_dst) / filename 
            cv2.imwrite(str(path_chunk), img_chunk)
            cnt += 1


def split_img(path_img, dir_dst, gan_size):
    os.makedirs(dir_dst, exist_ok=True)
    try:
        img = cv2.imread(path_img, cv2.IMREAD_COLOR)
        img_h = img.shape[0]
        img_w = img.shape[1]
        if img_h < img_w:
            return []
    except:
        return[]

    img_new = _resize_to_aligned_img(img, gan_size, path_img, dir_dst)
    return _scan_chunk_img(img_new, gan_size, path_img, dir_dst)


def prepare_gan_imgs(dir_src, dir_dst, gan_size):
    fnames = os.listdir(dir_src)

    for fname in fnames:
        path_img = dir_src + "/" + fname
        if os.path.isfile(path_img):
            split_img(path_img, dir_dst, gan_size)    

if __name__ == "__main__":
    dir_src = "ds_org_lilei"
    dir_dst = "ds_chunk_lilei"
    gan_size = 256

    prepare_gan_imgs(dir_src, dir_dst, gan_size)
