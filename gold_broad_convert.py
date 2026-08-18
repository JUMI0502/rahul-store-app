import re

with open('screens/MainStore.js', 'r') as f:
    content = f.read()

# Step 1: Protect the genuine "order ready = green" status exceptions with placeholders
protect = [
    ("  ready: '#22C55E', collected: 'rgba(255,255,255,0.3)'",
     "  ready: '###KEEPGREEN1###', collected: 'rgba(255,255,255,0.3)'"),
    ("<TouchableOpacity style={[s.zohoActionBtn, { backgroundColor: 'rgba(34,197,94,0.15)', borderColor: 'rgba(34,197,94,0.4)' }]}",
     "<TouchableOpacity style={[s.zohoActionBtn, { backgroundColor: 'rgba(###KEEPGREEN2###)', borderColor: 'rgba(###KEEPGREEN3###)' }]}"),
    ("<Text style={[s.zohoActionBtnText, { color: '#22C55E' }]}>Mark Ready</Text>",
     "<Text style={[s.zohoActionBtnText, { color: '###KEEPGREEN4###' }]}>Mark Ready</Text>"),
    ('<Ionicons name="checkmark" size={12} color="#22C55E" />',
     '<Ionicons name="checkmark" size={12} color="###KEEPGREEN5###" />'),
    ("{ label: 'Ready', key: 'ready', color: '#22C55E', icon: 'checkmark-circle-outline' },",
     "{ label: 'Ready', key: 'ready', color: '###KEEPGREEN6###', icon: 'checkmark-circle-outline' },"),
]

protected_count = 0
for old, new in protect:
    if old in content:
        content = content.replace(old, new, 1)
        protected_count += 1
    else:
        print(f"PROTECT FAILED: {old[:60]}")

print(f"Protected {protected_count}/5 genuine 'ready=green' exceptions")

# Step 2: Broad conversion of all remaining green to gold
before_hex = content.count("#22C55E")
before_rgba = content.count("34,197,94")

content = content.replace("#22C55E", "#C9A84C")
content = content.replace("34,197,94", "201,168,76")

print(f"Converted {before_hex} hex + {before_rgba} rgba instances to gold")

# Step 3: Restore the protected exceptions
restore = [
    ("###KEEPGREEN1###", "#22C55E"),
    ("###KEEPGREEN2###", "34,197,94,0.15"),
    ("###KEEPGREEN3###", "34,197,94,0.4"),
    ("###KEEPGREEN4###", "#22C55E"),
    ("###KEEPGREEN5###", "#22C55E"),
    ("###KEEPGREEN6###", "#22C55E"),
]

for old, new in restore:
    content = content.replace(old, new)

with open('screens/MainStore.js', 'w') as f:
    f.write(content)

print("Restored genuine green exceptions - done")
