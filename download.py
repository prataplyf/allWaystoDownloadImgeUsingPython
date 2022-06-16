# using wget.download()
import wget
def downloadImageWGET(url=None, path=None):
    dwn = wget.download(url, path)

url = "https://th.bing.com/th/id/OIP.QB7flk0M76hqLmGl9Dn1CAEdDb?pid=ImgDet&w=1024&h=787&rs=1"
imageSavingPath = "D:\Medium\downloadImages\cyberSecurity.jpg"
downloadImageWGET(url=url, path=imageSavingPath)


# using urlretrieve()
import urllib.request
def downloadImageUrlretrieve(url=None, path=None):
    urllib.request.urlretrieve(url,path)

url = "http://www.python.org/images/success/nasa.jpg"
imageSavingPath = "D:\Medium\downloadImages\Inasa.jpg"
downloadImageUrlretrieve(url=url, path=imageSavingPath)


# using urlopen()
import urllib.request
def downloadImageUrlopen(url=None, path=None):
    f = open(path,'wb')
    f.write(urllib.request.urlopen(url).read())
    f.close()

url = "http://www.python.org/images/success/nasa.jpg"
imageSavingPath = "D:\Medium\downloadImages\Inasa1.jpg"
downloadImageUrlretrieve(url=url, path=imageSavingPath)


# using request
import requests
def downloadImageRequests(url=None, path=None):
    f = open(path,'wb')
    response = requests.get(url)
    f.write(response.content)
    f.close()

url = "http://www.python.org/images/success/nasa.jpg"
imageSavingPath = "D:\Medium\downloadImages\Inasa2.jpg"
downloadImageRequests(url=url, path=imageSavingPath)


# using requests(to get image from web) and shutil(to save it locally)
import requests
import shutil
def downloadImageShutil(url=None, path=None):
    req = requests.get(url, stream=True)  # streat=True( to guarantee no interruptions)
    req.raw.decode_content = True
    with open(path, 'wb') as f:
        shutil.copyfileobj(req.raw, f)

url = "http://www.python.org/images/success/nasa.jpg"
imageSavingPath = "D:\Medium\downloadImages\Inasa3.jpg"
downloadImageShutil(url=url, path=imageSavingPath)