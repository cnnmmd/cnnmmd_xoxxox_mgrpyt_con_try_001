#!/bin/bash

pthtop='/opt/common'
cntmid='xoxxox_appmid'
script="python ${pthtop}"/bin/xoxxox/flwpyt_con_try_001.py

docker exec ${cntmid} ${script}
