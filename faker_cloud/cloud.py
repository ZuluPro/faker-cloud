import string
from faker.providers import BaseProvider


class Provider(BaseProvider):
    def hexify(self, text='???'):
        return self.lexify(text, string.hexdigits[:-6])
