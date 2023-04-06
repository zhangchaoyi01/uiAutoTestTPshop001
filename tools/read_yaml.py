import os
import yaml

from config import BASE_PATH


# 定义函数
def read_yaml(filename):
    # BASE_PATH: D:\PycharmProjects\uiAutoTestTPshop001\
    # os.sep: 是 “\” 的意思
    # filename: 数据文件名称
    file_path = BASE_PATH + os.sep + "data" + os.sep + filename

    # 定义空列表  组装测试数据
    arr = []
    # 获取文件流
    with open(file_path, "r", encoding="utf-8") as f:
        for datas in yaml.safe_load(f).values():
            arr.append(tuple(datas.values()))

    return arr


# if __name__ == '__main__':
#     read_yaml("login.yaml")
