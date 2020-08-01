import os
from tqdm import tqdm

def rename(path):
    for item in tqdm(os.listdir(path)):
        newname = item.zfill(8) #位数
        os.rename(path+item,path+newname)
        pass


if __name__ == '__main__':
    path = input("please input your path")
    rename(path)