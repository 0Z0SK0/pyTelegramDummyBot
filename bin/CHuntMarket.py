from CTelegram import CTelegram
from CLog import CLog

import asyncio

class CHuntMarket():
    def start(self):
        CLog().startLogging()
        asyncio.run(CTelegram().start())

if __name__ == "__main__":
    CHuntMarket().start()