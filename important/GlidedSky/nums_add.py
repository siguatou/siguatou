import requests
from lxml import etree
url = 'http://www.glidedsky.com/level/web/crawler-basic-1'

headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Language':'en-US,en;q=0.9',
'Cookie':'_ga=GA1.2.301140318.1656061103; __gads=ID=a82b6b8e31c127a5-2246b7fdaed3003f:T=1656061103:RT=1656061103:S=ALNI_MYFFUuiYzqXcYBNazG4AesWDKov8A; footprints=eyJpdiI6IkFVMEt4TVVhTTN2T3pOV2JVUUgwTHc9PSIsInZhbHVlIjoicjR6ajl6dUlSQXN4UHRzbUsycVIrdjQ5VmhldU81eUtRVVdrdEdkREJNamNJeVlBWmYyRFUzSXdxc3B4MGZ5UCIsIm1hYyI6ImViNWE4YWQyODRiMDdkNGUxNzFhN2JhM2QzMWE2MmEwYzIwNWQyNTllZWMyMGQyNDk5ZGUyYjEyNzYxNjdhYWIifQ%3D%3D; _gid=GA1.2.1968617040.1658216778; __gpi=UID=000006869fc7331a:T=1656061103:RT=1658216778:S=ALNI_MZ2niYQu-9XH4jRyK072Gavwa52HQ; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1656061104,1658216779; XSRF-TOKEN=eyJpdiI6Ikl3dGFiZ2pNTGVEbE5nWGdSb2x4V0E9PSIsInZhbHVlIjoiaVFJUTROSlUrYVdXMG1pRnBGWjM3dDFHN3FsbDZ5Y2hsMGZHN1hGc2syMTlWbU5zZTF6dzRaM1wvZEdlREdzYlQiLCJtYWMiOiI3Yzg3OWE5NGJlNmE4NmIzNGZhZjVhODExMTJmZmMxY2ExZTBmMDc1OTc2MWVlMmNlYzZiZjViOTY4M2NlODU3In0%3D; glidedsky_session=eyJpdiI6IkpOVlpINGVUdWdBZzFtUFlrVXMwd2c9PSIsInZhbHVlIjoic2tWZjZkSVlqU0wrZU1VckxlNGxOMjVxa21FVmhtZThVcWYwZTFPaEtueHZDRDJFUSt3dStseXd6TFwvYXdOTGQiLCJtYWMiOiJkNGYzMTZhYzQ1NzYxNzk0MTJjZjRhODRjZGUxNzRiOWUwYmFiNjRjMjIwZWQ0OWMzYWU0NTY3MDFlNGFmNmJkIn0%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1658216801',
'Host':'www.glidedsky.com',
'Referer':'http://www.glidedsky.com/level/crawler-basic-1',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
res = requests.get(url=url,headers=headers)
print(res.text)
html = etree.HTML(res.text)
print(html)
nodes = html.xpath("//div[@class='col-md-1']")
print(nodes)

num_total = 0
for node in nodes:
    num = node.text
    num_total += int(num)

print(num_total)





