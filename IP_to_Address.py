#!/usr/bin/env python
# __coding:utf8__
# IP transfer to Country & City etc.
# 2015-11-06

'''
Install instructions
--- Install from source
1. download GeoIP-version.tar.gz from https://pypi.python.org/pypi/GeoIP/
2. tar zxvf GeoIP-version.tar.gz
3. cd GeoIP-version
4. python setup.py build
5. python setup.py install

--- Install from pip:
1. pip install GeoIP
'''

import GeoIP,time

# define the file of GeoIP file
geodb=raw_input("Please input the path of GeoIP data file: ")


gi = GeoIP.open(geodb,GeoIP.GEOIP_STANDARD)


with open(raw_input('Please input a filename: '),'r') as ip_list:
	for i in ip_list.readlines():
		j = i.strip()
		print j
		print gi.record_by_addr(j)
		#time.sleep(1)