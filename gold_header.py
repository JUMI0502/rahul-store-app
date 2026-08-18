with open('screens/MainStore.js', 'r') as f:
    content = f.read()

replacements = [
    ("borderBottomColor: 'rgba(34,197,94,0.15)', gap: 8,", "borderBottomColor: 'rgba(201,168,76,0.25)', gap: 8,"),
    ("headerRole: { fontSize: 10, color: 'rgba(34,197,94,0.6)', letterSpacing: 2, marginBottom: 2 },", "headerRole: { fontSize: 10, color: 'rgba(201,168,76,0.7)', letterSpacing: 2, marginBottom: 2 },"),
    ("refreshBtn: { backgroundColor: 'rgba(34,197,94,0.1)', borderRadius: 10, padding: 8, borderWidth: 1, borderColor: 'rgba(34,197,94,0.2)' },", "refreshBtn: { backgroundColor: 'rgba(201,168,76,0.1)', borderRadius: 10, padding: 8, borderWidth: 1, borderColor: 'rgba(201,168,76,0.2)' },"),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new, 1)
        count += 1

with open('screens/MainStore.js', 'w') as f:
    f.write(content)

print(f'{count}/3 applied')
