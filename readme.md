# EasyPasswall
本程序正处于开发阶段，暂不可用。  
` 用于在Linux中终端（命令行）代理SS，SSR，V2ray，Trojan等协议的代理，支持订阅链接。 `

## Requirements:
- x86_64 Linux
- Python 3

## Usage:  
` python3 easypasswall.py --<main-action>-<addtional-action> `  
首次使用前，需要执行：` python3 easypasswall.py --config-first `来配置。

## main-actions:
- config   
  配置EasyPasswall
- control  
  控制代理  
- test  
  测试（速度等等）   
  
## addtional-adtions:
- control:  
 start  
 开始代理  
 stop    
 停止代理  
 restart    
 重启代理  
  