#!/usr/bin/env python3

import argparse
import asyncio
import logging
import sys

from bosch_alarm_mode2 import Panel

logging.basicConfig(stream = sys.stdout,
                    format='%(levelname)s: %(message)s',
                    level = logging.DEBUG)

async def run():
    args = dict(host='10.66.15.147', port=7700, passcode='2580')
    panel = Panel(host=args['host'], port=args['port'], passcode=args['passcode'])
    try:
        loop.create_task(panel.connect())
        panel.print()
        while True:
             await asyncio.sleep(0.1)
    except KeyboardInterrupt:
        await panel.disconnect()
        
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
asyncio.run(run())

async def unused():
    await panel._connect(panel.LOAD_ALL)
    await panel.load(panel.LOAD_ALL)
