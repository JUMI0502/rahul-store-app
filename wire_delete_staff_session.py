with open('screens/MainStore.js', 'r') as f:
    content = f.read()

old = '''              await fetch(`${API_URL}/staff/${staffId}`, { method: 'DELETE' });'''
new = '''              await fetch(`${API_URL}/staff/${staffId}`, { method: 'DELETE', headers: { 'x-staff-session-token': staff?.sessionToken || '' } });'''

if old in content:
    content = content.replace(old, new, 1)
    with open('screens/MainStore.js', 'w') as f:
        f.write(content)
    print("Applied - delete staff now sends manager session token")
else:
    print("Anchor not found")
