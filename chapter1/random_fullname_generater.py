"""A script to generate random Chinese full names."""

import random

family_name_set = (
    "王", "李", "张", "刘", "陈", "杨", "黄", "赵", "吴", "周",
    "徐", "孙", "马", "朱", "胡", "郭", "何", "高", "林", "罗",
    "郑", "梁", "谢", "宋", "唐", "许", "韩", "冯", "邓", "曹"
)

first_name_set = (
    "秀英", "桂英", "秀兰", "玉兰", "婷婷", "桂兰", "玉梅", "秀珍", "海燕", "一诺",
    "欣怡", "梓涵", "梦瑶", "子轩", "子涵", "浩然", "俊杰", "宇轩", "浩宇", "博文",
    "伟", "芳", "娜", "敏", "静", "丽", "强", "磊", "军", "洋"
)

nick_name_set = (
    "小虎", "阿宝", "小强", "小芳", "小明", "小红", "小刚", "小龙", "小丽", "小杰",
    "豆豆", "妞妞", "乐乐", "阳阳", "果果", "糖糖", "石头", "铁蛋", "二狗", "狗剩",
    "大壮", "柱子", "翠花", "春花", "秋香", "冬梅", "夏雨", "春生", "建国", "建军"
)

def main():
    """Generate random Chinese full names."""
    while True:
        first_name = random.choice(first_name_set)
        family_name = random.choice(family_name_set)
        nick_name = random.choice(nick_name_set)
        full_name = family_name + first_name
        print(f"\n\n随机生成的姓名是: \033[91m{full_name}\033[0m, 小名: {nick_name}\n\n")
        _continue = input("是否继续生成?(y/n)").lower() == "y"
        if not _continue:
            print("\n感谢您的使用, 再见!")
            break

if __name__ == "__main__":
    main()
