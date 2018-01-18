# coding: utf-8
# __author__=='Gan'

import asyncio
import concurrent
import os

PATH = '/Users/wukong/Downloads/WebStudent'
FILETER = ['class', 'css', 'gif', 'jpg', 'jar']
REPLACER = 'ljm'
MY_NAME = 'gbw'


async def async_replace(file_name):
    loop = asyncio.get_event_loop()
    executor = concurrent.futures.ThreadPoolExecutor(5)
    loop.set_default_executor(executor)
    loop.run_in_executor(None, replace_name, file_name)
    executor.shutdown(wait=True)


def replace_name(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        try:
            f_read = f.read()
        except UnicodeDecodeError as e:
            print(file_name, e)
        else:
            replaced_text = f_read.replace(REPLACER, MY_NAME)
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(replaced_text)


def find_all_files(path):
    if os.path.isdir(path):
        replace_files = list()
        files = os.listdir(path)
        for file in files:
            file = os.path.join(path, file)
            if REPLACER in file:
                os.rename(file, file.replace(REPLACER, MY_NAME))
                file = file.replace(REPLACER, MY_NAME)
            if os.path.isfile(file) and all(f not in file for f in FILETER):
                replace_files += file,
            elif os.path.isdir(file):
                replace_files.extend(find_all_files(file))
        return replace_files


def main():
    replace_files = find_all_files(PATH)
    print(replace_files)
    loop = asyncio.get_event_loop()
    to_do = [async_replace(file) for file in replace_files]
    wait_coro = asyncio.wait(to_do)
    finished, unfinished = loop.run_until_complete(wait_coro)
    loop.close()
    print('Job done\nFinished: {}\nUnfinished :{}'.format(len(finished), len(unfinished)))


if __name__ == '__main__':
    main()
