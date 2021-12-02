import requests

counter=1

for num in range(51):
    x = requests.get('http://10.4.76.214:2224/fast').text
    print(f"counter: {counter}")
    counter += 1
# plaintext is returned..if you wanted json, you would say json()


