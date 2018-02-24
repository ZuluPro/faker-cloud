from unittest import TestCase
import re

from faker import Faker
from faker_cloud import cloud

REG_FLAVOR_NAME = re.compile(r'\d{1,3}CPU-\d{1,4}GB')


class CloudTest(TestCase):
    volume_types = cloud.Provider._volume_types

    def setUp(self):
        self.factory = Faker()
        self.factory.add_provider(cloud.Provider)

    def test_flavor_name(self):
        for i in range(1000):
            name = self.factory.flavor_name()
            self.assertTrue(REG_FLAVOR_NAME.match(name))

    def test_volume_type(self):
        for i in range(1000):
            vt = self.factory.volume_type()
            self.assertIn(vt, self.volume_types)

    def test_volume_type_name(self):
        names = [i for i, j in self.volume_types]
        for i in range(1000):
            name = self.factory.volume_type_name()
            self.assertIn(name, names)

    def test_volume_type_code(self):
        codes = [j for i, j in self.volume_types]
        for i in range(1000):
            code = self.factory.volume_type_code()
            self.assertIn(code, codes)
