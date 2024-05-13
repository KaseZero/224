import time
t_tuple = time.localtime()
print('当前时间元组:{}'.format(t_tuple))
print('当前年:{}'.format(t_tuple.tm_year))
print('当前月:{}'.format(t_tuple.tm_mon))
print('当前日:{}'.format(t_tuple.tm_mday))
print('当前时:{}'.format(t_tuple.tm_hour))
print('当前分:{}'.format(t_tuple.tm_min))
print('当前秒:{}'.format(t_tuple.tm_sec))
print('当前周几:{}'.format(t_tuple.tm_wday))
print('当前是一年中第几天:{}'.format(t_tuple.tm_yday))
print('当前是否夏令时:{}'.format(t_tuple.tm_isdst))

