# -*- coding: utf-8 -*-
from faker.providers import BaseProvider

HEX_LETTERS = '0123456789abcdef'


class AmazonWebServicesProvider(BaseProvider):
    _regions = [
        ('us-east-1', 'US East (N. Virginia)'),
        ('us-east-2', 'US East (Ohio)'),
        ('us-west-1', 'US West (Northern California)'),
        ('us-west-2', 'US West (Oregon)'),
        ('ap-south-1', 'Asia Pacific (Mumbai)'),
        ('ap-southeast-1', 'Asia Pacific (Singapore)'),
        ('ap-southeast-2', 'Asia Pacific (Sydney)'),
        ('ap-northeast-1', 'Asia Pacific (Tokyo)'),
        ('ap-northeast-2', 'Asia Pacific (Seoul)'),
        # ('ap-northeast-3', 'Asia Pacific (Osaka-Local)'),
        ('sa-east-1', 'South America (Sao Paulo)'),
        ('ca-central-1', 'Canada (Central)'),
        ('eu-central-1', 'EU (Frankfurt)'),
        ('eu-west-1', 'EU (Ireland)'),
        ('eu-west-2', 'EU (London)'),
        # ('eu-west-3', 'EU (Paris)'),
        ('eu-central-1', 'EU (Frankfurt)'),
        # ('us-gov-west-1', 'AWS GovCloud (US)'),
    ]
    _availability_zones = [
        'us-east-1a', 'us-east-1b', 'us-east-1c', 'us-east-1d', 'us-east-1e',
        'us-east-1f',
        'us-east-2a', 'us-east-2b', 'us-east-2c',
        'us-west-1a', 'us-west-1c',
        'us-west-2a', 'us-west-2b', 'us-west-2c',
        'ap-south-1a', 'ap-south-1b',
        'ap-southeast-1a', 'ap-southeast-1b',
        'ap-southeast-2a', 'ap-southeast-2b', 'ap-southeast-2c',
        'ap-northeast-1a', 'ap-northeast-1c',
        'ap-northeast-2a', 'ap-northeast-2c',
        'sa-east-1a', 'sa-east-1b', 'sa-east-1c',
        'ca-central-1a', 'ca-central-1b',
        'eu-central-1a', 'eu-central-1b',
        'eu-west-1a', 'eu-west-1b', 'eu-west-1c',
        'eu-west-2a', 'eu-west-2b',
        'eu-central-1c',
    ]
    _instance_id_format = 'i-?????????????????'
    _kernel_id_format = 'aki-????????'
    _image_id_format = 'ami-????????'

    def region(self):
        """
        Returns a tuple (region_code, region_name).

        >>> fake.region()
        ('us-gov-west-1', 'AWS GovCloud (US)')

        :returns: Region
        :rtype: tuple
        """
        return self.random_element(self._regions)

    def region_code(self):
        """
        Returns a region code.

        >>> fake.region_code()
        'us-gov-west-1'

        :returns: Region code
        :rtype: str
        """
        return self.random_element(self._regions)[0]

    def region_name(self):
        """
        Returns a region name.

        >>> fake.region_name()
        'AWS GovCloud (US)'

        :returns: Region name
        :rtype: str
        """
        return self.random_element(self._regions)[1]

    def availability_zone(self, region=None):
        """
        Returns an availability zone code.

        >>> fake.availability_zone()
        'eu-central-1c'

        :param region: Region where availability zone belong to
        :type region: str

        :returns: Availability zone code
        :rtype: str
        """
        region = region or self.region()
        azs = self._availability_zones[:]
        azs = [a for a in azs if a.startswith(region)]
        return self.random_element(azs)

    def hexify(self, text='???', letters=HEX_LETTERS):
        return self.lexify(text, letters)

    def instance_id(self):
        return self.hexify(self._instance_id_format)

    def kernel_id(self):
        return self.hexify(self._kernel_id_format)

    def image_id(self):
        return self.hexify(self._image_id_format)
