# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 14:01:17 2016

@author: liudiwei
"""
import os
import logging  

class LogClient(object):
    def __init__(self):
        self.logger = None

    """#EXAMPLE 
    logger = createLogger('mylogger', 'temp/logger.log')
    logger.debug('logger debug message')  
    logger.info('logger info message')  
    logger.warning('logger warning message')  
    logger.error('logger error message')  
    logger.critical('logger critical message')  
    """    
    def createLogger(self, logger_name, log_file):
        prefix = os.path.dirname(log_file)
        if not os.path.exists(prefix):
            os.makedirs(prefix)     #// 注意这句话会在当前目录下创建文件夹out,然后在out文件夹下类似log_20190420.log的文档
        # 创建一个logger
        logger = logging.getLogger(logger_name)  
        logger.setLevel(logging.INFO)           #//设置日志记录级别
        # 创建一个handler，用于写入日志文件 //将日志记录输出发送到磁盘文件  
        fh = logging.FileHandler(log_file)  
        # 再创建一个handler，用于输出到控制台    
        ch = logging.StreamHandler()  
        # 定义handler的输出格式formatter //Formatter对象定义了log信息的结构和内容
        #// %(asctime)s 字符串形式的当前时间。默认格式是“2003-07-08 16:49:45,896”。逗号后面的是毫秒
        #// %(name)s Logger的名字
        #// %(levelname)s 文本形式的日志级别
        #// %(message)s 用户输出的消息
        formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')  
        fh.setFormatter(formatter)  
        ch.setFormatter(formatter)  
        # 给logger添加handler    
        logger.addHandler(fh)  
        logger.addHandler(ch)
        self.logger = logger
        return self.logger
