import shutil

PATH = "screens/MainStore.js"

with open(PATH, "r") as f:
    content = f.read()

shutil.copy(PATH, PATH + ".backup2")
print(f"Backup saved to {PATH}.backup2")

changes_made = 0

# Add STORE_UPI constant near WHATSAPP constant
old_const = "const WHATSAPP = '916300281504';"
new_const = """const WHATSAPP = '916300281504';
const STORE_UPI = 'rahulautospares@paytm';"""

if old_const in content:
    content = content.replace(old_const, new_const, 1)
    changes_made += 1
    print("Added STORE_UPI constant")
else:
    print("Could not find WHATSAPP constant anchor - skipped")

# Add the Send UPI button, owner/senior only, right after the phone row
old_phone_block = '''                {selectedOrder.customer_phone && (
                  <TouchableOpacity style={s.detailRow}
                    onPress={() => Linking.openURL(`tel:${selectedOrder.customer_phone}`)}>
                    <Text style={s.detailLabel}>Phone</Text>
                    <Text style={[s.detailValue, { color: G }]}>📞 {selectedOrder.customer_phone}</Text>
                  </TouchableOpacity>
                )}'''

new_phone_block = '''                {selectedOrder.customer_phone && (
                  <TouchableOpacity style={s.detailRow}
                    onPress={() => Linking.openURL(`tel:${selectedOrder.customer_phone}`)}>
                    <Text style={s.detailLabel}>Phone</Text>
                    <Text style={[s.detailValue, { color: G }]}>📞 {selectedOrder.customer_phone}</Text>
                  </TouchableOpacity>
                )}
                {selectedOrder.customer_phone && (isOwner || isSenior) && (
                  <TouchableOpacity style={s.detailRow}
                    onPress={() => {
                      const msg = `Please pay ₹${selectedOrder.total_amount} to:\\n${STORE_UPI}\\n\\nOrder: ${selectedOrder.custom_id || 'RAS-' + selectedOrder.id}`;
                      Linking.openURL(`https://wa.me/91${selectedOrder.customer_phone}?text=${encodeURIComponent(msg)}`);
                    }}>
                    <Text style={s.detailLabel}>Send UPI</Text>
                    <Text style={[s.detailValue, { color: G }]}>📱 Send Payment Details</Text>
                  </TouchableOpacity>
                )}'''

if old_phone_block in content:
    content = content.replace(old_phone_block, new_phone_block, 1)
    changes_made += 1
    print("Added Send UPI button (owner/senior only)")
else:
    print("Could not find phone row anchor - skipped")

with open(PATH, "w") as f:
    f.write(content)

print(f"\n{changes_made}/2 changes applied.")
