#!/usr/bin/env bash

export PATH=$PATH:/usr/bin

cd ~/bilipy/bilipy/
python3 -m scrapy crawl bilibili >> ~/bilipy/crawl.log 2>&1
cd ~/bilipy/bilipy/yuntuFlask/
python3 bili_api.py >>  ~/bilipy/bilipy/yuntuFlask/log 2>&1
