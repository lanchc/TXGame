# 常用工具类方法
import time
import random
import datetime
from Tools.configure import kMacro


# 时间随机延迟
def kk_delay(second = None):
    if second is None:
        r = random.randint(2, 8)
        time.sleep(0.08 * r)
    else:
        time.sleep(second)


# 坐标随机偏移
def kk_offset_coordinates(original_x, original_y):
    coefficient = 1.24
    offset_x = random.randint(2, 12) * coefficient
    offset_y = random.randint(2, 12) * coefficient
    return original_x + offset_x + 2, original_y + offset_y + 2


# 坐标转换计算
def kk_transform_coordinates(original_x, original_y):
    real_x = int((original_x / kMacro.screen_w) * kMacro.target_w)
    real_y = int((original_y / kMacro.screen_h) * kMacro.target_h)
    return real_x, real_y


# 获取当前时间戳
def kk_time_current_timestamp():
    return datetime.datetime.now()


# 比较记录时间跟当前时间差
def kk_time_difference(record_time):
    return kk_time_current_timestamp() - record_time
