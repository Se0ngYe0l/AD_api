import torchvision.transforms as transforms

import os
from PIL import Image


def data_transform(file_name, device):
    transform = transforms.Compose([transforms.Resize(32),
                                    transforms.CenterCrop(32),
                                    transforms.ToTensor(),
                                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)), ])
    img = Image.open(os.path.join("C:/Users/SeongYeol/Downloads/ganomaly-master/ganomaly-master/data/TEST",file_name)).convert('RGB')
    #img = Image.open(os.path.join("/data/Dark_data/stt_API_new/darkdata/datasets/",file_name)).convert('RGB')
    img = transform(img)
    img = img.unsqueeze(0)
    img = img.to(device)

    return img