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
        for each in link:
            url = each.get("href")
            if url != "/" and url != "#":
                self.getPage(url)

    def getPage(self, url):
        succeeded, req = self.tryToDownload(url)
        if not succeeded:
            return 
        
        html = req.text
        self.store(url + "index.html", html)
        
        self.getNext(html)

    def clone(self, url, path):
        self.rootUrl = url
        self.rootPath = path

        self.getPage("/")

