from django.shortcuts import render
from pathlib import Path
import os
import random
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

def matcher(request):
    print(os.getcwd())
    if os.getcwd() == '/Applications/Django/MatchBox/static/img':
        pass
    else:
        os.chdir('static/img/')

    print(os.listdir())

    list_img = os.listdir()
    img1 = random.choice(list_img)
    img2 = random.choice(list_img)
    if img1 == img2:
        img2 = random.choice(list_img)
    return render(request, 'matcher.html', {'img1': img1, 'img2': img2})
