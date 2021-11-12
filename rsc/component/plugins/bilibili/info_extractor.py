import requests
import json
from difflib import SequenceMatcher
from .bilibili_config import config

def string_similarity(s1:str, s2:str):
    return SequenceMatcher(None, s1, s2).quick_ratio()

def find_best_match(ls:list, dst:str)->str:
    best_ratio = 0
    best_str = ''
    for s in ls:
        ratio = string_similarity(s, dst)
        if ratio > best_ratio:
            best_ratio = ratio
            best_str = s
        if ratio == 1.0:
            break
    return best_str



sess = config['SESSDATA']
uid = config['uid']
# 认证方式
hd = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Referer' : 'https://t.bilibili.com/',
    'Accept' : 'application/json, text/plain, */*',
    'Cookie': f'{sess}'
}

# 根据关键字搜索用户(@时的填充列表)
# http://api.vc.bilibili.com/dynamic_mix/v1/dynamic_mix/at_search
# 请求方式：GET
# 认证方式：Cookie（SESSDATA）
async def get_usr_info(usrname: str):

    url = f'https://api.vc.bilibili.com/dynamic_mix/v1/dynamic_mix/at_search?uid={uid}&keyword={usrname}'

    try:
        r = requests.request('GET', url=url, headers=hd)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        result = json.loads(r.text)
        all = [j for i in result['data']['groups'] for j in i['items']]

        if len(all) == 0:
            return ' 不存在相似的用户 '

        all_usrname = [i['uname'] for i in all]
        best_match_usr_name = find_best_match(all_usrname, usrname)
        index = all_usrname.index(best_match_usr_name)

        # 返回uname与usrname相似度最高的用户信息
        return all[index]
        
    except:
        return f' 查询失败, StatusCode={r.status_code} '


# 用户空间详细信息
# http://api.bilibili.com/x/space/acc/info
# 请求方式：GET
# 认证方式：Cookie(SESSDATA)
async def get_particular_info(uid:str):

    url = f'http://api.bilibili.com/x/space/acc/info?mid={uid}'

    try:
        r = requests.request('GET', url=url, headers=hd)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        result = json.loads(r.text)

    # 返回值形如：
    # h: -{
    #     birthday: "09-19",
    #     coins: 0,
    #     face: +"http://i1.hdslb.com/bfs/face/ef0457addb24141e15dfac6fbf45293ccf1e32ab. ...",
    #     fans_badge: true,
    #     fans_medal: +{3 items},
    #     is_followed: false,
    #     jointime: 0,
    #     level: 6,
    #     live_room: +{9 items},
    #     mid: 2,
    #     moral: 0,
    #     name: "碧诗",
    #     nameplate: +{6 items},
    #     official: +{4 items},
    #     pendant: +{6 items},
    #     profession: +{1 items},
    #     rank: 20000,
    #     school: +{1 items},
    #     series: +{2 items},
    #     sex: "男",
    #     sign: "kami.im 直男过气网红 # av362830 “We Are Star Dust”",
    #     silence: 0,
    #     sys_notice: {},
    #     tags: null,
    #     theme: {},
    #     top_photo: +"http://i1.hdslb.com/bfs/space/cb1c3ef50e22b6096fde67febe863494caefebad ...",
    #     user_honour_info: +{3 items},
    #     vip: +{10 items}
    # }
        return result['data']

    except:
        return f' 查询失败, StatusCode={r.status_code} '


#根据uid搜索用户直播间状态
async def get_liveroom_status(uid:str):
    usr_info = await get_particular_info(uid)
    return usr_info['live_room']