# -*- encoding:utf-8 -*-
# __author__=='Gan'

from concurrent import futures

from Fluent_Python_demo.Concurrency_demo.sequential_script_demo import save_flags, get_flag, show, main

MAX_WORKERS = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flags(image, cc.lower() + '.gif')
    return cc


# def download_many(cc_list):
#     workers = min(MAX_WORKERS, len(cc_list))
#     with futures.ThreadPoolExecutor(workers) as executor:
#         res = executor.map(download_one, sorted(cc_list))
#
#     return len(list(res))  # 如果任意一个线程的发生了异常，由于隐式调用了next()方法得到返回值，所以异常会在这里被抛出。


def download_many(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        # for future in to_do:
        #     res = future.result()
        #     msg = '{} result: {!r}'
        #     print(msg.format(future, res))
        #     results.append(res)  # Different from the below.
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)


if __name__ == '__main__':
    main(download_many)
