# EasyPasswall
本程序正处于开发阶段，暂不可用。  
用于在Linux中终端（命令行）代理 ` SS，SSR，V2ray，Trojan`等协议的代理，支持订阅链接。 `

## Requirements:
- x86_64 Linux
- Python 3

## Usage:  
首先输入` ./easypasswall.sh  `进入EasyPasswall程序（注意：本脚本默认采用bash终端）。  
接着，会出现` > ` ，控制需要输入` <main-action> `和` <additional-action> `两个参数。
举例：` control start `开始代理。   
首次使用前，需要执行：`chmod +x easypasswall.sh `来给予EasyPasswall脚本可执行权限。  
初次进入EasyPasswall程序，需要执行` config first `来初始化。

## main-actions:
- config   
  配置EasyPasswall
- sub  
  配置有关代理的内容  
- control  
  控制代理  
- test  
  测试（速度等等）
- update  
  升级（代理核心等等）
  
## additional-adtions:
- config:  
 first  
 初始化     
 http_port  
 设置http代理端口  
 https_port  
 设置https代理端口  
 socks5_port  
 设置socks5代理端口  

- sub:  
 add    
 添加订阅链接     
 rm  
 删除订阅链接  
 update  
 更新订阅   
 
- control:  
 start  
 开始代理  
 stop  
 停止代理  
 restart  
 重启代理  
 
- test:  
 speed  
 测试访问百度和谷歌的速度  
 proxy  
 测试各种代理协议状态  

- update:  
  core  
  更新代理核心  
  
  