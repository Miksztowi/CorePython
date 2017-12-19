# -*- encoding:utf-8 -*-
# __author__=='Gan'

import asyncio


def stage1(response1):
    request2 = step1(response1)
    api_call2(request2, stage2)

def stage2(response2):
    request3 = step2(response2)
    api_call3(request3, stage3)

def stage3(response3):
    step(response3)

api_call(request1, stage1)


@asyncio.coroutine
def three_stages(request1):
    response1 = yield from api_call1(request1)

    request2 = step1(response1)
    response2 = yield from api_call2(request2)

    request3 = step2(response2)
    response3 = yield from api_call3(request3)

    step3(request3)


