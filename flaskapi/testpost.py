import requests

# the URL you wish to post to
url = 'http://10.4.76.214:2224/post'

# the data you wish to post
ye_olde_dict = {'age': '34'}

x = requests.post(url, json = ye_olde_dict)

print(x.text)
