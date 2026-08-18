with open('screens/MainStore.js', 'r') as f:
    content = f.read()

changes = 0

old1 = '''              const r = await fetch(`${API_URL}/staff/${staffId}/reset-pin`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ pin: newPin })
              });'''
new1 = '''              const r = await fetch(`${API_URL}/staff/${staffId}/reset-pin`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'x-staff-session-token': staff?.sessionToken || '' },
                body: JSON.stringify({ pin: newPin })
              });'''
if old1 in content:
    content = content.replace(old1, new1, 1)
    changes += 1
    print("1/2: reset-pin call now sends session token")
else:
    print("FAILED 1/2")

old2 = '''          await fetch(`${API_URL}/staff/${staff?.id}/pin`, {
            method: 'PUT', headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ pin: newPin })
          });'''
new2 = '''          await fetch(`${API_URL}/staff/${staff?.id}/pin`, {
            method: 'PUT', headers: { 'Content-Type': 'application/json', 'x-staff-session-token': staff?.sessionToken || '' },
            body: JSON.stringify({ pin: newPin })
          });'''
if old2 in content:
    content = content.replace(old2, new2, 1)
    changes += 1
    print("2/2: update-pin call now sends session token")
else:
    print("FAILED 2/2")

with open('screens/MainStore.js', 'w') as f:
    f.write(content)

print(f"\n{changes}/2 applied")
