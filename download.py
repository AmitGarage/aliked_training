import os
import requests

from urllib.parse import urlparse

username = 'amit.singh@visionetsystems.com'
password = 'Aastha5@nistha'

url = 'https://visionetsys-my.sharepoint.com/:u:/r/personal/amit_singh_visionetsystems_com/Documents/MegaDepth_v1.tar.gz?csf=1&web=1&e=HwMT9w'
filename = "MegaDepth.tar.gz"#os.path.basename(urlparse(url).path)

r = requests.get(url, auth=(username,password))

if r.status_code == 200:
   with open(filename, 'wb') as out:
      for bits in r.iter_content():
          out.write(bits)
