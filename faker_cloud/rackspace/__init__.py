# -*- coding: utf-8 -*-
import ipaddress
from faker.providers import file
from faker_cloud import cloud


class Provider(cloud.Provider, file.Provider):
    _ipv4_public_nets = (
        ipaddress.ip_network('134.213.252.0/24'),
        ipaddress.ip_network('95.138.128.0/18'),
    )
