str = input()
dn = {}
for ch in str:
    if ch not in dn:
        dn[ch] = 1
    else:
        dn[ch] += 1
sorted_dict = dict(sorted(dn.items(), key=lambda item: item[0]))
print(dn)
for key, value in sorted_dict.items():
    print(f"Character:{key}->{value}")
