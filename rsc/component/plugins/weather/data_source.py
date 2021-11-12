import requests
import json

hd = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

async def get_weather_of_city(city : str)->str:
    url = fr'https://www.tianqiapi.com/free/day?appid=59698588&appsecret=LZ9FUHM4&unescape=1&city={city}'
    try:
        r = requests.request('GET', url=url, headers=hd, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        # {'cityid': '101010100', 
        # 'city': '北京', 
        # 'update_time': '13:48', 
        # 'wea': '晴', 
        # 'wea_img': 'qing', 
        # 'tem': '14', 
        # 'tem_day': '15', 
        # 'tem_night': '0', 
        # 'win': '南风', 
        # 'win_speed': '2级', 
        # 'win_meter': '9km/h', 
        # 'air': '33'}

        result = json.loads(r.text)
        wea         = result['wea']
        tem         = result['tem']
        tem_day     = result['tem_day']
        tem_night   = result['tem_night']
        win         = result['win']
        win_speed   = result['win_speed']
        win_meter   = result['win_meter']
        air         = result['air']

        # 北京
        # 11℃，晴（实时）
        # 7 ~ 16℃
        # 西北风3级, 9km/h
        # 空气质量指数：76
        return f'{city}\n{tem}℃，{wea}（实时）\n{tem_night}~{tem_day}℃\n{win}{win_speed}，{win_meter}\n空气质量指数：{air} '
    except:
        return f' 查询失败，StatusCode:{r.status_code} '