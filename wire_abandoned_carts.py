import shutil

PATH = "screens/MainStore.js"

with open(PATH, "r") as f:
    content = f.read()

shutil.copy(PATH, PATH + ".backup19")
print(f"Backup saved to {PATH}.backup19")

changes_made = 0

# 1. Import
old1 = "import WarrantyReturnsScreen from './WarrantyReturnsScreen';"
new1 = """import WarrantyReturnsScreen from './WarrantyReturnsScreen';
import AbandonedCartsScreen from './AbandonedCartsScreen';"""
if old1 in content:
    content = content.replace(old1, new1, 1)
    changes_made += 1
    print("1/4 Added import")
else:
    print("1/4 FAILED")

# 2. State
old2 = "  const [showWarrantyReturns, setShowWarrantyReturns] = useState(false);"
new2 = """  const [showWarrantyReturns, setShowWarrantyReturns] = useState(false);
  const [showAbandonedCarts, setShowAbandonedCarts] = useState(false);"""
if old2 in content:
    content = content.replace(old2, new2, 1)
    changes_made += 1
    print("2/4 Added state")
else:
    print("2/4 FAILED")

# 3. Screen conditional render
old3 = "  if (showWarrantyReturns) return ("
new3 = """  if (showAbandonedCarts) return (
    <AbandonedCartsScreen onBack={() => setShowAbandonedCarts(false)} />
  );
  if (showWarrantyReturns) return ("""
if old3 in content:
    content = content.replace(old3, new3, 1)
    changes_made += 1
    print("3/4 Added conditional render")
else:
    print("3/4 FAILED")

# 4. Button in Reports section
old4 = """            {/* WARRANTY & RETURNS */}
            {(isOwner || isSenior) && ("""
new4 = """            {/* ABANDONED CARTS */}
            {(isOwner || isSenior) && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => setShowAbandonedCarts(true)}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="cart" size={22} color="#4F6EF7" />
                  <View>
                    <Text style={s.customerHistoryBtnTitle}>Abandoned Carts</Text>
                    <Text style={s.customerHistoryBtnSub}>Nudge customers who didn't finish checking out</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {/* WARRANTY & RETURNS */}
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
