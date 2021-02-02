import bs4
import requests

download_path = './data/'
cookie = dict(BAZAAR='k45deend8ubhl60q16sdq6il24')
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',}
html_file = requests.get('https://bazaar.abuse.ch/browse.php?search=file_type%3Aexe', headers=header)
print(html_file)
objsoup = bs4.BeautifulSoup(html_file.text, 'lxml')
td = objsoup.find('tbody')
print(type(td), len(td))
malware_td = td.find('tr')
# print(type(malware_td), len(malware_td))
malware_tr = malware_td.find_all('a')
# print(type(malware_tr), len(malware_tr))
hash_ = []
hash_.append(malware_tr[0])
for item in malware_tr:
    print(item.text)
print('b')
url = []

for item in malware_tr:
    print(item['href'], item['title'])
    if 'download' in item['title']:
        url.append(item['href'])


download_ = requests.post('https://mb-api.abuse.ch/api/v1/',{'query':'get_file','sha256_hash':hash_[0]}, timeout=15, headers={ 'API-KEY': '' }, allow_redirects=True)
print(download_)
with open(download_path+'a.zip', "wb") as file:
    # get request
    response = download_
    # write to file
    file.write(response.content)


