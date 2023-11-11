from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
import urllib.error as err

class URLprocessor:
    def __init__(self, url):
        self.url = url
        parsed_url      = urlparse(url)
        self.domain     = parsed_url.netloc
        self.path       = parsed_url.path
        self.scheme     = parsed_url.scheme
        self.params     = parsed_url.params
        self.query      = parsed_url.query
        self.fragment   = parsed_url.fragment

        self.headers    = {'User-Agent': 'Mozilla/5.0'}

    def print(self):
        print("URL: {}".format(self.url))
        print("Domain: {}".format(self.domain))
        print("Path: {}".format(self.path))
        print("Scheme: {}".format(self.scheme))
        print("Params: {}".format(self.params))
        print("Query: {}".format(self.query))

    def buildURL(self, scheme, domain, path, params, query):
        # TODO: implement
        pass

    # Returns the content of the URL
    def read(self, url):
        obj = Request(url, headers=self.headers)
        try:
            response = urlopen(obj)
            data = response.read()
            return data
        except err.URLError as e:
            print("Error: {}".format(e.reason))
            return None
        
    def write(self, values = None):
        try:
            data = urlencode(values).encode('utf-8')
            obj = Request(self.url, data, self.headers)
        except err.URLError as e:
            print("Error: {}".format(e.reason))
        

if __name__ == "__main__":
    # url = 'https://medium.com/mlearning-ai/face-recognition-for-superimposed-facemasks-using-vggface2-in-keras-c13e610acd56'
    # url_processor = URLprocessor(url)
    # url_processor.print()