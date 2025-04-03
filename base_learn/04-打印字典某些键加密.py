import base64
import copy
import json


# 示例加密函数：用SHA-256哈希值替换原值
def encrypt_value(value):
    if isinstance(value, str):  # 确保处理字符串类型
        return base64.b64encode(value.encode()).decode()
    elif isinstance(value, dict) or isinstance(value, list):
        return base64.b64encode(json.dumps(value).encode()).decode()
    return value  # 非字符串类型保持不变（或根据需求处理）

def encrypt_dict_values(original_dict, keys_to_encrypt):
    """
    对字典中的指定键进行加密，返回一个新字典。
    
    :param original_dict: 原始字典
    :param keys_to_encrypt: 需要加密的键列表
    :return: 加密后的新字典
    """
    # 创建深拷贝副本（避免嵌套字典被影响）
    copied_dict = copy.deepcopy(original_dict)

    # 对副本中的指定键进行加密
    for key in keys_to_encrypt:
        if key in copied_dict:
            copied_dict[key] = encrypt_value(copied_dict[key])

    return copied_dict

if __name__ == "__main__":
    # 原始字典（后续还要用，不能修改）
    original_dict = {
        "name": "Alice",
        "password": "my_secret",
        "email": "alice@example.com",
        "details": {"age": 30, "address": "123 Street"}
    }

    # 需要加密的键列表
    keys_to_encrypt = ["password", "email"]

    copied_dict = encrypt_dict_values(original_dict, keys_to_encrypt)

    # 打印处理后的副本
    print("加密后的字典：", copied_dict)

    # 验证原字典未被修改
    print("\n原始字典未被改变：", original_dict)