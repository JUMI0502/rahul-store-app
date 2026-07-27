import shutil

PATH = "screens/MainStore.js"

with open(PATH, "r") as f:
    content = f.read()

shutil.copy(PATH, PATH + ".backup3")
print(f"Backup saved to {PATH}.backup3")

changes_made = 0

old_fn = "  const deleteStaffMember = (staffId, staffName) => {"
new_fn = '''  const resetStaffPin = (staffId, staffName, staffPhone) => {
    const newPin = String(Math.floor(1000 + Math.random() * 9000));
    Alert.alert(
      'Reset PIN',
      `Generate a new PIN for ${staffName}?`,
      [
        { text: 'Cancel', style: 'cancel' },
        {
          text: 'Reset',
          onPress: async () => {
            try {
              const r = await fetch(`${API_URL}/staff/${staffId}/reset-pin`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ pin: newPin })
              });
              const d = await r.json();
              if (d.success) {
                Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success);
                Alert.alert(
                  'PIN Reset',
                  `New PIN: ${newPin}`,
                  [
                    {
                      text: 'Send via WhatsApp',
                      onPress: () => {
                        if (staffPhone) {
                          const msg = `Your new login PIN is: ${newPin}`;
                          Linking.openURL(`https://wa.me/91${staffPhone}?text=${encodeURIComponent(msg)}`);
                        }
                      }
                    },
                    { text: 'Done' }
                  ]
                );
              } else {
                Alert.alert('Error', d.error || 'Could not reset PIN');
              }
            } catch {
              Alert.alert('Error', 'Could not reset PIN');
            }
          }
        }
      ]
    );
  };

  const deleteStaffMember = (staffId, staffName) => {'''

if old_fn in content:
    content = content.replace(old_fn, new_fn, 1)
    changes_made += 1
    print("Added resetStaffPin function")
else:
    print("Could not find deleteStaffMember anchor - skipped")

old_buttons = '''                    <TouchableOpacity
                      onPress={() => deleteStaffMember(member.id, member.name)}>
                      <Ionicons name="trash-outline" size={20} color="#EF4444" />
                    </TouchableOpacity>'''

new_buttons = '''                    <TouchableOpacity
                      onPress={() => resetStaffPin(member.id, member.name, member.phone)}
                      style={{ marginRight: 14 }}>
                      <Ionicons name="key-outline" size={20} color="#4F6EF7" />
                    </TouchableOpacity>
                    <TouchableOpacity
                      onPress={() => deleteStaffMember(member.id, member.name)}>
                      <Ionicons name="trash-outline" size={20} color="#EF4444" />
                    </TouchableOpacity>'''

if old_buttons in content:
    content = content.replace(old_buttons, new_buttons, 1)
    changes_made += 1
    print("Added Reset PIN button to staff card")
else:
    print("Could not find delete button anchor - skipped")

with open(PATH, "w") as f:
    f.write(content)

print(f"\n{changes_made}/2 changes applied.")
