import requests

'''处理超时等待，方法中增加timeout'''
r = requests.get(url='',timeout=0.001)
r.text
