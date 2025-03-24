def __init__(self):
    self.longToShort = {}
    self.shortToLong = {}
    self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    self.baseUrl = "http://tinyurl.com/"


def encode(self, longUrl: str) -> str:
    """Encodes a URL to a shortened URL.
    """
    if longUrl in self.longToShort:
        return self.longToShort[longUrl]
    else:
        while True:
            short = "".join(random.choice(self.chars) for _ in range(6))
            shortUrl = self.baseUrl + short
            if shortUrl not in self.shortToLong:
                self.longToShort[longUrl] = shortUrl
                self.shortToLong[shortUrl] = longUrl
                return shortUrl


def decode(self, shortUrl: str) -> str:
    """Decodes a shortened URL to its original URL.
    """
    return self.shortToLong[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))