# 13numsToDatetime
A tool to convert unix millisecond stamp into normal date and time in the filename created by Wechat.

# wechatdatetime.py的功能
把微信生成的图像或视频文件名中的毫秒级时间戳转换为普通的年月日时分秒。
目前支持4种变换：
1. mmexport[毫秒级时间戳].* 转换为 mmexdate[年月日_时分秒_毫秒].*
2. microMsg.[毫秒级时间戳].* 转换为 microMsg-[年月日_时分秒_毫秒].*
3. wx_camera_[毫秒级时间戳].* 转换为 wx_camera-[年月日_时分秒_毫秒].*
4. [毫秒级时间戳].* 转换为 [年月日_时分秒_毫秒].*
作者：Zander
代码分发协议：GPL v3

# Windows下的使用方法
1. 访问 https://www.python.org/getit/ 下载安装最新版的python。
2. 把wechatdatetime.py 文件和要该名的图像或视频文件放到同一个目录下。
3. 右键单击wechatdatetime.py 文件，选择"Edit with IDLE -> Edit with IDLE x.x".
4. 在弹出的窗口的菜单栏中选择"Run -> Run Module"，或者直接按F5键。

# Linux下的使用方法
1. 把wechatdatetime.py 文件和要该名的图像或视频文件放到同一个目录下。
2. 右键单击"在终端打开"。
3. 在弹出的终端窗口中执行"python wechatdatetime.py"。
