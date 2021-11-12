import requests
from config import IMAGE_LOCAL_BUFF

class GetPic:
    def __init__(self, pic_name:str = 'tmp.jpg') -> None:
        self.session = requests.session()
        self.picname = pic_name

    async def get_pic(self, url="https://iw233.cn/API/ghs.php", buffer=IMAGE_LOCAL_BUFF):
        res = self.session.get(url)
        with open(buffer, 'wb') as f:
            f.write(res.content)
        return True
