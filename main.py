from requests import get
ip = get('https://api.ipify.org').text
a = get(f'https://ipinfo.io/{format(ip)}/geo').json()
print(a['country'])