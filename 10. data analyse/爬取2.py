import requests
import pandas as pd
import time

template = 'https://www.zhihu.com/api/v4/questions/30644408/feeds?cursor=1c4cacd45e70f24bd620bad51c605d59&include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,attachment,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,is_labeled,paid_info,paid_info_content,reaction_instruction,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[*].mark_infos[*].url;data[*].author.follower_count,vip_info,badge[*].topics;data[*].settings.table_of_content.enabled&limit=5&{offset}&order=default&platform=desktop&session_id=1698132896804376037'

df = pd.DataFrame()
# df有三列，answer_id和content以及创建日期
df['answer_id'] = []
df['content'] = []
df['created_time'] = []

answer_ids = []

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

cookies = { 
# 填自己的z_0 cookie
    
}
# 第一条使用模版，后面的都是next来获取
url0 = template.format(offset=0)
resp0 = requests.get(url0, headers=headers,cookies=cookies)
for data in resp0.json()['data']:
        answer_id = data['target']['id']
        # 添加answer_id到df中
        answer_ids.append(answer_id)
next = resp0.json()['paging']['next']

for page in range(1,400):# 这里自己估算一下，每页是5条数据
    #对第page页进行访问
    resp = requests.get(next, headers=headers,cookies=cookies)
    print('正在爬取第' + str(page) + '页')
    
    for data in resp.json()['data']:
        answer_id = data['target']['id']
        # 添加answer_id到df中
        answer_ids.append(answer_id)
    next = resp.json()['paging']['next']
    time.sleep(3) # 这里是情况可快可慢
    
# 将answer_ids写入df
df['answer_id'] = answer_ids
df.to_csv('answer_id.csv', index=True)


from bs4 import BeautifulSoup
import pandas as pd
import random

contents = []

batch = 0
for answer_id in answer_ids:
    print('正在爬取answer_id为{answer_id}的数据'.format(answer_id=answer_id))
    url = 'https://www.zhihu.com/question/30644408/answer/{answer_id}'.format(answer_id=answer_id)
    try:
        resp = requests.get(url, headers=headers, cookies=cookies)
        soup = BeautifulSoup(resp.text, 'html.parser')
        # 查找content
        content = soup.find('div', class_='RichContent-inner').text
        contents.append(content)
        print(content)
    except Exception as e:
        print(f'爬取answer_id为{answer_id}的数据时出现异常：{e}')
        break
    
    time.sleep(random.randint(1,4))

    # 每爬取100个回答就保存一次数据,保存在不同的文件中
    
    if len(contents) % 100 == 0:
        new_data = {'answer_id': answer_ids[:len(contents)], 'content': contents}
        new_df = pd.DataFrame(new_data)
        new_df.to_csv(f'text_{batch}.csv', index=True)
        batch += 1

# new_data = {'answer_id': answer_ids[:len(contents)], 'content': contents}
# new_df = new_df.append(pd.DataFrame(new_data))
# new_df.to_csv('text1.csv', index=True)


