import random

def find_murderer(suspects:list = ['yz', 'ys', 'slx', 'mlhh', 'yqy', 'm11'])->str:
    random.seed = None
    murderer = random.choice(suspects)
    return murderer