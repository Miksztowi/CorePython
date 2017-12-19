# -*- encoding:utf-8 -*-
# __author__=='Gan'
import asyncio
import collections
from http import HTTPStatus
import time
import os
from collections import namedtuple

import aiohttp
from aiohttp import web
import tqdm

DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000
POP20_CC = ('CN IN US ID BR PK NG BD RU JP'
            'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'http://flupy.org/data/flags'

DEST_DIR = 'downloads/'

Result = namedtuple('Result', 'status cc')


def save_flags(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


class FetchError(Exception):
    def __init__(self, country_code):
        self.country_code = country_code


@asyncio.coroutine
def get_flag(base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    session = aiohttp.ClientSession()
    resp = yield from session.get(url)
    if resp.status == 200:
        image = yield from resp.read()
        return image
    elif resp.status == 404:
        return web.HTTPNotFound()
    else:
        raise aiohttp.http.HttpProcessingError(
            code=resp.status, message=resp.reason, headers=resp.headers
        )


@asyncio.coroutine
def download_one(cc, base_url, semaphore, verbose):
    try:
        with (yield from semaphore):
            image = yield from get_flag(base_url, cc)
    except web.HTTPNotFound:
        status = HTTPStatus.NOT_FOUND
        msg = 'not found'
    except Exception as exc:
        raise FetchError(cc) from exc
    else:
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, save_flags, image, cc.lower() + '.gif') # Avoiding blocking.
        status = HTTPStatus.OK
        msg = 'OK'

    if verbose and msg:
        print(cc, msg)

    return Result(status, cc)


@asyncio.coroutine
def downlaoder_coro(cc_list, base_url, verbose, concur_req):
    counter = collections.Counter()
    semaphore = asyncio.Semaphore(concur_req)
    to_do = [download_one(cc, base_url, semaphore, verbose)
             for cc in sorted(cc_list)]
    to_do_iter = asyncio.as_completed(to_do)
    if not verbose:
        to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list))
    for future in to_do_iter:
        try:
            res = yield from future
        except FetchError as exc:
            country_code = exc.country_code
            try:
                error_msg = exc.__cause__.args[0]
            except IndexError:
                error_msg = exc.__cause__.__class__.__name__
            if verbose and error_msg:
                msg = '*** Error for {} {}'
                print(msg.format(country_code, error_msg))
            status = HTTPStatus.NOT_FOUND
        else:
            status = res.status
        counter[status] += 1

    return counter


def download_many(cc_list, base_url, verbose, concur_req):
    loop = asyncio.get_event_loop()
    coro = downlaoder_coro(cc_list, base_url, verbose, concur_req)
    counts = loop.run_until_complete(coro)
    loop.close()

    return counts


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC, base_url=BASE_URL, verbose=None, concur_req=DEFAULT_CONCUR_REQ)
    elapsed = time.time() - t0
    msg = '\n{} flags download in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main(download_many)
