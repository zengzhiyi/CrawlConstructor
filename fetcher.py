#decide whether add or remove urls
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, urls):
        if urls is None:
            return
        for url in urls:
            if url not in self.new_urls and url not in self.old_urls:
                self.new_urls.add(url)

    def has_new_url(self):
        '''当new_urls中扔有url未爬取时，True，在主函数中用while搭配'''
        return len(self.new_urls) != 0

    def get_new_url(self):
        '''把在new_urls里的最后一个url弄下来再爬'''
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
