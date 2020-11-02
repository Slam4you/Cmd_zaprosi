import requests

with open(r"C:\Users\Slam\Documents\dataset_3378_2.txt") as dat:
    url = dat.readline().strip()
    print(url)
site = requests.get(url)
print('Строк: ', len(site.text.splitlines()))


