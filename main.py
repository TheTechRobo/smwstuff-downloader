


# SMWSTUFF.NET GRABBER

import requests, json, os

def map():
    images = []
    params = {"cmd" : "alloftype", "arg": "map"}
    url = "http://smwstuff.net/api"
    data = json.loads(requests.post(url, data=params).text)
    images_str = ""
    for i in data:
        images.append('smwstuff.net' + i['content_specific']['preview_full_path'])
        #print('smwstuff.net' + i['content_specific']['preview_full_path'])
        images.append("smwstuff.net/get?f=%s" % i['id'])
    for i in images:
        images_str += i
        images_str += "\n"
    with open("images", "w+") as file:
        file.write(images_str)
    os.system('wget --warc-file="smwstuff-api" --post-data="cmd=alloftype&arg=map" http://smwstuff.net/api')
    a = os.system("""zsh -c "source ~/gs-venv/bin/activate && grab-site --delay 1-50 -i images" """)
    print(a)

def skin():
    images = []
    params = {"cmd" : "alloftype", "arg": "skin"}
    url = "http://smwstuff.net/api"
    data = json.loads(requests.post(url, data=params).text)
    images_str = ""
    for i in data:
        images.append('smwstuff.net' + i['content_specific']['png_path'])
        #print('smwstuff.net' + i['content_specific']['preview_full_path'])
        images.append("smwstuff.net/get?f=%s" % i['id'])
    for i in images:
        images_str += i
        images_str += "\n"
    with open("images", "w+") as file:
        file.write(images_str)
    os.system('wget --warc-file="smwstuff-api" --post-data="cmd=alloftype&arg=map" http://smwstuff.net/api')
    a = os.system("""zsh -c "source ~/gs-venv/bin/activate && grab-site --delay 1-50 -i images" """)
    print(a)
