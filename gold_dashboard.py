with open('screens/MainStore.js', 'r') as f:
    content = f.read()

replacements = [
    ("dashBanner: { backgroundColor: '#0D1A0D', borderBottomWidth: 1, borderBottomColor: 'rgba(34,197,94,0.1)', padding: 12 },",
     "dashBanner: { backgroundColor: '#0D1A0D', borderBottomWidth: 1, borderBottomColor: 'rgba(201,168,76,0.15)', padding: 12 },"),
    ("dashCard: { flexDirection: 'row', alignItems: 'center', backgroundColor: 'rgba(34,197,94,0.05)', borderRadius: 12, padding: 12, marginBottom: 8, borderWidth: 1, borderColor: 'rgba(34,197,94,0.15)' },",
     "dashCard: { flexDirection: 'row', alignItems: 'center', backgroundColor: 'rgba(201,168,76,0.05)', borderRadius: 12, padding: 12, marginBottom: 8, borderWidth: 1, borderColor: 'rgba(201,168,76,0.2)' },"),
    ("cashRegBtn: { flex: 1, flexDirection: 'row', alignItems: 'center', justifyContent: 'center', gap: 6, backgroundColor: 'rgba(34,197,94,0.1)', borderRadius: 10, padding: 10, borderWidth: 1, borderColor: 'rgba(34,197,94,0.3)' },",
     "cashRegBtn: { flex: 1, flexDirection: 'row', alignItems: 'center', justifyContent: 'center', gap: 6, backgroundColor: 'rgba(201,168,76,0.1)', borderRadius: 10, padding: 10, borderWidth: 1, borderColor: 'rgba(201,168,76,0.3)' },"),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new, 1)
        count += 1
    else:
        print(f"FAILED: {old[:70]}")

with open('screens/MainStore.js', 'w') as f:
    f.write(content)

print(f'{count}/3 applied')
