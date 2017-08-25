#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date: 2017/3/1
# author: he.zhiming

from __future__ import absolute_import, unicode_literals
import time
import random
from datetime import datetime
from datetime import timedelta
# 我们的调度器( 以Tornado为蓝本 ), 另外 APScheduler提供了集中调度器( 其实都大同小异 )
from apscheduler.schedulers.tornado import TornadoScheduler
# 我们的触发器(触发规则)
from apscheduler.triggers.interval import IntervalTrigger
import tornado.ioloop

# 这里忽略, 我个人习惯使用日志来代替print, 另外不太习惯于使用 pdb 单步调试
import logging

LOG_FMT = "%(levelname)s %(asctime)s  %(processName)s %(threadName)s %(filename)s:%(lineno)s:%(funcName)s [%(message)s]"
logging.basicConfig(format=LOG_FMT, level=logging.DEBUG)
mylogger = logging.getLogger(__name__)
mylogger.setLevel(logging.DEBUG)


# 要做一件什么事情( 可以替换为你需要做的其他任何事情 )
def testfunc(a, b, c):
    print('DOING: %s' % locals())


if __name__ == '__main__':
    # OK, 调度器有了
    sched = TornadoScheduler()
    for _ in range(30):
        # 往调度器里面喂 Job 了
        sched.add_job(
            func=testfunc,  # 被调度的函数
            args=(1, 2, 3),  # 被调度函数所需要的参数

            trigger=IntervalTrigger(  # 触发规则, 推荐这种我个人总结的写法, 不要用官方示例的那种
                # 开始时间
                start_date=datetime.now() + timedelta(seconds=random.randint(1, 5)),
                # 结束时间
                end_date=datetime.now() + timedelta(seconds=random.randint(5, 10)),
                # 每隔多少时间
                seconds=random.randint(1, 5)
            ),

            name='testfunc',  # 这个 Job, 起个别名
        )

    # 调度器启动
    sched.start()

    # Tornado开启 IOLoop, 本例中我们也是使用 TornadoScheduler
    # 其实官方还提供了各种各样的调度器
    # 但是都大同小异, 只要掌握了套路, 便可不变因万变
    try:
        tornado.ioloop.IOLoop.current().start()
    except (KeyboardInterrupt, SystemExit) as e:
        sched.shutdown()