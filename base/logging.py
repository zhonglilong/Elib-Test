import logging
import logging.handlers
from base.config import LOG_PATH


# 设置日志配置
# def set_log_config():
# 创建日志器对象 / 设置日志级别
logger = logging.getLogger()      # 默认日志器名称为 root
logger.setLevel(level=logging.INFO)

# 创建处理器对象: 输出到控制台 + 文件(按时间切割)
ls = logging.StreamHandler()
lf = logging.handlers.TimedRotatingFileHandler(filename=LOG_PATH, when="d", backupCount=3)    # 按天切割

# 创建格式器对象
fmt = "%(asctime)s %(levelname)s [%(filename)s:%(funcName)s:%(lineno)d] - %(message)s"
formatter = logging.Formatter(fmt=fmt)

# 将格式器添加到处理器
ls.setFormatter(formatter)
lf.setFormatter(formatter)

# 将处理器添加到日志器
logger.addHandler(ls)
logger.addHandler(lf)
