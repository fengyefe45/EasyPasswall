import os

def ping_baidu():
    os.system("timeout 15 ping baidu.com | tee tmp/ping_baidu.log")

def ping_google():
    os.system("timeout 15 ping google.com | tee tmp/ping_google.log")