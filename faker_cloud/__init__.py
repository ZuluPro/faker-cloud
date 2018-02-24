"""A collection of fake cloud data for use with faker"""
VERSION = (0, 1)
__version__ = '.'.join([str(i) for i in VERSION])
__author__ = 'Anthony Monthe (ZuluPro)'
__email__ = 'anthony.monthe@gmail.com'
__url__ = 'https://github.com/ZuluPro/faker_cloud/'
__license__ = 'BSD'
__keywords__ = ['cloud', 'test', 'faker', 'amazon web services', 'ec2', 's3',
                'upcloud']

try:
    from .cloud import Provider as BaseCloudProvider
    from .amazon_web_services import Provider as AmazonWebServicesProvider
    from .upcloud import Provider as UpcloudProvider
except ImportError:
    pass
