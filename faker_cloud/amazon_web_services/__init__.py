# -*- coding: utf-8 -*-
import ipaddress
from faker.providers import file
from faker_cloud import cloud


class Provider(cloud.Provider, file.Provider):
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
    _instance_types = (
        't2.nano', 't2.micro', 't2.small', 't2.medium', 't2.large', 't2.xlarge', 't2.2xlarge',
        'm4.large', 'm4.xlarge', 'm4.2xlarge', 'm4.4xlarge', 'm4.10xlarge', 'm4.16xlarge ',
        'm5.large', 'm5.xlarge', 'm5.2xlarge', 'm5.4xlarge', 'm5.12xlarge', 'm5.24xlarge',
        'c4.large', 'c4.xlarge', 'c4.2xlarge', 'c4.4xlarge', 'c4.8xlarge',
        'c5.large', 'c5.xlarge', 'c5.2xlarge', 'c5.4xlarge', 'c5.9xlarge', 'c5.18xlarge',
        'r4.large', 'r4.xlarge', 'r4.2xlarge', 'r4.4xlarge', 'r4.8xlarge', 'r4.16xlarge',
        'x1.16xlarge', 'x1.32xlarge',
        'x1e.xlarge', 'x1e.2xlarge', 'x1e.4xlarge', 'x1e.8xlarge', 'x1e.16xlarge', 'x1e.32xlarge',
        'd2.xlarge', 'd2.2xlarge', 'd2.4xlarge', 'd2.8xlarge',
        'h1.2xlarge', 'h1.4xlarge', 'h1.8xlarge', 'h1.16xlarge',
        'i3.large', 'i3.xlarge', 'i3.2xlarge', 'i3.4xlarge', 'i3.8xlarge', 'i3.16xlarge',
        'f1.2xlarge', 'f1.16xlarge',
        'g3.4xlarge', 'g3.8xlarge', 'g3.16xlarge',
        'p2.xlarge', 'p2.8xlarge', 'p2.16xlarge',
        'p3.2xlarge', 'p3.8xlarge', 'p3.16xlarge',
        'm1.small', 'm1.medium', 'm1.large', 'm1.xlarge',
        'm3.medium', 'm3.large', 'm3.xlarge', 'm3.2xlarge',
        'c1.medium', 'c1.xlarge',
        'cc2.8xlarge',
        'c3.large', 'c3.xlarge', 'c3.2xlarge', 'c3.4xlarge', 'c3.8xlarge',
        'm2.xlarge', 'm2.2xlarge', 'm2.4xlarge',
        'cr1.8xlarge',
        'r3.large', 'r3.xlarge', 'r3.2xlarge', 'r3.4xlarge', 'r3.8xlarge',
        'hs1.8xlarge',
        'i2.xlarge', 'i2.2xlarge', 'i2.4xlarge', 'i2.8xlarge',
        'g2.2xlarge', 'g2.8xlarge',
        't1.micro',
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

    def instance_type_serie(self):
        """
        Returns an instance type serie.

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

    def instance_type(self, serie=None):
        """
        Returns an instance type.

        >>> fake.instance_type()
        'm5.2xlarge'
        >>> fake.instance_type(serie='m5')
        'm5.4xlarge'

        :param serie: Optional filter for instance type serie
        :type serie: str

        :returns: Instance type
        :rtype: str
        """
        serie = serie or self.instance_type_serie_name()
        its = [i for i in self._instance_types
               if i.startswith(serie)]
        return self.random_element(its)

    def flavor_name(self):
        return self.instance_type()

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
