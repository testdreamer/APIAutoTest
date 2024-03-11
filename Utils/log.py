import logging,os
# 打印日志
# logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
# log = logging.getLogger(__name__)
# logging.StreamHandler()
# logFile = logging.FileHandler('logTest.txt','a',encoding='utf-8')
# fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
# logFile.setFormatter(fmt)
# log = logging.Logger('logTest',level=logging.DEBUG)
#
# log.info("开始")
# log.debug("debug级别")
# log.warning("waring级别")


# logFile = logging.FileHandler('logTest.txt','a',encoding='utf-8')
# fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
# logFile.setFormatter(fmt)
# LoggerMany = logging.Logger('logTest',level=logging.DEBUG)
# LoggerMany.addHandler(logFile)
# LoggerMany.critical('info')
# LoggerMany.info("info级别")
# LoggerMany.debug("debug级别")
# LoggerMany.warning("waring级别")

# 创建一个logger
log = logging.getLogger()
log.setLevel(logging.INFO)
# 创建一个handler，用于写入日志文件
base_dir = os.path.dirname(os.path.realpath(__file__))                                       #获取文件所在路径
pro_dir = os.path.dirname(os.path.realpath(__file__)).split('Utils')[0]               #项目所在路径
test_dir = os.path.join(base_dir)                                                #测试用例所在目录
test_report = os.path.join(pro_dir,'Log','log.txt')         #测试报告所在目录
# print(base_dir)
# print(pro_dir)
# print(test_dir)
# print(test_report)

fh = logging.FileHandler(test_report ,'a',encoding='utf-8')
fh.setFormatter(logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s"))
log.addHandler(fh)
# 创建一个handler，输出到控制台
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s"))
log.addHandler(ch)

# log.critical('info')
# log.info("info级别")
# log.debug("debug级别")
# log.warning("waring级别")
# log.error("error级别")