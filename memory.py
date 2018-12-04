import psutil

def memory():
    '''
    Measure memory usage; modified from:
    https://stackoverflow.com/questions/938733/total-memory-used-by-python-process
    '''
    #w = WMI('.')
    #result = w.query("SELECT WorkingSet FROM Win32_PerfRawData_PerfProc_Process WHERE IDProcess=%d" % os.getpid())
    result = psutil.virtual_memory()[3]
    
    return result#int(result[0].WorkingSet)
