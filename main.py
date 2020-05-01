# 输入命令，转换成列表
while True:
    order = input(">")
    order_list = order.split()
    # 当输入control exit时，终止程序
    if order_list[0]=='control' and order_list[1]=='exit':
        break
