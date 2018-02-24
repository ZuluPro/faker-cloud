from unittest import TestCase

from faker import Faker
from faker_cloud import upcloud


class UpcloudTest(TestCase):
    zones = upcloud.Provider._zones
    volume_types = upcloud.Provider._volume_types

    def setUp(self):
        self.factory = Faker()
        self.factory.add_provider(upcloud.Provider)

    def test_zone(self):
        for i in range(1000):
            zone = self.factory.zone()
            self.assertIn(zone, self.zones)
            self.assertIsInstance(zone, tuple)

    def test_zone_name(self):
        for i in range(1000):
            zone = self.factory.zone_name()
            self.assertIsInstance(zone, str)

    def test_zone_code(self):
        for i in range(1000):
            zone = self.factory.zone_code()
            self.assertIsInstance(zone, str)

    def test_datacenter(self):
        for i in range(1000):
            dc = self.factory.datacenter()
            self.assertIsInstance(dc, tuple)
            self.assertIn(dc, self.zones)
