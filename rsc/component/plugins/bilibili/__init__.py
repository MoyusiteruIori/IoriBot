from config import IMAGE_LOCAL_BUFF
from aiocqhttp.message import MessageSegment
from nonebot import on_command, on_startup, CommandSession
import nonebot
from .info_extractor import *
from ..eropic.pic_info import GetPic
from aiocqhttp.exceptions import Error as CQHttpError
from .bilibili_config import sub_liver, liver_pre_status


pic_getter = GetPic()

@on_startup
async def init_liver_status():
    for liver_uid in sub_liver:
        live_room_info = await get_liveroom_status(liver_uid)
        liver_pre_status[liver_uid] = live_room_info['liveStatus']


@on_command("SearchUser", aliases=('查询用户','查找用户','搜索用户'))
async def usrsearch(session:CommandSession):
    usrname = session.current_arg_text.strip()
    if not usrname:
        usrname = (await session.aget(prompt='你想查询的bilibili用户的用户名是？')).strip()
    while not usrname:
        usrname = (await session.aget(prompt='要查询的用户名不能为空哦')).strip()

    usr = await get_usr_info(usrname)
    if isinstance(usr, dict):
        face, uname, uid, fans = usr['face'], usr['uname'], usr['uid'], usr['fans']
        await pic_getter.get_pic(face)
        image_seq = MessageSegment.image('file:///{}'.format(IMAGE_LOCAL_BUFF))
        info_seq  = MessageSegment.text(f'{uname}\nuid:{uid}\n粉丝数:{fans}')
        await session.send(info_seq + image_seq, at_sender=True)
    else:
        await session.send(usr)


@on_command("SearchLiveRoom", aliases=('播了吗', '查询直播间', '查找直播间', '搜索直播间'))
async def liveroom_search(session:CommandSession):
    usrname = session.current_arg_text.strip()
    if not usrname:
        usrname = (await session.aget(prompt='你想查询的直播间的主播是？')).strip()
    while not usrname:
        usrname = (await session.aget(prompt='电子宠物也要有名字喔')).strip()

    usr = await get_usr_info(usrname)
    if not (isinstance(usr, dict) and usr['uname'] == usrname):
        await session.send(f' 未找到主播 ')
    else:
        particular_info = await get_particular_info(usr['uid'])
        live_room_info  = particular_info['live_room']

        if live_room_info['roomStatus'] == 0:
            await session.send(' TA还没有直播间 ')
        else:
            live_status = '直播中' if live_room_info['liveStatus'] == 1 else '未开播'
            online      = live_room_info['online']
            title       = live_room_info['title']
            roomid      = live_room_info['roomid']
            cover       = live_room_info['cover']
            await pic_getter.get_pic(cover)

            cover_seq = MessageSegment.image('file:///{}'.format(IMAGE_LOCAL_BUFF))
            text_seq  = MessageSegment.text(f'{live_status}\n标题：{title}\n主播：{usrname}\n房间号：{roomid}\n人气：{online}\n')
            await session.send(text_seq + cover_seq, at_sender=True)



@nonebot.scheduler.scheduled_job('cron', minute='*')
async def _():

    bot = nonebot.get_bot()
    for liver_uid in sub_liver:
        live_room_info = await get_liveroom_status(liver_uid)
        cur_sta, pre_sta = live_room_info['liveStatus'], liver_pre_status[liver_uid]
        if cur_sta != pre_sta:
            try:
                liver_pre_status[liver_uid] = live_room_info['liveStatus']
                status = '开播啦' if cur_sta == 1 else '下播啦'
                await bot.send_private_msg(user_id=1037655483, message=f'现在{sub_liver[liver_uid]}{status}')
            except CQHttpError:
                pass
