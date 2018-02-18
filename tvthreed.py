import os
import sys
import requests
import time
import distutils.dir_util
import codecs

#Path to Configuration Files
ip_addr_file = 'braviaConfIP.conf'

#File header   
headers = {  
    'User-Agent': 'TVSideView/2.0.1 CFNetwork/672.0.8 Darwin/14.0.0',
    'Content-Type': 'text/xml; charset=UTF-8',
    'SOAPACTION': '"urn:schemas-sony-com:service:IRCC:1#X_SendIRCC"',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}
#Store .xml information as command.
command3d = """<?xml version="1.0"?>  
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">  
  <s:Body>
    <u:X_SendIRCC xmlns:u="urn:schemas-sony-com:service:IRCC:1">
      <IRCCCode>AAAAAgAAAHcAAABNAw==</IRCCCode>
    </u:X_SendIRCC>
  </s:Body>
</s:Envelope>"""

if os.path.isfile(ip_addr_file):
    fip = codecs.open(ip_addr_file, 'r', encoding="utf-8")
    for line in fip:
        url = ("http://"+line+"/sony/IRCC")
        response = requests.post(url, data=command3d, headers=headers)


