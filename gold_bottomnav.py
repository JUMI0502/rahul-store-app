with open('screens/MainStore.js', 'r') as f:
    content = f.read()

replacements = [
    ("color={active === tab.id ? '#22C55E' : 'rgba(255,255,255,0.35)'}", "color={active === tab.id ? '#C9A84C' : 'rgba(255,255,255,0.35)'}"),
    ("borderTopWidth: 1, borderTopColor: 'rgba(34,197,94,0.2)',", "borderTopWidth: 1, borderTopColor: 'rgba(201,168,76,0.25)',"),
    ("  labelActive: { color: G },\n  dot: { width: 4, height: 4, borderRadius: 2, backgroundColor: G, marginTop: 2 },",
     "  labelActive: { color: '#C9A84C' },\n  dot: { width: 4, height: 4, borderRadius: 2, backgroundColor: '#C9A84C', marginTop: 2 },"),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new, 1)
        count += 1
    else:
        print(f"FAILED: {old[:60]}")

with open('screens/MainStore.js', 'w') as f:
    f.write(content)

print(f'{count}/3 applied')
