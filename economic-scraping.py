Microsoft Windows [Version 10.0.18362.356]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\r40815014>python
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> from bs4 import BeautifulSoup
>>> r=requests.get("https://www.nikkei.com/markets/worldidx/chart/nk225/")
>>> soup=BeautifulSoup(r.content,"html.parser")
>>> print(soup.find("span","economic_value_now a-fs26").string)
21,798.87