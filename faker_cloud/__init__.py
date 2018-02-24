"""A collection of fake cloud data for use with faker"""
VERSION = (0, 1)
__version__ = '.'.join([str(i) for i in VERSION])
__author__ = 'Anthony Monthe (ZuuPro)'
__email__ = 'anthony.monthe@gmail.com'
__url__ = 'https://github.com/ZuluPro/faker_cloud/'
__license__ = 'BSD'
__keywords__ = ['cloud', 'test', 'faker', 'amazon web services', 'ec2', 's3',
                'upcloud']

from .cloud import Provider
from .amazon_web_services import Provider as AmazonWebServicesProvider
from .upcloud import Provider as UpcloudProvider
