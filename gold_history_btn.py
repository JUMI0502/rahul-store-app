with open('screens/MainStore.js', 'r') as f:
    content = f.read()

old = """  customerHistoryBtn: {
    flexDirection: 'row', alignItems: 'center',
    backgroundColor: '#0D1A0D', borderRadius: 14, padding: 16,
    marginBottom: 14, borderWidth: 1, borderColor: 'rgba(79,110,247,0.2)',
  },"""

new = """  customerHistoryBtn: {
    flexDirection: 'row', alignItems: 'center',
    backgroundColor: '#0D1A0D', borderRadius: 14, padding: 16,
    marginBottom: 14, borderWidth: 1, borderColor: 'rgba(201,168,76,0.2)',
  },"""

if old in content:
    content = content.replace(old, new, 1)
    with open('screens/MainStore.js', 'w') as f:
        f.write(content)
    print("Applied - Reports menu items now gold-bordered")
else:
    print("Anchor not found")
