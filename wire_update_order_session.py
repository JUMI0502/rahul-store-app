with open('screens/MainStore.js', 'r') as f:
    content = f.read()

changes = 0

old1 = '''      await fetch(`${API_URL}/orders/${orderId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status: newStatus })
      });'''
new1 = '''      await fetch(`${API_URL}/orders/${orderId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', 'x-staff-session-token': staff?.sessionToken || '' },
        body: JSON.stringify({ status: newStatus })
      });'''
if old1 in content:
    content = content.replace(old1, new1, 1)
    changes += 1
    print("1/2: updateStatus now sends session token")
else:
    print("FAILED 1/2")

old2 = '''      const r = await fetch(`${API_URL}/orders/${orderId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ payment_type: type })
      });'''
new2 = '''      const r = await fetch(`${API_URL}/orders/${orderId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', 'x-staff-session-token': staff?.sessionToken || '' },
        body: JSON.stringify({ payment_type: type })
      });'''
if old2 in content:
    content = content.replace(old2, new2, 1)
    changes += 1
    print("2/2: updatePayment now sends session token")
else:
    print("FAILED 2/2")

with open('screens/MainStore.js', 'w') as f:
    f.write(content)

print(f"\n{changes}/2 applied")
