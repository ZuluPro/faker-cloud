from unittest import TestCase
import re

from faker import Faker
from faker_cloud import amazon_web_services


class AmazonWebServicesTest(TestCase):
    regions = amazon_web_services.AmazonWebServicesProvider._regions
    azs = amazon_web_services.AmazonWebServicesProvider._availability_zones

    def setUp(self):
        self.factory = Faker()
        self.factory.add_provider(amazon_web_services.AmazonWebServicesProvider)

    def test_region(self):
        for i in range(1000):
            region = self.factory.region()
            self.assertIn(region, self.regions)
            self.assertIsInstance(region, tuple)

    def test_region_name(self):
        for i in range(1000):
            region = self.factory.region_name()
            self.assertIsInstance(region, str)

    def test_region_code(self):
        for i in range(1000):
            region = self.factory.region_code()
            self.assertIsInstance(region, str)

    def test_availability_zone(self):
        for i in range(1000):
            az = self.factory.availability_zone()
            self.assertIsInstance(az, str)

        for i in range(1000):
            region_code = self.factory.region_code()
            az = self.factory.availability_zone(region_code)
            self.assertIsInstance(az, str)
            self.assertTrue(az.startswith(region_code))
            self.assertIn(az, self.azs)

    def test_instance_id(self):
        reg_instance_id = re.compile('^i-[0-9a-f]{17}$')
        for i in range(1000):
            instance_id = self.factory.instance_id()
            self.assertTrue(reg_instance_id.match(instance_id))

    def test_kernel_id(self):
        reg_kernel_id = re.compile('^aki-[0-9a-f]{8}$')
        for i in range(1000):
            kernel_id = self.factory.kernel_id()
            self.assertTrue(reg_kernel_id.match(kernel_id))

    def test_image_id(self):
        reg_image_id = re.compile('^ami-[0-9a-f]{8}$')
        for i in range(1000):
            image_id = self.factory.image_id()
            self.assertTrue(reg_image_id.match(image_id))
