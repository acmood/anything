# Scrapy settings for lou project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'lou'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['lou.spiders']
NEWSPIDER_MODULE = 'lou.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

