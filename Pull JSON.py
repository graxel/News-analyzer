#import urllib.request, json

#urllib.request.urlopen("https://newsapi.org/v2/everything?sources=cnn&pagesize=10&page=1&apiKey=2d2757dedcbb49398de5f5ea3342068a", cafile=None, capath=None)
    #data = json.loads(url.read().decode())
    #print(data)



import requests #, json



i = requests.get("https://newsapi.org/v2/everything?sources=cnn&pagesize=10&page=1&apiKey=2d2757dedcbb49398de5f5ea3342068a",verify=False)
