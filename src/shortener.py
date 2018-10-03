# Implement a URL shortener with the following methods:
# •	shorten(url), which shortens the url into a six-character alphanumeric 
#     string, such as zLg6wl. 
# •	restore(short), which expands the shortened string into the original url.
#     If no such shortened string exists, return null. 
# Hint: What if we enter the same URL twice?

from uuid import uuid4

class Shortener:
    def __init__(self):
        self.db = {}
        self.map = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def shorten(self, url):
        # in product, this should be an auto-incremented id
        uid = uuid4().int % (62 ** 6)
        short_url = []
        n = uid
        while n:
            short_url.append(self.map[n % 62])
            n //= 62
        
        short_url = ''.join(short_url)
        self.db[uid] = url
        return short_url

    def restore(self, short_url):
        uid = 0
        for i, c in enumerate(short_url):
            uid += 62 ** i * self.map.index(c)

        if uid not in self.db:
            return None
        return self.db[uid]


if __name__ == '__main__':
    s = Shortener()
    for url in ['https://github.com/', 'https://www.wikipedia.org/']:
        short_url = s.shorten(url)
        origin_url = s.restore(short_url)
        print(url, short_url, origin_url)

    print(s.db)