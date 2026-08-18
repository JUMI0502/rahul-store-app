with open('screens/MainStore.js', 'r') as f:
    content = f.read()

old = '''      const r = await fetch(`${API_URL}/mechanics/${id}/approve`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status, approved_by: staff?.name })
      });'''
new = '''      const r = await fetch(`${API_URL}/mechanics/${id}/approve`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', 'x-staff-session-token': staff?.sessionToken || '' },
        body: JSON.stringify({ status, approved_by: staff?.name })
      });'''

if old in content:
    content = content.replace(old, new, 1)
    with open('screens/MainStore.js', 'w') as f:
        f.write(content)
    print("Applied - mechanic approval now sends staff session token")
else:
    print("Anchor not found")
