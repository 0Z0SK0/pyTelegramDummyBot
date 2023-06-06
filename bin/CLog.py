import time

from CConfig import CConfig

class CLog():
    def __init__(self):
        self.dir = CConfig().getLogDirectory()
        self.log = self.dir + "\\log.txt"

    def startLogging(self):
        localTime = time.localtime()
        currentTime = time.strftime("%Y.%m.%d %H:%M:%S", localTime)

        with open(self.log, "w") as logfile:
            logfile.write(f"[{currentTime}] Launched\n")
            logfile.close()

    def Log(self, text):
        localTime = time.localtime()
        currentTime = time.strftime("%Y.%m.%d %H:%M:%S", localTime)

        with open(self.log, "a") as logfile:
            logfile.write(f"[{currentTime}] {text}\n")
            logfile.close()
