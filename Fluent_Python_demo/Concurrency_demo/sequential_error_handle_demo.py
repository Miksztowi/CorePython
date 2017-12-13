# -*- encoding:utf-8 -*-
# __author__=='Gan'

import requests
from concurrent import futures
from http import HTTPStatus
from collections import namedtuple, Counter
from tqdm import tqdm

from Fluent_Python_demo.Concurrency_demo.sequential_script_demo import save_flags, get_flag, show, main

MAX_WORKERS = 20
Result = namedtuple('Result', 'status cc')


def get_flag(base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    resp = requests.get(url)
    if resp.status_code != 200:
        resp.raise_for_status()
    return resp.content


def download_one(cc, base_url, verbose=False):
    try:
        image = get_flag(base_url, cc)
    except requests.exceptions.HTTPError as exc:
        res = exc.response
        if res.status_code == 404:
            status = HTTPStatus.NOT_FOUND
            msg = 'not found'
        else:
            raise

    else:
        save_flags(image, cc.lower() + '.gif')
        status = HTTPStatus.OK
        msg = 'OK'

    if verbose:
        print(cc, msg)

    return Result(status, cc)


def download_many(cc_list, base_url, verbose, max_req):
    counter = Counter()
    cc_iter = sorted(cc_list)
    if not verbose:
        cc_iter = tqdm(cc_iter)
    for cc in cc_iter:
        try:
            res = download_one(cc, base_url, verbose)
        except requests.exceptions.HTTPError as exc:
            error_msg = 'HTTP error {res.status_code} - {res.reason}'
            error_msg = error_msg.format(res=exc.response)
        except requests.exceptions.ConnectionError as exc:
            error_msg = 'Connection error'
        else:
            error_msg = ''
            status = res.status

    if error_msg:
        status = HTTPStatus.error

    counter[status] += 1
    if verbose and error_msg:
        print('*** Error for {}: {}'.format(cc, error_msg))

    return counter


if __name__ == '__main__':
    main(download_many)