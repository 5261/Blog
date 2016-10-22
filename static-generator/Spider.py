from requests import get
from bs4 import BeautifulSoup
import os

class Spider:
    def __init__(self):
        self.vised = set()
        
        reload(os.sys)
        os.sys.setdefaultencoding("utf-8")

    def clear(self):
        self.vised.clear()

    def shouldGet(self, url):
        if url[0:4] == "http":
            return False
        if self.rootUrl + url in self.vised:
            return False

        return True
    
    def tryToDownload(self, url):
        if not self.shouldGet(url):
            return (False, None)
        absUrl = self.rootUrl + url
        print "Downloading %s" % (absUrl, )
        self.vised.add(absUrl)
    
        req = get(absUrl)
        
        return (True, req)
        
    def store(self, url, content, model = "w"):
        path = self.rootPath + url

        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

        with open(path, model) as f:
            f.write(content)
            
    def getNext(self, html):
        doc = BeautifulSoup(html, "html5lib")

        link = doc.find_all("a")
        css = doc.find_all("link")
        img = doc.find_all("img")
        script = doc.find_all("scipt")

        for each in link:
            url = each.get("href")
            if url != "/" and url != "#":
                self.getPage(url)

        for each in css:
            self.getFile(each.get("href"))

        for each in img:
            self.getImg(each.get("src"))

        for each in script:
            self.getFile(each.get("src"))

    def getPage(self, url):
        succeeded, req = self.tryToDownload(url)
        if not succeeded:
            return 
        
        html = req.text
        self.store(url + "index.html", html)
        
        self.getNext(html)

    def getFile(self, url):
        succeeded, req = self.tryToDownload(url)
        if not succeeded:
            return 
        
        content = req.text
        self.store(url, content)
        
    def getImg(self, url):
        succeeded, req = self.tryToDownload(url)
        if not succeeded:
            return 
        
        content = req.content
        self.store(url, content, "wb")
    
    def clone(self, url, path):
        self.rootUrl = url
        self.rootPath = path

        self.getPage("/")

