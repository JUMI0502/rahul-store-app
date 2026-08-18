import shutil

PATH = "screens/MainStore.js"

with open(PATH, "r") as f:
    content = f.read()

shutil.copy(PATH, PATH + ".backup18")
print(f"Backup saved to {PATH}.backup18")

changes_made = 0

# 1. Import
old1 = "import ServiceRemindersScreen from './ServiceRemindersScreen';"
new1 = """import ServiceRemindersScreen from './ServiceRemindersScreen';
import WarrantyReturnsScreen from './WarrantyReturnsScreen';"""
if old1 in content:
    content = content.replace(old1, new1, 1)
    changes_made += 1
    print("1/4 Added import")
else:
    print("1/4 FAILED")

# 2. State
old2 = "  const [showServiceReminders, setShowServiceReminders] = useState(false);"
new2 = """  const [showServiceReminders, setShowServiceReminders] = useState(false);
  const [showWarrantyReturns, setShowWarrantyReturns] = useState(false);"""
if old2 in content:
    content = content.replace(old2, new2, 1)
    changes_made += 1
    print("2/4 Added state")
else:
    print("2/4 FAILED")

# 3. Screen conditional render
old3 = "  if (showServiceReminders) return ("
new3 = """  if (showWarrantyReturns) return (
    <WarrantyReturnsScreen onBack={() => setShowWarrantyReturns(false)} staff={staff} />
  );
  if (showServiceReminders) return ("""
if old3 in content:
    content = content.replace(old3, new3, 1)
    changes_made += 1
    print("3/4 Added conditional render")
else:
    print("3/4 FAILED")

# 4. Add button in Reports section
old4 = """            {/* SERVICE REMINDERS */}
            {(isOwner || isSenior) && ("""
new4 = """            {/* WARRANTY & RETURNS */}
            {(isOwner || isSenior) && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => setShowWarrantyReturns(true)}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="shield-checkmark" size={22} color="#F59E0B" />
                  <View>
                    <Text style={s.customerHistoryBtnTitle}>Warranty & Returns</Text>
                    <Text style={s.customerHistoryBtnSub}>Track defect claims and resolutions</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {/* SERVICE REMINDERS */}
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
