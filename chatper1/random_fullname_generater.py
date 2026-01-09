# 定义一个姓的元组

# 定义一个名的元组

# 循环
# 随机取一个姓
# 随机取一个名
# 组合成一个全名
# 打印全名
# 询问用户继续还是退出

import sys,random

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

while True:
    first_name = random.choice(first_name_set)
    family_name = random.choice(family_name_set)
    full_name = family_name +first_name
    print(f"\n\n随机生成的姓名是: {full_name}\n\n", file = sys.stderr)
    _continue = True if input("是否继续生成?(y/n)") == "y" else False
    if _continue == False:
        print(f"\n感谢您的使用, 再见!")
        break


