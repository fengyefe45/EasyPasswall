import os, sys

print("开始测试速度……")
os.system(f"bash {sys.path[0]}/speed_test.sh")

print("开始读取结果……")
global log_google_int
global log_baidu_int
log_baidu_int_a = open(f'{sys.path[0]}/logs/ping_baidu.log', 'r')
log_google_int_a = open(f'{sys.path[0]}/logs/ping_google.log', 'r')
log_baidu_int = log_baidu_int_a.read().strip()
log_google_int = log_google_int_a.read().strip()
log_baidu_int_a.close()
log_google_int_a.close()
global final_baidu
global final_google
if log_google_int != '':
    how_google = 0
    log_google_int = eval(log_google_int)
else:
    how_google = 1

if log_baidu_int != '':
    how_baidu = 0
    log_baidu_int = eval(log_baidu_int)
else:
    how_baidu = 1

# 速度50以内算非常快，80~50算快，130~80算慢，130以上算非常慢，没有则直接算无法连接
if how_baidu == 0:
    if 0 < log_baidu_int < 50:
        final_baidu = "非常快"
    elif log_baidu_int > 50 and log_baidu_int <= 80:
        final_baidu = "快"
    elif log_baidu_int > 80 and log_baidu_int <= 130:
        final_baidu = "慢"
    elif log_baidu_int > 130:
        final_baidu = "非常慢"
else:
    final_baidu = "无法连接"

if how_google == 0:
    if 0 < log_google_int < 50:
        final_google = "非常快"
    elif log_google_int > 50 and log_google_int <= 80:
        final_google = "快"
    elif log_google_int > 80 and log_google_int <= 130:
        final_google = "慢"
    elif log_google_int > 130:
        final_google = "非常慢"
else:
    final_google = "无法连接"

print(f"测试结束，结果：\n百度连接状态：{final_baidu}；谷歌连接状态：{final_google}")
