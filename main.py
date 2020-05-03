import os

# 输入命令，转换成列表
while True:
    order = input(">")
    order_list = order.split()
    if order_list[0] == 'config':
        if order_list[1] == 'first':
            os.system("python3 scripts/first_run.py")
    elif order_list[0] == 'sub':
        pass
    elif order_list[0] == 'control':
        if order_list[1] == 'exit':
            break
    elif order_list[0] == 'test':
        if order_list[1] == 'speed':
            os.system("python3 scripts/speed_test.py")
    elif order_list[0] == 'update':
        pass
    else:
        print("请输入正确的指令，详见readme.md")