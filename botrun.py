#!/bin/env python3.6

import subprocess
import asyncio

while(True):
    subprocess.call('python3.8 discordbot.py', shell=True)
    asyncio.sleep(10)
