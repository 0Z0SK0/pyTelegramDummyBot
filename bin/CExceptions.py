from CLog import CLog

class _FunctionNotFound(Exception):
    CLog().Log(f"Exception occured: {Exception}")
    pass

class _CommandNotFound(Exception):
    CLog().Log(f"Exception occured: {Exception}")
    pass