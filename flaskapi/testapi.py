import requests

URL = 'http://10.4.76.214:2224/awesome/stuffo' 

def main():

    r = requests.get(URL)
    print (r.text)

main()
