# -*- coding: utf-8 -*-
from faker_cloud import cloud


class Provider(cloud.Provider):
    _regions = (
        ('BHS1', 'Beauharnois 1'),
        ('WAW1', 'Warsaw 1'),
        ('DE1', 'Frankfurt 1'),
        ('UK1', 'London 1'),
        ('SBG3', 'Strasbourg 1'),
    )
    _flavors = (
        ('b2-7', 'ovh.ssd.eg'),
        ('b2-15', 'ovh.ssd.eg'),
        ('b2-30', 'ovh.ssd.eg'),
        ('b2-60', 'ovh.ssd.eg'),
        ('b2-120', 'ovh.ssd.eg'),
        ('b2-7-flex', 'ovh.ssd.eg'),
        ('b2-15-flex', 'ovh.ssd.eg'),
        ('b2-30-flex', 'ovh.ssd.eg'),
        ('b2-60-flex', 'ovh.ssd.eg'),
        ('b2-120-flex', 'ovh.ssd.eg'),
        ('c2-7', 'ovh.ssd.cpu'),
        ('c2-15', 'ovh.ssd.cpu'),
        ('c2-30', 'ovh.ssd.cpu'),
        ('c2-60', 'ovh.ssd.cpu'),
        ('c2-120', 'ovh.ssd.cpu'),
        ('c2-7-flex', 'ovh.ssd.cpu'),
        ('c2-15-flex', 'ovh.ssd.cpu'),
        ('c2-30-flex', 'ovh.ssd.cpu'),
        ('c2-60-flex', 'ovh.ssd.cpu'),
        ('c2-120-flex', 'ovh.ssd.cpu'),
        ('eg-7', 'ovh.ceph.eg'),
        ('eg-15', 'ovh.ceph.eg'),
        ('eg-30', 'ovh.ceph.eg'),
        ('eg-60', 'ovh.ceph.eg'),
        ('eg-120', 'ovh.ceph.eg'),
        ('eg-7-flex', 'ovh.ceph.eg'),
        ('eg-15-flex', 'ovh.ceph.eg'),
        ('eg-30-flex', 'ovh.ceph.eg'),
        ('eg-60-flex', 'ovh.ceph.eg'),
        ('eg-120-flex', 'ovh.ceph.eg'),
        ('eg-7-ssd', 'ovh.ceph.eg'),
        ('eg-15-ssd', 'ovh.ceph.eg'),
        ('eg-30-ssd', 'ovh.ceph.eg'),
        ('eg-60-ssd', 'ovh.ceph.eg'),
        ('eg-120-ssd', 'ovh.ceph.eg'),
        ('eg-7-ssd-flex', 'ovh.ceph.eg'),
        ('eg-15-ssd-flex', 'ovh.ceph.eg'),
        ('eg-30-ssd-flex', 'ovh.ceph.eg'),
        ('eg-60-ssd-flex', 'ovh.ceph.eg'),
        ('eg-120-ssd-flex', 'ovh.ceph.eg'),
        ('hg-7', 'ovh.cpu'),
        ('hg-15', 'ovh.cpu'),
        ('hg-30', 'ovh.cpu'),
        ('hg-60', 'ovh.cpu'),
        ('hg-120', 'ovh.cpu'),
        ('hg-7-flex', 'ovh.cpu'),
        ('hg-15-flex', 'ovh.cpu'),
        ('hg-30-flex', 'ovh.cpu'),
        ('hg-60-flex', 'ovh.cpu'),
        ('hg-120-flex', 'ovh.cpu'),
        ('hg-7-ssd', 'ovh.cpu'),
        ('hg-15-ssd', 'ovh.cpu'),
        ('hg-30-ssd', 'ovh.cpu'),
        ('hg-60-ssd', 'ovh.cpu'),
        ('hg-120-ssd', 'ovh.cpu'),
        ('hg-7-ssd-flex', 'ovh.cpu'),
        ('hg-15-ssd-flex', 'ovh.cpu'),
        ('hg-30-ssd-flex', 'ovh.cpu'),
        ('hg-60-ssd-flex', 'ovh.cpu'),
        ('hg-120-ssd-flex', 'ovh.cpu'),
        ('r2-15', 'ovh.ssd.ram'),
        ('r2-30', 'ovh.ssd.ram'),
        ('r2-60', 'ovh.ssd.ram'),
        ('r2-120', 'ovh.ssd.ram'),
        ('r2-240', 'ovh.ssd.ram'),
        ('r2-15-flex', 'ovh.ssd.ram'),
        ('r2-30-flex', 'ovh.ssd.ram'),
        ('r2-60-flex', 'ovh.ssd.ram'),
        ('r2-120-flex', 'ovh.ssd.ram'),
        ('r2-240-flex', 'ovh.ssd.ram'),
        ('s1-2', 'ovh.vps-ssd'),
        ('s1-4', 'ovh.vps-ssd'),
        ('s1-8', 'ovh.vps-ssd'),
        ('sp-30', 'ovh.vps-ssd'),
        ('sp-60', 'ovh.vps-ssd'),
        ('sp-120', 'ovh.vps-ssd'),
        ('sp-240', 'ovh.vps-ssd'),
        ('sp-30-flex', 'ovh.vps-ssd'),
        ('sp-60-flex', 'ovh.vps-ssd'),
        ('sp-120-flex', 'ovh.vps-ssd'),
        ('sp-240-flex', 'ovh.vps-ssd'),
        ('sp-30-ssd', 'ovh.vps-ssd'),
        ('sp-60-ssd', 'ovh.vps-ssd'),
        ('sp-120-ssd', 'ovh.vps-ssd'),
        ('sp-240-ssd', 'ovh.vps-ssd'),
        ('sp-30-ssd-flex', 'ovh.vps-ssd'),
        ('sp-60-ssd-flex', 'ovh.vps-ssd'),
        ('sp-120-ssd-flex', 'ovh.vps-ssd'),
        ('sp-240-ssd-flex', 'ovh.vps-ssd'),
        ('vps-ssd-1', 'ovh.vps-ssd'),
        ('vps-ssd-2', 'ovh.vps-ssd'),
        ('vps-ssd-3', 'ovh.vps-ssd'),

        ('win-b2-7', 'ovh.ssd.eg'),
        ('win-b2-15', 'ovh.ssd.eg'),
        ('win-b2-30', 'ovh.ssd.eg'),
        ('win-b2-60', 'ovh.ssd.eg'),
        ('win-b2-120', 'ovh.ssd.eg'),
        ('win-b2-7-flex', 'ovh.ssd.eg'),
        ('win-b2-15-flex', 'ovh.ssd.eg'),
        ('win-b2-30-flex', 'ovh.ssd.eg'),
        ('win-b2-60-flex', 'ovh.ssd.eg'),
        ('win-b2-120-flex', 'ovh.ssd.eg'),
        ('win-c2-7', 'ovh.ssd.cpu'),
        ('win-c2-15', 'ovh.ssd.cpu'),
        ('win-c2-30', 'ovh.ssd.cpu'),
        ('win-c2-60', 'ovh.ssd.cpu'),
        ('win-c2-120', 'ovh.ssd.cpu'),
        ('win-c2-7-flex', 'ovh.ssd.cpu'),
        ('win-c2-15-flex', 'ovh.ssd.cpu'),
        ('win-c2-30-flex', 'ovh.ssd.cpu'),
        ('win-c2-60-flex', 'ovh.ssd.cpu'),
        ('win-c2-120-flex', 'ovh.ssd.cpu'),
        ('win-eg-7', 'ovh.ceph.eg'),
        ('win-eg-15', 'ovh.ceph.eg'),
        ('win-eg-30', 'ovh.ceph.eg'),
        ('win-eg-60', 'ovh.ceph.eg'),
        ('win-eg-120', 'ovh.ceph.eg'),
        ('win-eg-7-flex', 'ovh.ceph.eg'),
        ('win-eg-15-flex', 'ovh.ceph.eg'),
        ('win-eg-30-flex', 'ovh.ceph.eg'),
        ('win-eg-60-flex', 'ovh.ceph.eg'),
        ('win-eg-120-flex', 'ovh.ceph.eg'),
        ('win-eg-7-ssd', 'ovh.ceph.eg'),
        ('win-eg-15-ssd', 'ovh.ceph.eg'),
        ('win-eg-30-ssd', 'ovh.ceph.eg'),
        ('win-eg-60-ssd', 'ovh.ceph.eg'),
        ('win-eg-120-ssd', 'ovh.ceph.eg'),
        ('win-eg-7-ssd-flex', 'ovh.ceph.eg'),
        ('win-eg-15-ssd-flex', 'ovh.ceph.eg'),
        ('win-eg-30-ssd-flex', 'ovh.ceph.eg'),
        ('win-eg-60-ssd-flex', 'ovh.ceph.eg'),
        ('win-eg-120-ssd-flex', 'ovh.ceph.eg'),
        ('win-hg-7', 'ovh.cpu'),
        ('win-hg-15', 'ovh.cpu'),
        ('win-hg-30', 'ovh.cpu'),
        ('win-hg-60', 'ovh.cpu'),
        ('win-hg-120', 'ovh.cpu'),
        ('win-hg-7-flex', 'ovh.cpu'),
        ('win-hg-15-flex', 'ovh.cpu'),
        ('win-hg-30-flex', 'ovh.cpu'),
        ('win-hg-60-flex', 'ovh.cpu'),
        ('win-hg-120-flex', 'ovh.cpu'),
        ('win-hg-7-ssd', 'ovh.cpu'),
        ('win-hg-15-ssd', 'ovh.cpu'),
        ('win-hg-30-ssd', 'ovh.cpu'),
        ('win-hg-60-ssd', 'ovh.cpu'),
        ('win-hg-120-ssd', 'ovh.cpu'),
        ('win-hg-7-ssd-flex', 'ovh.cpu'),
        ('win-hg-15-ssd-flex', 'ovh.cpu'),
        ('win-hg-30-ssd-flex', 'ovh.cpu'),
        ('win-hg-60-ssd-flex', 'ovh.cpu'),
        ('win-hg-120-ssd-flex', 'ovh.cpu'),
        ('win-r2-15', 'ovh.ssd.ram'),
        ('win-r2-30', 'ovh.ssd.ram'),
        ('win-r2-60', 'ovh.ssd.ram'),
        ('win-r2-120', 'ovh.ssd.ram'),
        ('win-r2-240', 'ovh.ssd.ram'),
        ('win-r2-15-flex', 'ovh.ssd.ram'),
        ('win-r2-30-flex', 'ovh.ssd.ram'),
        ('win-r2-60-flex', 'ovh.ssd.ram'),
        ('win-r2-120-flex', 'ovh.ssd.ram'),
        ('win-r2-240-flex', 'ovh.ssd.ram'),
        ('win-sp-30', 'ovh.vps-ssd'),
        ('win-sp-60', 'ovh.vps-ssd'),
        ('win-sp-120', 'ovh.vps-ssd'),
        ('win-sp-240', 'ovh.vps-ssd'),
        ('win-sp-30-flex', 'ovh.vps-ssd'),
        ('win-sp-60-flex', 'ovh.vps-ssd'),
        ('win-sp-120-flex', 'ovh.vps-ssd'),
        ('win-sp-240-flex', 'ovh.vps-ssd'),
        ('win-sp-30-ssd', 'ovh.vps-ssd'),
        ('win-sp-60-ssd', 'ovh.vps-ssd'),
        ('win-sp-120-ssd', 'ovh.vps-ssd'),
        ('win-sp-240-ssd', 'ovh.vps-ssd'),
        ('win-sp-30-ssd-flex', 'ovh.vps-ssd'),
        ('win-sp-60-ssd-flex', 'ovh.vps-ssd'),
        ('win-sp-120-ssd-flex', 'ovh.vps-ssd'),
        ('win-sp-240-ssd-flex', 'ovh.vps-ssd'),
    )

    def region(self):
        """
        Returns a tuple (code, name).

        >>> fake.region()
        ('UK1', 'London 1')

        :returns: Region
        :rtype: tuple
        """
        return self.random_element(self._regions)

    def region_code(self):
        """
        Returns a region code.

        >>> fake.region_name()
        'UK1"

        :returns: Region code
        :rtype: str
        """
        return self.random_element(self._regions)[0]

    def region_name(self):
        """
        Returns a region name.

        >>> fake.region_name()
        "London 1"

        :returns: Region name
        :rtype: str
        """
        return self.random_element(self._regions)[1]

    def datacenter(self):
        return self.region()

    def project_id(self):
        return self.hexify('?'*32)
