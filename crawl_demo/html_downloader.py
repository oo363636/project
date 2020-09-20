import urllib.request


class HtmlDownloader:
    def download(self, url):
        if url is None:
            return None

        respond = urllib.request.urlopen(url)

        if respond.getcode() != 200:
            return None

        # respond.decode('utf-8')         # 不用这个嘛？

        return respond.read()

