import logging,os
# ��ӡ��־
# logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
# log = logging.getLogger(__name__)
# logging.StreamHandler()
# logFile = logging.FileHandler('logTest.txt','a',encoding='utf-8')
# fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
# logFile.setFormatter(fmt)
# log = logging.Logger('logTest',level=logging.DEBUG)
#
# log.info("��ʼ")
# log.debug("debug����")
# log.warning("waring����")


# logFile = logging.FileHandler('logTest.txt','a',encoding='utf-8')
# fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
# logFile.setFormatter(fmt)
# LoggerMany = logging.Logger('logTest',level=logging.DEBUG)
# LoggerMany.addHandler(logFile)
# LoggerMany.critical('info')
# LoggerMany.info("info����")
# LoggerMany.debug("debug����")
# LoggerMany.warning("waring����")

# ����һ��logger
log = logging.getLogger()
log.setLevel(logging.INFO)
# ����һ��handler������д����־�ļ�
base_dir = os.path.dirname(os.path.realpath(__file__))                                       #��ȡ�ļ�����·��
pro_dir = os.path.dirname(os.path.realpath(__file__)).split('Utils')[0]               #��Ŀ����·��
test_dir = os.path.join(base_dir)                                                #������������Ŀ¼
test_report = os.path.join(pro_dir,'Log','log.txt')         #���Ա�������Ŀ¼
# print(base_dir)
# print(pro_dir)
# print(test_dir)
# print(test_report)

fh = logging.FileHandler(test_report ,'a',encoding='utf-8')
fh.setFormatter(logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s"))
log.addHandler(fh)
# ����һ��handler�����������̨
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s"))
log.addHandler(ch)

# log.critical('info')
# log.info("info����")
# log.debug("debug����")
# log.warning("waring����")
# log.error("error����")