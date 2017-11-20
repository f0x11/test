# -*- coding: utf-8 -*-
import os
import time

__author__ = 'f0x11'

CHECK_INTERVAL = 2  # 单位：秒


def daemon_monitor(cmd, cmd_key, interval=CHECK_INTERVAL):
    """
    用ps命令检查进程是否存在。
    :param cmd: 启动命令
    :param cmd_key: ps 检查关键字
    :param interval: 检查间隔
    :return:
    """
    if not cmd or not cmd_key:
        return

    while 1:
        ret_lines = os.popen('ps axu|grep ' + cmd_key).readlines()
        print ret_lines
        for li in ret_lines:
            if li.find('grep') < 0:
                print 'running'
                break
        else:
            print 'end'
            os.system(cmd)  # 仍然是child，放弃此种方法。

        time.sleep(interval)


if __name__ == '__main__':
    command = "python ../views/main.py"
    command_key = "../view"
    daemon_monitor(command, command_key)