'''Log module, write logs day by day'''
import os
import time
import inspect
import threading


class Logs:
    def __init__(self, prex: str, dir: str = '.'):
        super(Logs, self).__init__()
        self.prex = prex
        self.savepath = os.path.join(dir, 'logs')
        if not os.path.exists(self.savepath):
            os.makedirs(self.savepath)
        self.lock = threading.Lock()

    def __write(self, cont: list):
        str, msgtype, filename, fileline = cont
        logname = '{}-{}.txt'.format(self.prex, self.__getcurr_ymd())
        logpath = os.path.join(self.savepath, logname)
        try:
            self.lock.acquire(True)
            with open(logpath, mode='a') as f:
                cont = '{} - {}[line:{}] - {}: {}\n'.format(self.__getcurr_ymdhmsms(), filename, fileline, msgtype, str)
                f.write(cont)
        finally:
            self.lock.release()

    def info(self, str):
        print(str)
        frame, filename, fileline, function_name, lines, index = inspect.getouterframes(inspect.currentframe())[1]
        threading.Thread(target=self.__write, args=([str, 'INFO', os.path.basename(filename), fileline],)).start()

    def warning(self, str):
        frame, filename, fileline, function_name, lines, index = inspect.getouterframes(inspect.currentframe())[1]
        threading.Thread(target=self.__write, args=([str, 'WARNING', os.path.basename(filename), fileline],)).start()

    def error(self, str):
        frame, filename, fileline, function_name, lines, index = inspect.getouterframes(inspect.currentframe())[1]
        threading.Thread(target=self.__write, args=([str, 'ERROR', os.path.basename(filename), fileline],)).start()

    def __getcurr_ymd(self):
        return time.strftime("%Y-%m-%d", time.localtime())

    def __getcurr_ymdhms(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def __getcurr_ymdhmsms(self):
        prex = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        suffix = int((time.time() - int(time.time())) * 1000)
        return '{},{}'.format(prex, suffix)

