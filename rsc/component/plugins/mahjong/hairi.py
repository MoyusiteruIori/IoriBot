import os

helper_path = r'D:\projects\python\IoriBot\mahjong-helper.exe'

def hairi(tehai:str)->str:
    command = f'{helper_path} {tehai}'
    result = os.popen(command, 'r', 1024)
    return result.buffer.read().decode(encoding='utf-8')[31:-1]