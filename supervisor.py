# -*- encoding: utf-8 -*-
import logging
import wmi
import os
import time

CONFIGFILE = 'config.ini'
# 读取配置文件中的进程名和系统路径，这2个参数都可以在配置文件中修改
ProList = []
# 定义一个列表
c = wmi.WMI()
# 要监控的程序的名字
code_name = 'test.py'
# 要监控的程序的路径
code_path = r'D:\zmg\lbjr\test.py'

def main():
    for process in c.Win32_Process():
        ProList.append(str(process.Name))
    # 把所有任务管理器中的进程名添加到列表

    if code_name in ProList:
        # 判断进程名是否在列表中，如果是True，则所监控的服务正在 运行状态，
        # 打印服务正常运行
        print('')
        print("Server is running...")
        print('')
    else:
        # 如果进程名不在列表中，即监控的服务挂了，则在log文件下记录日志
        # 日志文件名是以年月日为文件名

        f = open('.\\log\\' + time.strftime("%Y%m%d", time.localtime()) + '-exception.txt', 'a')
        print('Server is not running,Begining to Restart Server...')
        # 打印服务状态
        f.write('\n' + 'Server is not running,Begining to Restart Server...' + '\n')
        f.write(time.strftime('%Y-%m-%d %H:%M:%S --%A--%c', time.localtime()) + '\n')
        # 写入时间和服务状态到日志文件中
        os.startfile(code_path)
        # 调用服务重启
        f.write('Restart Server Success...' + '\n')
        f.write(time.strftime('%Y-%m-%d %H:%M:%S --%A--%c', time.localtime()))
        f.close()
        # 关闭文件
        print('Restart Server Success...')
        print(time.strftime('%Y-%m-%d %H:%M:%S --%A--%c', time.localtime()))
    del ProList[:]


# 清空列表，否则列表会不停的添加进程名，会占用系统资源

if __name__ == "__main__":
    while True:
        main()
        time.sleep(10)
        # 每隔10秒调用脚本看下服务是否正常，如果不正常则重启服务，如果正常，则打印服务正常