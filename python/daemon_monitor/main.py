# -*- coding: utf-8 -*-
import subprocess
import time

CHECK_INTERVAL = 2  # 检查间隔：s


def daemon_monitor(cmd, interval=CHECK_INTERVAL):
    """
    启动进程作为子进程，监控子进程状态
    :param cmd: 启动命令
    :param interval: 检查间隔
    :return:
    """
    if not cmd:
        return

    while 1:
        # 执行命令
        proc = subprocess.Popen(cmd, shell=True)
        while 1:
            # 获取状态
            status = subprocess.Popen.poll(proc)
            if status is None:
                print 'running'
                time.sleep(interval)
            else:
                print proc.pid, 'end'
                break


if __name__ == '__main__':
    command = "python ../views/main.py"
    daemon_monitor(command)