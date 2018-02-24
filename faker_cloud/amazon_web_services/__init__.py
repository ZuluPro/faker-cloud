# -*- coding: utf-8 -*-
import ipaddress
from faker.providers import BaseProvider
from faker.providers import file

HEX_LETTERS = '0123456789abcdef'


class AmazonWebServicesProvider(file.Provider):
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
    _volume_types = (
        ('Cold HDD', 'sc1'),
        ('General Purpose SSD', 'gp2'),
        ('Magnetic', 'standard'),
        ('Throughput Optimized HDD', 'st1'),
        ('Provisioned IOPS SSD', 'io1'),
    )
    _instance_type_series = (
        ('t1', 'Burstable Performance 1'),
        ('t2', 'Burstable Performance 2'),
        ('m1', 'General Purpose 1'),
        ('m2', 'General Purpose 2'),
        ('m3', 'General Purpose 3'),
        ('m4', 'General Purpose 4'),
        ('m5', 'General Purpose 5'),
        ('p2', 'Accelerated computing'),
        ('c1', 'Compute Optimized 1'),
        ('c3', 'Compute Optimized 3'),
        ('c4', 'Compute Optimized 4'),
        ('c5', 'Compute Optimized 5'),
        ('r3', 'Memory optimized R3'),
        ('r4', 'Memory optimized R4'),
        ('i2', 'Storage optimized I2'),
        ('i3', 'Storage optimized I3'),
        ('d2', 'Storage optimized D2'),
        ('g2', 'GPU optimized 2'),
        ('g3', 'GPU optimized 3'),
        ('cc2', 'Accelerated computing CC2'),
        ('cr1', 'Memory optimized CR1'),
        ('x1', 'Memory optimized X1'),
        ('x1e', 'Memory optimized X1E'),
        ('hs1', 'Storage optimized HS1'),
        ('h1', 'Storage optimized H1'),
    )
    _instance_id_format = 'i-?????????????????'
    _kernel_id_format = 'aki-????????'
    _ami_id_format = 'ami-????????'
    _sg_id_format = 'sg-????????'
    _volume_id_format = 'vol-?????????????????'
    _vpc_id_format = 'vpc-????????'
    _snapshot_id_format = 'snap-????????'
    _ipv4_public_net = ipaddress.IPv4Network('54.160.0.0/12')
    _ec2_public_dns_format = 'ec2-{ip}.compute-1.amazonaws.com'
    _s3_object_url_format = 'https://s3.amazonaws.com/{bucket_name}/{obj_name}'

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
        """
        Returns an instance ID.

        >>> fake.instance_id()
        'i-055a44951998d0d12'

        :returns: Instance ID
        :rtype: str
        """
        return self.hexify(self._instance_id_format)

    def kernel_id(self):
        """
        Returns an kernel ID.

        >>> fake.kernel_id()
        'aki-919dcaf8'

        :returns: Kernel ID
        :rtype: str
        """
        return self.hexify(self._kernel_id_format)

    def ami_id(self):
        """
        Returns an AMI ID.

        >>> fake.ami_id()
        'ami-919dcbf8'

        :returns: AMI ID
        :rtype: str
        """
        return self.hexify(self._ami_id_format)

    def security_group_id(self):
        """
        Returns an security group ID.

        >>> fake.security_group_id()
        'sg-919dcbf8'

        :returns: Security group ID
        :rtype: str
        """
        return self.hexify(self._sg_id_format)

    def vpc_id(self):
        """
        Returns an VPC ID.

        >>> fake.vpc_id()
        'vpc-119dcbf8'

        :returns: VPC ID
        :rtype: str
        """
        return self.hexify(self._vpc_id_format)

    def volume_id(self):
        """
        Returns an volume ID.

        >>> fake.volume_id()
        'vol-04ceccde3881f8f6e'

        :returns: Volume ID
        :rtype: str
        """
        return self.hexify(self._volume_id_format)

    def volume_type(self):
        """
        Returns an volume type.

        >>> fake.volume_type()
        ('General Purpose SSD', 'gp2')

        :returns: Tuple with (verbose_name, code)
        :rtype: tuple
        """
        return self.random_element(self._volume_types)

    def volume_type_name(self):
        """
        Returns an volume type name.

        >>> fake.volume_type_name()
        'General Purpose SSD'

        :returns: Volume type name
        :rtype: str
        """
        return self.random_element(self._volume_types)[0]

    def volume_type_code(self):
        """
        Returns an volume type code.

        >>> fake.volume_type_code()
        'gp2'

        :returns: Volume type code
        :rtype: str
        """
        return self.random_element(self._volume_types)[1]

    def instance_type_serie(self):
        """
        Returns an volume type.

        >>> fake.instance_type_serie()
        ('m5', 'General Purpose 5')

        :returns: Tuple with (name, verbose_name)
        :rtype: tuple
        """
        return self.random_element(self._instance_type_series)

    def instance_type_serie_name(self):
        """
        Returns an instance type serie name.

        >>> fake.instance_type_serie_name()
        'm5'

        :returns: Instance type serie name
        :rtype: str
        """
        return self.random_element(self._instance_type_series)[0]

    def instance_type_serie_verbose_name(self):
        """
        Returns an instance type serie verbose name.

        >>> fake.instance_type_serie_verbose_name()
        'General Purpose 5'

        :returns: Instance type serie verbose name
        :rtype: str
        """
        return self.random_element(self._instance_type_series)[1]

    def snapshot_id(self):
        """
        Returns an snapshot ID.

        >>> fake.snapshot_id()
        'vol-04ceccde3881f8f6e'

        :returns: Snapshot ID
        :rtype: str
        """
        return self.hexify(self._snapshot_id_format)

    def ipv4_public(self):
        """
        Returns an AWS public IPv4.

        >>> fake.ipv4_public()
        IPv4Address('52.162.42.6')

        :returns: Public AWS IPv4
        :rtype: ipaddress.IPv4Address
        """
        min_ip = self._ipv4_public_net[1]._ip
        max_ip = self._ipv4_public_net[-2]._ip
        ip = ipaddress.IPv4Address(self.random_int(min_ip, max_ip))
        return ip

    def ec2_public_dns(self, ip=None):
        """
        Returns an EC2 domain name bound to an IPv4.

        >>> fake.ec2_public_dns()
        'ec2-52-162-42-6.compute-1.amazonaws.com'

        :returns: Public DNS
        :rtype: str
        """
        ip = str(ip or self.ipv4_public()).replace('.', '-')
        dns = self._ec2_public_dns_format.format(ip=ip)
        return dns

    def s3_object_url(self, bucket_name=None, obj_name=None):
        """
        Returns a S3 URL to an object.

        >>> fake.s3_object_url()
        'https://s3.amazonaws.com/Ham/Let

        :returns: A URL
        :rtype: str
        """
        bucket_name = bucket_name or self.file_extension()
        obj_name = obj_name or self.file_name(extension=bucket_name)
        return self._s3_object_url_format.format(bucket_name=bucket_name,
                                                 obj_name=obj_name)
