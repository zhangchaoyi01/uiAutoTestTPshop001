import json


def read_json(filename):
    filepath = "./data/" + filename
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


def get_data():
    # 新建空列表
    lists = []
    datas = read_json("login.json")
    for data in datas.values():
        # 注意：添加到一个元组内（）
        lists.append((data["username"],
                     data["password"],
                     data["verify_code"],
                     data["expect_result"],
                     data["success"]))
    # 注意：必须在for循环外return返回
    # print(lists)
    return lists

# if __name__ == '__main__':
#     get_data()

