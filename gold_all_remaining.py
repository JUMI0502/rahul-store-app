import shutil

files_to_convert = [
    "screens/AddProductScreen.js",
    "screens/AttendanceScreen.js",
    "screens/BroadcastScreen.js",
    "screens/CustomerAnalyticsScreen.js",
    "screens/CustomerManagementScreen.js",
    "screens/PurchaseOrdersScreen.js",
    "screens/QRScannerScreen.js",
    "screens/SalesDashboardScreen.js",
    "screens/ServiceRemindersScreen.js",
    "screens/AbandonedCartsScreen.js",
]

total_hex = 0
total_rgba = 0

for path in files_to_convert:
    shutil.copy(path, path + ".goldbackup")
    with open(path, "r") as f:
        content = f.read()
    h = content.count("#22C55E")
    r = content.count("34,197,94")
    content = content.replace("#22C55E", "#C9A84C")
    content = content.replace("34,197,94", "201,168,76")
    with open(path, "w") as f:
        f.write(content)
    total_hex += h
    total_rgba += r
    print(f"{path}: {h} hex + {r} rgba converted")

print(f"\nTotal (10 files): {total_hex} hex + {total_rgba} rgba = {total_hex + total_rgba} instances")

# WarrantyReturnsScreen.js - protect the 'resolved: G' status color
path = "screens/WarrantyReturnsScreen.js"
shutil.copy(path, path + ".goldbackup")
with open(path, "r") as f:
    content = f.read()

old_protect = "const STATUS_COLORS = { pending: '#F59E0B', resolved: G, rejected: '#EF4444' };"
new_protect = "const STATUS_COLORS = { pending: '#F59E0B', resolved: '###KEEPGREEN###', rejected: '#EF4444' };"
if old_protect in content:
    content = content.replace(old_protect, new_protect, 1)
    print("\nWarrantyReturnsScreen.js: protected 'resolved' status color")
else:
    print("\nWarrantyReturnsScreen.js: WARNING - protection anchor not found")

h = content.count("#22C55E")
r = content.count("34,197,94")
content = content.replace("#22C55E", "#C9A84C")
content = content.replace("34,197,94", "201,168,76")
content = content.replace("###KEEPGREEN###", "G")

with open(path, "w") as f:
    f.write(content)
print(f"WarrantyReturnsScreen.js: {h} hex + {r} rgba converted (resolved status restored to green)")
