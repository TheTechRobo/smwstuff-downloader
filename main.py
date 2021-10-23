


# SMWSTUFF.NET GRABBER

import requests, json, os

def map():
    images = []
    params = {"cmd" : "alloftype", "arg": "map"}
    url = "http://smwstuff.net/api"
    data = json.loads(requests.post(url, data=params).text)
    images_str = ""
    comments = []
    for i in data:
        images.append('smwstuff.net' + i['content_specific']['preview_full_path'])
        #print('smwstuff.net' + i['content_specific']['preview_full_path'])
        images.append("smwstuff.net/get?f=%s" % i['id'])
        comments.append(i['id'])
    for i in images:
        images_str += i
        images_str += "\n"
    with open("images", "w+") as file:
        file.write(images_str)
    os.system('wpull --warc-append --warc-file="smwstuff-api-map" --post-data="cmd=alloftype&arg=map" http://smwstuff.net/api')
    for i in comments:
        print(i)
        os.system('wpull --warc-append --warc-file="smwstuff-api-map" --post-data="cmd=commentsof&arg=%s" http://smwstuff.net/api' % i)
    a = os.system("""zsh -c "grab-site --delay 1-50 -i images" """)
    print(a)

def skin():
    images = []
    params = {"cmd" : "alloftype", "arg": "skin"}
    url = "http://smwstuff.net/api"
    data = json.loads(requests.post(url, data=params).text)
    images_str = ""
    comments =  []
    for i in data:
        images.append('smwstuff.net' + i['content_specific']['png_path'])
        #print('smwstuff.net' + i['content_specific']['preview_full_path'])
        images.append("smwstuff.net/get?f=%s" % i['id'])
        comments.append( i['id'])
    for i in images:
        images_str += i
        images_str += "\n"
    with open("images", "w+") as file:
        file.write(images_str)
    os.system('wpull --warc-append --warc-file="smwstuff-api-skin" --post-data="cmd=alloftype&arg=skin" http://smwstuff.net/api')
    for i in comments:
        print(i)
        os.system('wpull --warc-append --warc-file="smwstuff-api-skin" --post-data="cmd=commentsof&arg=%s" http://smwstuff.net/api' % i)
        #os.system('rm ' + i)
    a = os.system("""zsh -c "grab-site --delay 1-50 -i images" """)

def world():
    return "Sorry! There are no worlds hosted on the site, so I cannot reverse-engineer the API."
announcer = world
music = world
gpack = world
sfx = world
