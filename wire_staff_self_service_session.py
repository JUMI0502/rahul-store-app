with open('screens/MainStore.js', 'r') as f:
    content = f.read()

changes = 0

old1 = '''      const r = await fetch(`${API_URL}/staff/${staffId}/profile`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: editStaffName.trim(),
          phone: editStaffPhone.trim(),
          role: editStaffRole,
        })'''
new1 = '''      const r = await fetch(`${API_URL}/staff/${staffId}/profile`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', 'x-staff-session-token': staff?.sessionToken || '' },
        body: JSON.stringify({
          name: editStaffName.trim(),
          phone: editStaffPhone.trim(),
          role: editStaffRole,
        })'''
if old1 in content:
    content = content.replace(old1, new1, 1)
    changes += 1
    print("1/4: edit-other-staff profile call now sends session token")
else:
    print("FAILED 1/4")

old2 = '''            const r = await fetch(`${API_URL}/staff/${staff?.id}/clockout`, { method: 'POST' });'''
new2 = '''            const r = await fetch(`${API_URL}/staff/${staff?.id}/clockout`, { method: 'POST', headers: { 'x-staff-session-token': staff?.sessionToken || '' } });'''
if old2 in content:
    content = content.replace(old2, new2, 1)
    changes += 1
    print("2/4: clockout now sends session token")
else:
    print("FAILED 2/4")

old3 = '''        const r = await fetch(`${API_URL}/staff/${staff?.id}/clockin`, { method: 'POST' });'''
new3 = '''        const r = await fetch(`${API_URL}/staff/${staff?.id}/clockin`, { method: 'POST', headers: { 'x-staff-session-token': staff?.sessionToken || '' } });'''
if old3 in content:
    content = content.replace(old3, new3, 1)
    changes += 1
    print("3/4: clockin now sends session token")
else:
    print("FAILED 3/4")

old4 = '''      await fetch(`${API_URL}/staff/${staff?.id}/profile`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: editName.trim(), phone: editPhone.trim() })
      });'''
new4 = '''      await fetch(`${API_URL}/staff/${staff?.id}/profile`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', 'x-staff-session-token': staff?.sessionToken || '' },
        body: JSON.stringify({ name: editName.trim(), phone: editPhone.trim() })
      });'''
if old4 in content:
    content = content.replace(old4, new4, 1)
    changes += 1
    print("4/4: saveProfile (own profile) now sends session token")
else:
    print("FAILED 4/4")

with open('screens/MainStore.js', 'w') as f:
    f.write(content)

print(f"\n{changes}/4 applied")
