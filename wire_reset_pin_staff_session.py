changes = 0

# 1. CustomerManagementScreen.js - accept staff prop
with open('screens/CustomerManagementScreen.js', 'r') as f:
    content = f.read()

old1 = "export default function CustomerManagementScreen({ onBack }) {"
new1 = "export default function CustomerManagementScreen({ onBack, staff }) {"
if old1 in content:
    content = content.replace(old1, new1, 1)
    changes += 1
    print("1/3: staff prop accepted")
else:
    print("FAILED 1/3")

old2 = '''              const r = await fetch(`${API_URL}/customers/${customer.phone}/reset-pin`, { method: 'POST' });'''
new2 = '''              const r = await fetch(`${API_URL}/customers/${customer.phone}/reset-pin`, {
                method: 'POST',
                headers: { 'x-staff-session-token': staff?.sessionToken || '' },
              });'''
if old2 in content:
    content = content.replace(old2, new2, 1)
    changes += 1
    print("2/3: reset-pin call now sends staff session token")
else:
    print("FAILED 2/3")

with open('screens/CustomerManagementScreen.js', 'w') as f:
    f.write(content)

# 2. MainStore.js - pass staff down to CustomerManagementScreen
with open('screens/MainStore.js', 'r') as f:
    content2 = f.read()

old3 = '''    <CustomerManagementScreen onBack={() => setShowCustomers(false)} />'''
new3 = '''    <CustomerManagementScreen onBack={() => setShowCustomers(false)} staff={staff} />'''
if old3 in content2:
    content2 = content2.replace(old3, new3, 1)
    changes += 1
    print("3/3: MainStore now passes staff prop down")
else:
    print("FAILED 3/3")

with open('screens/MainStore.js', 'w') as f:
    f.write(content2)

print(f"\n{changes}/3 applied")
