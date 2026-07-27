@'
with open('datadump.json', 'rb') as f:
    raw = f.read()

try:
    text = raw.decode('cp1252')
    print("Decoded successfully with cp1252")
except UnicodeDecodeError as e:
    print(f"cp1252 failed too: {e}")
    text = raw.decode('utf-8', errors='replace')
    print("Fell back to utf-8 with replacement characters")

with open('datadump_fixed.json', 'w', encoding='utf-8') as f:
    f.write(text)

print("Done - wrote datadump_fixed.json")
'@ | Set-Content -Path fix_encoding.py -Encoding UTF8