import _scanner

var1 = _scanner.scan_now('8.8.8.8')

for keys, values in var1.items():
    print(keys, ":", values)
    print('----------')