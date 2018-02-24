# -*- coding: utf-8 -*-
from faker_cloud import cloud


class Provider(cloud.Provider):
    _zones = (
        ('de-fra1', 'Frankfurt #1'),
        ('fi-hel1', 'Helsinki #1'),
        ('nl-ams1', 'Amsterdam #1'),
        ('sg-sin1', 'Singapore #1'),
        ('uk-lon1', 'London #1'),
        ('us-chi1', 'Chicago #1'),
    )
    _datacenters = _zones
    _volume_types = (
        ('MaxIOPS', 'maxiops'),
        ('HDD', 'hdd'),
    )

    def zone(self):
        """
        Returns a tuple (code, name).

        >>> fake.zone()
        ('nl-ams1', 'Amsterdam #1')

        :returns: Zone
        :rtype: tuple
        """
        return self.random_element(self._zones)

    def zone_code(self):
        """
        Returns a zone code.

        >>> fake.zone_name()
        'uk-lon1'

        :returns: Flavor name
        :rtype: str
        """
        return self.random_element(self._zones)[0]

    def zone_name(self):
        """
        Returns a zone name.

        >>> fake.zone_name()
        'Amsterdam #1'

        :returns: Flavor name
        :rtype: str
        """
        return self.random_element(self._zones)[1]
