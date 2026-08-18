with open('screens/WarrantyReturnsScreen.js', 'r') as f:
    content = f.read()

changes = 0

old1 = '''      const r = await fetch(`${API_URL}/warranty-claims/${claimId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          status: 'resolved',
          resolution_type: resolutionType,
          resolution_notes: resolutionNotes.trim(),
          resolved_by: staff?.name || 'Staff'
        })
      });'''
new1 = '''      const r = await fetch(`${API_URL}/warranty-claims/${claimId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', 'x-staff-session-token': staff?.sessionToken || '' },
        body: JSON.stringify({
          status: 'resolved',
          resolution_type: resolutionType,
          resolution_notes: resolutionNotes.trim(),
          resolved_by: staff?.name || 'Staff'
        })
      });'''
if old1 in content:
    content = content.replace(old1, new1, 1)
    changes += 1
    print("1/2: resolveClaim now sends session token")
else:
    print("FAILED 1/2")

old2 = '''          await fetch(`${API_URL}/warranty-claims/${claimId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ status: 'rejected', resolved_by: staff?.name || 'Staff' })
          });'''
new2 = '''          await fetch(`${API_URL}/warranty-claims/${claimId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json', 'x-staff-session-token': staff?.sessionToken || '' },
            body: JSON.stringify({ status: 'rejected', resolved_by: staff?.name || 'Staff' })
          });'''
if old2 in content:
    content = content.replace(old2, new2, 1)
    changes += 1
    print("2/2: rejectClaim now sends session token")
else:
    print("FAILED 2/2")

with open('screens/WarrantyReturnsScreen.js', 'w') as f:
    f.write(content)

print(f"\n{changes}/2 applied")
