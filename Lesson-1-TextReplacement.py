# Example 1
marker = 'AFK'
replacement = 'away from keyboard'
line = 'I will now go to sleep and be AFK until lunch time tomorrow.'

total = len(line)
m = len(marker)
replace = line.find('AFK')
newline = line[:replace] + replacement + line[replace + m:total]
print(newline)
