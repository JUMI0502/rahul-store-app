with open('screens/MainStore.js', 'r') as f:
    content = f.read()

changes = 0

old1 = '''      await fetch(`${API_URL}/offers`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          title: offerTitle.trim(), description: offerDesc.trim(),
          discount_percent: parseInt(offerDiscount) || 0, emoji: offerEmoji
        })
      });'''
new1 = '''      await fetch(`${API_URL}/offers`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'x-staff-session-token': staff?.sessionToken || '' },
        body: JSON.stringify({
          title: offerTitle.trim(), description: offerDesc.trim(),
          discount_percent: parseInt(offerDiscount) || 0, emoji: offerEmoji
        })
      });'''
if old1 in content:
    content = content.replace(old1, new1, 1)
    changes += 1
    print("1/3: createOffer now sends session token")
else:
    print("FAILED 1/3")

old2 = '''      const r = await fetch(`${API_URL}/offers/${id}/toggle`, { method: 'PUT' });'''
new2 = '''      const r = await fetch(`${API_URL}/offers/${id}/toggle`, { method: 'PUT', headers: { 'x-staff-session-token': staff?.sessionToken || '' } });'''
if old2 in content:
    content = content.replace(old2, new2, 1)
    changes += 1
    print("2/3: toggleOffer now sends session token")
else:
    print("FAILED 2/3")

old3 = '''          const r = await fetch(`${API_URL}/offers/${id}`, { method: 'DELETE' });'''
new3 = '''          const r = await fetch(`${API_URL}/offers/${id}`, { method: 'DELETE', headers: { 'x-staff-session-token': staff?.sessionToken || '' } });'''
if old3 in content:
    content = content.replace(old3, new3, 1)
    changes += 1
    print("3/3: deleteOffer now sends session token")
else:
    print("FAILED 3/3")

with open('screens/MainStore.js', 'w') as f:
    f.write(content)

print(f"\n{changes}/3 applied")
