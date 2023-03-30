# KUSTNetLogin
适用于昆明理工大学的校园网登陆器（纯命令行）

使用python3编写，依赖为requests，可在openwrt，linux等具有python3环境下运行，适用于无线中继校园WiFi网络或登录使用。

## 代码使用
- 安装依赖：pip(或pip3） install requests -i https://pypi.tuna.tsinghua.edu.cn/simple/
- 代码运行：先将代码中的username，password替换为自己的校园网账号密码后，将python文件通过scp等命令上传到需要进行校园网认证的设备上
- 使用python（python3） NetWeb.py运行代码，显示已认证便认证成功。
