from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

import numpy as np

import torch
import json

from Ganomaly.networks import NetG
from Ganomaly.transform import data_transform
from .utils import download_img

path = "./Ganomaly/75_netG.pth"
device = torch.device("cuda:0")
netg = NetG().to(device)
pretrained_dict = torch.load(path)['state_dict']
netg.load_state_dict(pretrained_dict)


def class_func(request):
    if request.method == "POST":
        data = request.POST.get('thermal_img_url')

        file_name = download_img(data)

        diagnosis = model_func(file_name)

        data_dict = {}
        data_dict['result'] = diagnosis
        return HttpResponse(json.dumps(data_dict))


def model_func(file_name):
    t_data = data_transform(file_name, device)

    netg.eval()
    with torch.no_grad():
        _, latent_i, latent_o = netg(t_data)
        error = torch.mean(torch.pow((latent_i-latent_o), 2), dim=1)

        error = error.cpu().numpy()
        error = np.squeeze(error)
        error = error.tolist()
        
        min = 0.0004461664648260921
        max = 0.029765909537672997
        threshold = 0.43434194
        
        an_score = (error - min) / (max - min)
        if an_score >= threshold:
            return 1
        else:
            return 0
        


