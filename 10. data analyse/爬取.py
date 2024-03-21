import requests
import re
import json
import pprint
url='https://www.zhihu.com/question/633134172'
headers ={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
'Cookie':'SESSIONID=udzM9qrzkdaT9VoYGjKS2FMUHWb22vA8V1jyLgUlPu6; JOID=WlASCkvpGiRQFs7_XugS_fTLPTtGk11eNla7hiSMKh8Ga7C2MsHYTTQewf5ZKvxxMgAhev9wq4PrZjMWeaqCrY4=; osd=VlkdAE_lEytaEsL2UeIW8f3ENz9KmlJUMlqyiS6IJhYJYbS6O87SSTgXzvRdJvV-OAQtc_B6r4_iaTkSdaONp4o=; __snaker__id=1ORNIjQXP9mKVX04; _zap=9c866681-3c01-490a-a339-babd49c7b26c; d_c0=APAVQ9nyzBePThERHFp2RynWRjfa5dNrmSk=|1701670860; YD00517437729195%3AWM_TID=eRJpAshGbzlAAARUVQeV8BtL37EVR040; _xsrf=af020e0f-8e23-4287-bce2-846a7397c560; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1701670864,1701757515; SESSIONID=zHtoHuvtm04XtvIciR3uKsqeiDOEw5iQGUOsvuEEAJC; JOID=WlsWBk5oWifTg9rgE2Vc-nBfJSoPGRJVvMaklmEIYRON96GicAKeT7uF0eYV5IyB4jJsKe8VXEGBVtFtrBH7-ok=; osd=WloUC0hoWyXehdrhEWha-nFdKCwPGBBYusallGwOYRKP-qeicQCTSbuE0-sT5I2D7zRsKO0YWkGAVNxrrBD5948=; gdxidpyhxdE=L0Nb4pQ57bplfErcDVSvEIhIX9vH6Ppwb5EhsotgPLxrmr%2F%5CalncVUzpaDNwr%2F6OG1xOsepReL6kUiCfiaxjodRfgdOvdgc2y%2BT1dyuYTIGnYLop8JLGMDRTjQeBS%5CoO9qoHkiiaxw%5C58V7DuBYDacjsebXpQ5c4sR4EVdOGNYMs%2BgsI%3A1701758442968; YD00517437729195%3AWM_NI=WhsyCfVFGW9NJqgTr6HR2QSRWpCuqSPqT3wPtONFdgxL6BN5%2BVQnke8bq%2BLAd6kGGJj8NFtGuxEAcN2%2Fhnqoj%2FcNnWRI9cq%2Fm9y7OGVuawN93raIavA0MehFb%2FdzGPxNVnI%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee92f26293beaf90d3598c9e8ab2c44e868a9e87d83383f19bd3c780fb888795e82af0fea7c3b92a95b8bd9ac26e969a89b8bc468aafa9b5f13e8c8efeb2d25a95b08d96f45994af9cd4f65cb89182a7e76dbc94faa3cd3fe98a9f8fea6ffcbebfcccf4ba8eaa5a8c642aae882a7f74db7a88ba2e246f2f1a88ff465aaf1adafed5d9297f784f425afe7b7d8ce4d96abaf98cd33f1aeafaae47e83f08386eb4ea2f1ac9bc65cbc929a8fcc37e2a3; captcha_session_v2=2|1:0|10:1701757600|18:captcha_session_v2|88:TjdBNkRkODJjaFJvQURGYnJhUXExWTZpUmVWYjhybGFWdG5LNkVjTDVoS2kwTzBMNG55enBScU84ekhxYW1OUg==|0003bbfcc010612c2c0a80f57ac5a8c3c06fe0b727d63be4c97597897dd2fbf9; captcha_ticket_v2=2|1:0|10:1701757609|17:captcha_ticket_v2|728:eyJ2YWxpZGF0ZSI6IkNOMzFfQ2dBTWNCelc2TjFRNEZvb2UyQTBtbE9HdlVncEZaOVV0ZHhhUGVHenhOLmFwTlRVOGxzX29pbWw0RE91UldGc3RsYzQxaDh3VU0xdDg2YlNsb2xWZ3dCbkFZanBiWnhyR0JJWXJKZGtxVDNwOFBpeUtUTG1FT3dnY2FNSlpaakgqTVBqVG1CcWpNc2lRbzJWZEFZWExxUmpLOFJVeUZ1cWFMbnlnVWxJSm1pQXVPaEtUbmJfekJmYTRYRGoqRUg5Ti5oZUlaTEwyckxKdVpmYmx1UThkMElSZVFocEIzOTE1RUJKelllOF9ZVEhrM3djSE9QMTRTczVoRldqNnZ4Qk91MExFM00uckJpRUhsWXFlSTNnRHJtV2RWRzBLeDJaelpEV2QqaSpYdGZQaklSTndIb2hXVzlDeWdxa0ZhcTJxdFZfaGEzeTU1d2prUnNkeXVkUFFwbXdIQUVkRmYwb2JPem5veVl2QlloOG5ERkRDVzBzWkhCaGRvMWJIKnY5dTBWc3ZDbFJDSVR2ekR5aDVKd3I0U0ZPWGYzS09BKkVMRGNPV3I5RXhxc1lyQ0FDZEJCNlJhdGwxZGZuUjAwNV80YVZfVGdJUDY5STRKNFBGLmMzQ2JpZ3dTSGVYblZSdXlOaUVsZCo1R1huSVMyNlB3Z3RveFVTYUNNOEZ6M3dESUkyRWc3N192X2lfMSJ9|4f8ac53d1ca8d643cc9d630901a03d334fbd452017be9f2b5f4a6a307fb168e9; z_c0=2|1:0|10:1701757669|4:z_c0|92:Mi4xdXJ4SVRBQUFBQUFBOEJWRDJmTE1GeVlBQUFCZ0FsVk41UkJjWmdERUhsVm93MWJTSzR2REZQcnNfbjFlS1dNelJB|8489946ba5fcc5c1640c770a9b2cd1cbf2e9b3695cdddffc4e30b8939e82e01c; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1701757734; KLBRSID=031b5396d5ab406499e2ac6fe1bb1a43|1701757847|1701757514'
}


response = requests.get(url =url,headers=headers)
#print(response.text)
#成功拿到源码
#抓取标题
title = re.findall('<title data-rh="true">(.*?)</title>',response.text)[0]
#抓取答案
html_data = re.findall('<script id="js-initialData" type="text/json">(.*?)</script>',response.text)[0]
# print(html_data)#字符串类型
# print('----------------这里是分隔符---------------')
#接下来就是将字符串变成字典类型，使用json_data对象接收
json_data = json.loads(html_data)
# print(json_data)#这里是长的一条，在控制台输出则不好看，为了好看，则需要pprint库格式化。#这里就成功的将字符串转成字典，字典是用花括号表示，有键和值。列表则用方括号表示
json_dic = json_data['initialState']['entities']['answers']
# pprint.pprint(json_dic)
for i in json_dic.keys():
   content = json_dic[i]['content']
   content_1 = re.sub(r'</?\w+[^>]*>', '', content)
   name = json_dic[i]['author']['name']
   with open(title + '.txt' ,mode ='a',encoding='utf-8') as f:
       f.write(f'网友"{name}“回答：{content_1}\n  ')
   # pprint.pprint(name+':'+content)
   # 用正则简单过滤html的<>标签
   #这里使用了sub函数来滤过，是比replace更加强大的替换函数，
   print(name +':'+ content_1)