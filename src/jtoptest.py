from jtop import jtop
from Logs import Logs
import time

if __name__ == "__main__":
    logs = Logs('jtop', '../')
    str = "All accessible jtop properties"
    logs.info(str)
    with jtop() as jetson:
        # boards
        str = '*** board ***'
        logs.info(str)
        logs.info(jetson.board)
        # jetson.ok() will provide the proper update frequency
        while jetson.ok():
            try:
                # CPU
                str = '*** CPUs ***'
                logs.info(str)
                logs.info(jetson.cpu)
            except Exception as e:
                logs.error(e)
            try:
                # CPU
                str = '*** Memory ***'
                logs.info(str)
                logs.info(jetson.memory)
            except Exception as e:
                logs.error(e)
            try:                
                # GPU
                str = '*** GPU ***'
                logs.info(str)
                logs.info(jetson.gpu)
            except Exception as e:
                logs.error(e)
            try:
                # Engines
                str = '*** engine ***'
                logs.info(str)
                logs.info(jetson.engine)
            except Exception as e:
                logs.error(e)
            try:    
                # nvpmodel
                str = '*** NV Power Model ***'
                logs.info(str)
                logs.info(jetson.nvpmodel)
            except Exception as e:
                logs.error(e)
            try:    
                # jetson_clocks
                str = '*** jetson_clocks ***'
                logs.info(str)
                logs.info(jetson.jetson_clocks)
            except Exception as e:
                logs.error(e)    
                # Status disk
            try:
                str = '*** disk ***'
                logs.info(str)
                logs.info(jetson.disk)
            except Exception as e:
                logs.error(e)
            try:    
                # Status fans
                str = '*** fan ***'
                logs.info(str)
                logs.info(jetson.fan)
            except Exception as e:
                logs.error(e)
            try:    
                # uptime
                str = '*** uptime ***'
                logs.info(str)
                logs.info(jetson.uptime)
            except Exception as e:
                logs.error(e)
            # try:    
            #     # local interfaces
            #     str = '*** local interfaces ***'
            #     logs.info(str)
            #     logs.info(jetson.local_interfaces)
            # except Exception as e:
            #     logs.error(e)    
            try:
                # Temperature
                str = '*** temperature ***'
                logs.info(str)
                logs.info(jetson.temperature)
            except Exception as e:
                logs.error(e)    
            try:
                # Power
                str = '*** power ***'
                logs.info(str)
                logs.info(jetson.power)                
            except Exception as e:
                logs.error(e)
            time.sleep(3)
