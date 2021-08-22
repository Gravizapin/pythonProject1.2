
time_us = int(input('Введите время в секундах :'))
time_h = time_us // 3600
time_hm = time_us % 3600

time_m = time_hm // 60
time_s = time_hm % 60
text = f"{time_h:02}:{time_m:02}:{time_s:02}"
print(text)