from urllib import request
import os
import datetime

def download_img(img_url):
    #dir_save_imgs = "/data/Dark_data/stt_API_new/darkdata/datasets/"
    dir_save_imgs = "C:/Users/SeongYeol/Downloads/ganomaly-master/ganomaly-master/data/TEST"

    img_name = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

    file_name = os.path.join(dir_save_imgs, img_name)
    file_name += ".jpg"
    request.urlretrieve(img_url,file_name)

    return file_name
