# -*- encoding:utf-8 -*-
# __author__=='Gan'

import asyncio
import aiohttp
import time
import os
import sys

POP20_CC = ('CN IN US ID BR PK NG BD RU JP'
            'MX PH VN ET EG DE IR TR CD FR').split()
BASE_URL = 'http://flupy.org/data/flags'

DEST_DIR = 'downloads/'


def save_flags(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


@asyncio.coroutine
def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    session = aiohttp.ClientSession()
    res = yield from session.get(url)
    # res = yield from aiohttp.request('GET', url) will occur error with 'Unclosed client session'.
    image = yield from res.read()
    session.close()
    return image


@asyncio.coroutine
def download_one(cc):
    image = yield from get_flag(cc)
    show(cc)
    save_flags(image, cc.lower() + '.gif')
    return cc


# @asyncio.coroutine
def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()

    return len(res)


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags download in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main(download_many)
