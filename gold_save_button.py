with open('screens/MainStore.js', 'r') as f:
    content = f.read()

old = """  saveVendorBtn: {
    backgroundColor: '#22C55E', borderRadius: 10,
    padding: 12, alignItems: 'center',
  },"""

new = """  saveVendorBtn: {
    backgroundColor: '#C9A84C', borderRadius: 10,
    padding: 12, alignItems: 'center',
  },"""

if old in content:
    content = content.replace(old, new, 1)
    with open('screens/MainStore.js', 'w') as f:
        f.write(content)
    print("Applied - primary submit button now gold")
else:
    print("Anchor not found")
