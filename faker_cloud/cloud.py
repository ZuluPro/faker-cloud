import ipaddress
import string
from faker.providers import BaseProvider


class Provider(BaseProvider):
    _datacenters = (
        ('cam', 'Cameroun'),
        ('pt', 'Portugal'),
        ('es', 'Spain'),
    )
    _volume_types = (
        ('HDD', 'hdd'),
        ('SSD', 'ssd'),
    )

    def hexify(self, text='???'):
        return self.lexify(text, string.hexdigits[:-6])

    def datacenter(self):
        """
        Returns a datacenter.

        >>> fake.datacenter()
        ('London #1', 'uk-lon1')

        :returns: Tuple with (verbose_name, code)
        :rtype: tuple
        """
        return self.random_element(self._datacenters)

    def datacenter_code(self):
        """
        Returns a datacenter code.

        >>> fake.datacenter_code()
        'uk-lon1'

        :returns: Datacenter code
        :rtype: str
        """
        return self.datacenter()[0]

    def datacenter_name(self):
        """
        Returns a datacenter name.

        >>> fake.datacenter_name()
        'London #1'

        :returns: Datacenter name
        :rtype: str
        """
        return self.datacenter()[1]

    def flavor_name(self):
        """
        Returns a flavor name.

        >>> fake.flavor_name()
        '2CPU-8GB'

        :returns: Flavor name
        :rtype: str
        """
        cpu_number = self.random_int(1, 192)
        memory = self.random_int(cpu_number, cpu_number*8)
        name = '%dCPU-%dGB' % (cpu_number, memory)
        return name

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

    def ipv4_public(self):
        """
        Returns an cloud's public IPv4 or random IPv4

        >>> fake.ipv4_public()
        IPv4Address('52.162.42.6')

        :returns: IPv4
        :rtype: ipaddress.IPv4Address
        """
        if getattr(self, '_ipv4_public_nets'):
            net = self.random_element(self._ipv4_public_nets)
            min_ip = net[1]._ip
            max_ip = net[-2]._ip
            ip = ipaddress.IPv4Address(self.random_int(min_ip, max_ip))
            return ip
        return self.ipv4()
