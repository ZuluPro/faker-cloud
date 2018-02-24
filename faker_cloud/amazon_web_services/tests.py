from unittest import TestCase
import re

from faker import Faker
from faker_cloud import amazon_web_services


class AmazonWebServicesTest(TestCase):
    regions = amazon_web_services.Provider._regions
    azs = amazon_web_services.Provider._availability_zones
    volume_types = amazon_web_services.Provider._volume_types
    instance_type_series = amazon_web_services.Provider._instance_type_series
    instance_types = amazon_web_services.Provider._instance_types

    def setUp(self):
        self.factory = Faker()
        self.factory.add_provider(amazon_web_services.Provider)

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

    def test_ami_id(self):
        reg_ami_id = re.compile('^ami-[0-9a-f]{8}$')
        for i in range(1000):
            ami_id = self.factory.ami_id()
            self.assertTrue(reg_ami_id.match(ami_id))

    def test_security_group_id(self):
        reg_sg_id = re.compile('^sg-[0-9a-f]{8}$')
        for i in range(1000):
            sg_id = self.factory.security_group_id()
            self.assertTrue(reg_sg_id.match(sg_id))

    def test_vpc_id(self):
        reg_vpc_id = re.compile('^vpc-[0-9a-f]{8}$')
        for i in range(1000):
            vpc_id = self.factory.vpc_id()
            self.assertTrue(reg_vpc_id.match(vpc_id))

    def test_volume_id(self):
        reg_vol_id = re.compile('^vol-[0-9a-f]{17}$')
        for i in range(1000):
            vol_id = self.factory.volume_id()
            self.assertTrue(reg_vol_id.match(vol_id))

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

    def test_instance_type_serie(self):
        for i in range(1000):
            its = self.factory.instance_type_serie()
            self.assertIn(its, self.instance_type_series)

    def test_instance_type_serie_name(self):
        names = [i for i, j in self.instance_type_series]
        for i in range(1000):
            name = self.factory.instance_type_serie_name()
            self.assertIn(name, names)

    def test_instance_type_serie_verbose_name(self):
        names = [j for i, j in self.instance_type_series]
        for i in range(1000):
            name = self.factory.instance_type_serie_verbose_name()
            self.assertIn(name, names)

    def test_instance_type(self):
        for i in range(1000):
            it = self.factory.instance_type()
            self.assertIn(it, self.instance_types)

        for i in range(1000):
            serie = self.factory.instance_type_serie_name()
            it = self.factory.instance_type(serie=serie)
            self.assertIn(it, self.instance_types)
            self.assertTrue(it.startswith(serie))

    def test_flavor_name(self):
        for i in range(1000):
            it = self.factory.flavor_name()
            self.assertIn(it, self.instance_types)

    def test_snapshot_id(self):
        reg_snap_id = re.compile('^snap-[0-9a-f]{8}$')
        for i in range(1000):
            snap_id = self.factory.snapshot_id()
            self.assertTrue(reg_snap_id.match(snap_id))

    def test_ipv4_public(self):
        for i in range(1000):
            ip = self.factory.ipv4_public()
            self.assertTrue(str(ip).startswith('54.1'))

    def test_ec2_public_dns(self):
        for i in range(1000):
            dns = self.factory.ec2_public_dns()
            self.assertTrue(dns.startswith('ec2-'))
            self.assertTrue(dns.endswith('.compute-1.amazonaws.com'))

    def test_s3_object_url(self):
        for i in range(1000):
            url = self.factory.s3_object_url()
            self.assertTrue(url.startswith('https://s3.amazonaws.com/'))
