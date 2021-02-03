import bs4
import requests
import os

download_path = './data/'
cookie = dict(BAZAAR='k45deend8ubhl60q16sdq6il24')
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',}
html_file = requests.get('https://bazaar.abuse.ch/browse.php?search=tag%3ARansomware', headers=header)
# print(html_file)
objsoup = bs4.BeautifulSoup(html_file.text, 'lxml')
td = objsoup.find('tbody')
print(type(td), len(td))
malware_td = td.find('tr')
# print(type(malware_td), len(malware_td))
malware_tr = malware_td.find('a')
# print(td.find_all('tr')[0])
# print(type(malware_tr), len(malware_tr))
hash_ = []
signature_ = []
for item in td.find_all('tr'):
    item_2 = item.find_all('a')
    # print(item_2)
    if not 'exe' in item.text:
        print(item.text)
        # print(item.find('img')['alt'])
        continue
    hash_.append(item_2[0].text)
    if 'signature' in item_2[1]['href']:
        signature_.append(item_2[1].text)
    else:
        signature_.append('None')
# print(signature_)
print('Start to download')
i = 1
for hash_item, signature_item in zip(hash_, signature_):

    download_ = requests.post('https://mb-api.abuse.ch/api/v1/',{'query':'get_file','sha256_hash':hash_item}, timeout=15, headers={ 'API-KEY': '' }, allow_redirects=True)
    path_list = os.listdir(download_path)

    if not os.path.exists(download_path + signature_item):
        
        os.mkdir(download_path + signature_item )

    with open(download_path + signature_item + '/'+hash_item+ '.zip', "wb") as file:
            response = download_
            file.write(response.content)

    print(str(i/len(signature_)*100)[:6] + '%',end='\r',flush=True)
    i += 1

