# URL Short

This is a small program to short the Url by the help of `urllib`.

![URL SHORT](https://miro.medium.com/max/700/1*Pdw7h5X6vQQNVopIzHBG6A.jpeg)

## Program

```
import urllib.request

def tiny_url(url):
  apiurl = "http://tinyurl.com/api-create.php?url="
  tinyurl = urllib.request.urlopen(apiurl + url).read()
  return tinyurl.decode("utf-8")

url = input("Enter the url to short : ")
print(tiny_url(url))
```

## Run

```
git clone https://github.com/BasilcM/My-Projects.git
cd My-Projects\URL Short\
python URL_Short Python.py
```

Enter The Input Url 
