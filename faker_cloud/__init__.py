"""A collection of fake cloud data for use with faker"""
VERSION = (0, 1)
__version__ = '.'.join([str(i) for i in VERSION])
__author__ = 'Anthony Monthe (ZuluPro)'
__email__ = 'anthony.monthe@gmail.com'
__url__ = 'https://github.com/ZuluPro/faker_cloud/'
__license__ = 'BSD'
__keywords__ = ['cloud', 'test', 'faker', 'amazon web services', 'ec2', 's3',
                'upcloud']

import sys
try:
    from .cloud import Provider as BaseCloudProvider
    from .amazon_web_services import Provider as AmazonWebServicesProvider
    from .upcloud import Provider as UpcloudProvider
except ImportError:
    pass

import ipaddress
if sys.version_info[0] == 2:
    def unicode_ip(func):
        def wrapper(value, *args, **kwargs):
            if isinstance(value, str):
                value = unicode(value)
            return func(value, *args, **kwargs)
        return wrapper
    ipaddress.ip_address = unicode_ip(ipaddress.ip_address)
    ipaddress.ip_network = unicode_ip(ipaddress.ip_network)
