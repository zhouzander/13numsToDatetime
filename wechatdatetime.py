'''
This is a tool to convert unix millisecond stamp
into normal date and time in the filename created
by Wechat.
Author: Zander <zhou7905@mail.ustc.edu.cn>
Procotol: GPL v3
'''
import datetime
import os

def stamptoString(stamp):
    time = datetime.datetime.fromtimestamp(stamp)
    return(time.strftime("%Y%m%d_%H%M%S"))

def wechattoUnix(wcstamp):
    if not wcstamp.isdigit():
        return(0)
    else:
        if len(wcstamp) != 13:
            return(0)
        else:
            return(int(wcstamp[0:10]))

def wecharttoTime(wcstamp):
    unix = wechattoUnix(wcstamp)
    if unix != 0:
        time = stamptoString(unix)
        return(str(time)+"_"+wcstamp[10:13])
    else:
        return("WrongDatetime")

if __name__ == "__main__":
    files = os.listdir('.')
    for f in files:
        rename = 0
        if "mmexport" in f:
            lenth = len(f)
            newname = "mmexdate" + wecharttoTime(f[8:21]) + f[21:lenth]
            print(f)
            print(newname)
            rename = 1
        if "microMsg." in f:
            lenth = len(f)
            newname = "microMsg-" + wecharttoTime(f[9:22]) + f[22:lenth]
            print(f)
            print(newname)
            rename = 1
        
        if "wx_camera_" in f:
            lenth = len(f)
            newname = "wx_camera-" + wecharttoTime(f[10:23]) + f[23:lenth]
            print(f)
            print(newname)
            rename = 1        
        parts = f.split('.')
        if parts[0].isdigit() and len(parts[0])==13:
            lenth = len(f)
            newname = wecharttoTime(parts[0]) + f[13:lenth]
            print(f)
            print(newname)
            rename = 1
        if rename == 1:
            os.rename(f, newname)
    #print(stamptoString(1481021615))
    #print(stamptoString(wechattoUnix("1481021600371")))
    #print(wecharttoTime("1481021600371"))
