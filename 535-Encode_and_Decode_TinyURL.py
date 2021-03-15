class Codec:
    def __init__(self):
        self.p = []
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.p.append(longUrl)
        return str(len(self.p) - 1)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.p[int(shortUrl)]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))