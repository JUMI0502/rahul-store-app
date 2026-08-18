import shutil

PATH = "screens/MainStore.js"

with open(PATH, "r") as f:
    content = f.read()

shutil.copy(PATH, PATH + ".backup17")
print(f"Backup saved to {PATH}.backup17")

changes_made = 0

# 1. Import
old1 = "import BroadcastScreen from './BroadcastScreen';"
new1 = """import BroadcastScreen from './BroadcastScreen';
import ServiceRemindersScreen from './ServiceRemindersScreen';"""
if old1 in content:
    content = content.replace(old1, new1, 1)
    changes_made += 1
    print("1/4 Added import")
else:
    print("1/4 FAILED")

# 2. State
old2 = "  const [showBroadcast, setShowBroadcast] = useState(false);"
new2 = """  const [showBroadcast, setShowBroadcast] = useState(false);
  const [showServiceReminders, setShowServiceReminders] = useState(false);"""
if old2 in content:
    content = content.replace(old2, new2, 1)
    changes_made += 1
    print("2/4 Added state")
else:
    print("2/4 FAILED")

# 3. Screen conditional render
old3 = "  if (showBroadcast) return ("
new3 = """  if (showServiceReminders) return (
    <ServiceRemindersScreen onBack={() => setShowServiceReminders(false)} />
  );
  if (showBroadcast) return ("""
if old3 in content:
    content = content.replace(old3, new3, 1)
    changes_made += 1
    print("3/4 Added conditional render")
else:
    print("3/4 FAILED")

# 4. Add button in Reports section, next to Mechanic Approvals
old4 = """            {/* MECHANIC APPROVALS */}
            {(isOwner || isSenior) && ("""
new4 = """            {/* SERVICE REMINDERS */}
            {(isOwner || isSenior) && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => setShowServiceReminders(true)}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="time" size={22} color="#25D366" />
                  <View>
                    <Text style={s.customerHistoryBtnTitle}>Service Reminders</Text>
                    <Text style={s.customerHistoryBtnSub}>Nudge customers who haven't visited recently</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {/* MECHANIC APPROVALS */}
            {(isOwner || isSenior) && ("""
if old4 in content:
    content = content.replace(old4, new4, 1)
    changes_made += 1
    print("4/4 Added button")
else:
    print("4/4 FAILED")

with open(PATH, "w") as f:
    f.write(content)

print(f"\n{changes_made}/4 changes applied.")
