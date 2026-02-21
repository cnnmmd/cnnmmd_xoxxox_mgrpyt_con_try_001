#---------------------------------------------------------------------------

import time
import asyncio
from xoxxox.shared import PrcFlw
from xoxxox.midclt import MidClt

#---------------------------------------------------------------------------

dicsrv = PrcFlw.dicsrv()
adrmid = dicsrv["xoxxox_appmid_loc"]

#---------------------------------------------------------------------------
# 文字列を切断し、連結する（xyz -> x, yz -> xyz）

time.sleep(2)
async def catstr(strarg):
  datres = await MidClt.reqprc({}, adrmid + MidClt.adrini)
  datres = await MidClt.reqset(strarg, adrmid + MidClt.adrset)
  datcar = await MidClt.reqprc({"keymmd": datres["keymmd"], "keyprc": "xoxxox.OpeStr.strcar"}, adrmid + MidClt.adrprc)
  datcdr = await MidClt.reqprc({"keymmd": datres["keymmd"], "keyprc": "xoxxox.OpeStr.strcdr"}, adrmid + MidClt.adrprc)
  datcat = await MidClt.reqprc({"keymmd": datcar["keymmd"], "keycdr": datcdr["keymmd"], "keyprc": "xoxxox.OpeStr.strcat"}, adrmid + MidClt.adrprc)
  datres = await MidClt.reqget({"keymmd": datcat["keymmd"]}, adrmid + MidClt.adrget)
  return datres

strreq = "xyz"
datres = asyncio.run(catstr(strreq))
print(datres.decode("utf-8"))
