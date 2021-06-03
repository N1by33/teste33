
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://inovar.escolasdemira.pt/PortalUnicard/'

payload = {'inUserName': '1116', 'inUserPass': '1111'}

url = 'https://inovar.escolasdemira.pt/PortalUnicard/'
requests.post(url, data=payload)
