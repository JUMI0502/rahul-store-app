import shutil

PATH = "screens/SalesDashboardScreen.js"

with open(PATH, "r") as f:
    content = f.read()

shutil.copy(PATH, PATH + ".backup3")
print(f"Backup saved to {PATH}.backup3")

changes_made = 0

# 1. Add Ionicons import
old1 = "import * as Haptics from 'expo-haptics';"
new1 = """import * as Haptics from 'expo-haptics';
import { Ionicons } from '@expo/vector-icons';"""
if old1 in content:
    content = content.replace(old1, new1, 1)
    changes_made += 1
    print("1/7 Added Ionicons import")
else:
    print("1/7 FAILED")

# 2. Convert RevenueCard to use Ionicons
old2 = """      <View style={[rc.iconBox, { backgroundColor: color + '15' }]}>
        <Text style={rc.icon}>{icon}</Text>
      </View>"""
new2 = """      <View style={[rc.iconBox, { backgroundColor: color + '15' }]}>
        <Ionicons name={icon} size={22} color={color} />
      </View>"""
if old2 in content:
    content = content.replace(old2, new2, 1)
    changes_made += 1
    print("2/7 Converted RevenueCard to Ionicons")
else:
    print("2/7 FAILED")

# 3. Fix call sites with real icon names
old3 = """            <RevenueCard icon="" label="Cash" color={G}
              value={`₹${(cashRevenue/1000).toFixed(1)}k`} />
            <RevenueCard icon="" label="UPI" color="#4F6EF7"
              value={`₹${(upiRevenue/1000).toFixed(1)}k`} />"""
new3 = """            <RevenueCard icon="cash-outline" label="Cash" color={G}
              value={`₹${(cashRevenue/1000).toFixed(1)}k`} />
            <RevenueCard icon="phone-portrait-outline" label="UPI" color="#4F6EF7"
              value={`₹${(upiRevenue/1000).toFixed(1)}k`} />"""
if old3 in content:
    content = content.replace(old3, new3, 1)
    changes_made += 1
    print("3/7 Fixed Cash/UPI icons")
else:
    print("3/7 FAILED")

old4 = """            <RevenueCard icon="⏳" label="Pending" color="#F59E0B"
              value={`₹${(pendingRevenue/1000).toFixed(1)}k`} />
            <RevenueCard icon="⏰" label="Peak Hour" color="#A78BFA\""""
new4 = """            <RevenueCard icon="hourglass-outline" label="Pending" color="#F59E0B"
              value={`₹${(pendingRevenue/1000).toFixed(1)}k`} />
            <RevenueCard icon="time-outline" label="Peak Hour" color="#A78BFA\""""
if old4 in content:
    content = content.replace(old4, new4, 1)
    changes_made += 1
    print("4/7 Fixed Pending/Peak Hour icons")
else:
    print("4/7 FAILED")

# 5. Remove the internal debug notice banner (unprofessional to show staff)
old5 = """          {/* API STATUS NOTICE */}
          {!apiStatus.summary && (
            <View style={s.noticeBanner}>
              <Text style={s.noticeText}>
                ℹ️ Using order data directly · Summary API not connected yet
              </Text>
            </View>
          )}

"""
if old5 in content:
    content = content.replace(old5, "", 1)
    changes_made += 1
    print("5/7 Removed internal debug notice banner")
else:
    print("5/7 FAILED")

# 6. Fix loading state - remove hollow decorative text, use proper spinner
old6 = """      {loading ? (
        <View style={s.centerBox}>
          <Text style={{ fontSize: 36, marginBottom: 10 }}></Text>
          <Text style={s.loadingText}>Loading dashboard...</Text>
        </View>
      ) : ("""
new6 = """      {loading ? (
        <View style={s.centerBox}>
          <ActivityIndicator size="large" color={G} style={{ marginBottom: 12 }} />
          <Text style={s.loadingText}>Loading dashboard...</Text>
        </View>
      ) : ("""
if old6 in content:
    content = content.replace(old6, new6, 1)
    changes_made += 1
    print("6/7 Fixed loading state")
else:
    print("6/7 FAILED")

# 7. Add ActivityIndicator import if not present
if "ActivityIndicator" not in content.split("\n")[0:10].__str__():
    old7 = """  Animated, RefreshControl, Dimensions
} from 'react-native';"""
    new7 = """  Animated, RefreshControl, Dimensions, ActivityIndicator
} from 'react-native';"""
    if old7 in content:
        content = content.replace(old7, new7, 1)
        changes_made += 1
        print("7/7 Added ActivityIndicator import")
    else:
        print("7/7 FAILED")
else:
    changes_made += 1
    print("7/7 ActivityIndicator already imported - skipped")

with open(PATH, "w") as f:
    f.write(content)

print(f"\n{changes_made}/7 changes applied.")
