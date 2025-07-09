import random
import string
import json
from config.config import Config

def generate_random_string(length=8):
    """生成随机字符串"""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_email():
    """生成随机邮箱"""
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "example.com"]
    return f"{generate_random_string(8)}@{random.choice(domains)}"

def generate_random_username(prefix="user"):
    """生成随机用户名"""
    return f"{prefix}_{generate_random_string(6)}"

def load_test_data():
    """加载测试数据"""
    try:
        with open(Config.TEST_DATA_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}