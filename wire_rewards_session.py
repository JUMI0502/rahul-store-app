with open('screens/MainStore.js', 'r') as f:
    content = f.read()

changes = 0

old1 = '''      const r = await fetch(`${API_URL}/rewards`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: newRewardName,
          description: newRewardDesc,
          points_required: parseInt(newRewardPoints)
        })
      });'''
new1 = '''      const r = await fetch(`${API_URL}/rewards`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'x-staff-session-token': staff?.sessionToken || '' },
        body: JSON.stringify({
          name: newRewardName,
          description: newRewardDesc,
          points_required: parseInt(newRewardPoints)
        })
      });'''
if old1 in content:
    content = content.replace(old1, new1, 1)
    changes += 1
    print("1/2: create reward now sends session token")
else:
    print("FAILED 1/2")

old2 = '''      const r = await fetch(`${API_URL}/rewards/${id}`, { method: 'DELETE' });'''
new2 = '''      const r = await fetch(`${API_URL}/rewards/${id}`, { method: 'DELETE', headers: { 'x-staff-session-token': staff?.sessionToken || '' } });'''
if old2 in content:
    content = content.replace(old2, new2, 1)
    changes += 1
    print("2/2: delete reward now sends session token")
else:
    print("FAILED 2/2")

with open('screens/MainStore.js', 'w') as f:
    f.write(content)

print(f"\n{changes}/2 applied")
