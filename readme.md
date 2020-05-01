# EasyPasswall
本程序正处于开发阶段，暂不可用。  
` 用于在Linux中终端（命令行）代理SS，SSR，V2ray，Trojan等协议的代理，支持订阅链接。 `

## Requirements:
- x86_64 Linux
- Python 3

## Usage:  
首先输入` ./easypasswall.sh  `进入EasyPasswall程序。   
接着，会出现` > ` ，控制需要输入` <main-action> `和` <additional-action> `两个参数。
举例：` control start `开始代理。   
首次使用前，需要执行：`chmod +x easypasswall.sh `来给予EasyPasswall脚本可执行权限。  
初次进入EasyPasswall程序，需要执行` config first `来初始化。

## main-actions:
- config   
  配置EasyPasswall
- control  
  控制代理  
- test  
  测试（速度等等）   
  
## additional-adtions:
- control:  
 start  
 开始代理  
 stop    
 停止代理  
 restart    
 重启代理  
  