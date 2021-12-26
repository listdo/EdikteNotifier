from logic.edikte_parser import *
from logic.notifier import *

URL = 'https://edikte.justiz.gv.at/edikte/ex/exedi3.nsf/suchedi?SearchView&subf=eex&SearchOrder=4&SearchMax=4999' \
      '&retfields=~VKat=EH%20|%20GW%20|%20UL%20|%20BBL~BL=3&ftquery=&query=%28%5BVKat%5D%3D%28EH%29%20%7C%20%5BVKat' \
      '%5D%3D%28GW%29%20%7C%20%5BVKat%5D%3D%28UL%29%20%7C%20%5BVKat%5D%3D%28BBL%29%29%20AND%20%28%5BBL%5D%3D%283%29' \
      '%29#1640506687597'

CONFIG_PATH = './config/notification.conf'

dataset = get_dataset(URL)
check_and_send_notification(dataset, CONFIG_PATH)