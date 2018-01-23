# -*- encoding:utf-8 -*-
# __author__=='Gan'

import os
import asyncio
import gzip


import aiohttp

class pdb:
    def __init__(self):
        self.ids = []
        self.dl_id = []
        self.err_id = []

    async def download_file(self, session, url):
        try:
            async with session.get(url) as remotefile:
                if remotefile.status == 200:
                    data = await remotefile.read()
                    return {"error": "", "data": data}
                else:
                    return {"error": remotefile.status, "data": ""}
        except Exception as e:
            print(e)
            return {"error": e, "data": ""}

    async def unzip(self, session, work_queue):
        while not work_queue.empty():
            queue_url = await work_queue.get()
            print(queue_url)
            data = await self.download_file(session, queue_url)
            print(data)
            id = queue_url[-11:-7]
            ID = id.upper()
            if not data["error"]:
                saved_pdb = os.path.join("./pdb", ID, '{ID}.pdb')
                if ID not in self.dl_id:
                    self.dl_id.append(ID)
                with open("{id}.ent.gz", 'wb') as f:
                    f.write(data["data"].read())
                with gzip.open("{id}.ent.gz", "rb") as inFile, open(saved_pdb, "wb") as outFile:
                    shutil.copyfileobj(inFile, outFile)
                os.remove("{id}.ent.gz")
            else:
                self.err_id.append(ID)

    def download_queue(self, urls):
        loop = asyncio.get_event_loop()
        q = asyncio.Queue(loop=loop)
        [q.put_nowait(url) for url in urls]
        con = aiohttp.TCPConnector(limit=10)
        with aiohttp.ClientSession(loop=loop, connector=con) as session:
            tasks = [asyncio.ensure_future(self.unzip(session, q)) for _ in range(len(urls))]
            wait = asyncio.wait(tasks, timeout=10)
            done, unfinished = loop.run_until_complete(wait)
        loop.close()


if __name__ == "__main__":
    x = pdb()
    urls = ['ftp://ftp.wwpdb.org/pub/pdb/data/structures/divided/pdb/nf/pdb4nfn.ent.gz', 'ftp://ftp.wwpdb.org/pub/pdb/data/structures/divided/pdb/ny/pdb4nyj.ent.gz', 'ftp://ftp.wwpdb.org/pub/pdb/data/structures/divided/pdb/mn/pdb2mnz.ent.gz', 'ftp://ftp.wwpdb.org/pub/pdb/data/structures/divided/pdb/ra/pdb4ra4.ent.gz', 'ftp://ftp.wwpdb.org/pub/pdb/data/structures/divided/pdb/x5/pdb4x5w.ent.gz', 'ftp://ftp.wwpdb.org/pub/pdb/data/structures/divided/pdb/dm/pdb2dmq.ent.gz', 'ftp://ftp.wwpdb.org/pub/pdb/data/structures/divided/pdb/n7/pdb2n7r.ent.gz', 'ftp://ftp.wwpdb.org/pub/pdb/data/structures/divided/pdb/om/pdb2omv.ent.gz', 'ftp://ftp.wwpdb.org/pub/pdb/data/structures/divided/pdb/oy/pdb3oy8.ent.gz', 'ftp://ftp.wwpdb.org/pub/pdb/data/structures/divided/pdb/fe/pdb3fej.ent.gz', 'ftp://ftp.wwpdb.org/pub/pdb/data/structures/divided/pdb/hw/pdb2hw9.ent.gz']
    x.download_queue(urls)