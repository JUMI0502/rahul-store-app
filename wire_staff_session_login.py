with open('screens/LoginScreen.js', 'r') as f:
    content = f.read()

old = '''      const d = await r.json();
      if (d.staff) { await Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success); onLogin(d.staff); return; }'''
new = '''      const d = await r.json();
      if (d.staff) {
        await Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success);
        onLogin({ ...d.staff, sessionToken: d.session_token });
        return;
      }'''

if old in content:
    content = content.replace(old, new, 1)
    with open('screens/LoginScreen.js', 'w') as f:
        f.write(content)
    print("Applied - session token attached to staff object on login")
else:
    print("Anchor not found")
