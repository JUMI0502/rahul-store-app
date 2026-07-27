import shutil

PATH = "screens/MainStore.js"

with open(PATH, "r") as f:
    content = f.read()

shutil.copy(PATH, PATH + ".backup13")
print(f"Backup saved to {PATH}.backup13")

changes_made = 0

# 1. Add state for edit-mode OEM toggle
old1 = "  const [stockAdjustReason, setStockAdjustReason] = useState('');"
new1 = """  const [stockAdjustReason, setStockAdjustReason] = useState('');
  const [stockAdjustIsOem, setStockAdjustIsOem] = useState(false);"""
if old1 in content:
    content = content.replace(old1, new1, 1)
    changes_made += 1
    print("1/4 Added stockAdjustIsOem state")
else:
    print("1/4 FAILED")

# 2. Initialize it when a product is selected (both trigger points)
old2 = "onPress={() => { setStockAdjustProduct(p); setStockAdjustQty(p.stock_qty.toString()); }}>"
new2 = "onPress={() => { setStockAdjustProduct(p); setStockAdjustQty(p.stock_qty.toString()); setStockAdjustIsOem(!!p.is_oem); }}>"
count2 = content.count(old2)
if count2 > 0:
    content = content.replace(old2, new2)
    changes_made += 1
    print(f"2/4 Initialized stockAdjustIsOem on selection ({count2} spot(s))")
else:
    print("2/4 FAILED")

# 3. Add the toggle UI + save call in the adjust form
old3 = """                <TextInput style={s.vendorInput}
                  placeholder="Reason (e.g. Damaged, Physical count)"
                  placeholderTextColor="rgba(255,255,255,0.2)"
                  value={stockAdjustReason} onChangeText={setStockAdjustReason} />
                <TouchableOpacity style={s.saveVendorBtn} onPress={adjustStock}>
                  <Text style={s.saveVendorBtnText}>Update Stock</Text>
                </TouchableOpacity>"""
new3 = """                <TextInput style={s.vendorInput}
                  placeholder="Reason (e.g. Damaged, Physical count)"
                  placeholderTextColor="rgba(255,255,255,0.2)"
                  value={stockAdjustReason} onChangeText={setStockAdjustReason} />

                <Text style={{ color: 'rgba(255,255,255,0.4)', fontSize: 12, marginBottom: 8, marginTop: 4 }}>Part Type</Text>
                <View style={{ flexDirection: 'row', gap: 10, marginBottom: 14 }}>
                  <TouchableOpacity
                    style={[s.oemToggleBtn, stockAdjustIsOem && s.oemToggleBtnActive]}
                    onPress={() => setStockAdjustIsOem(true)}>
                    <Text style={[s.oemToggleText, stockAdjustIsOem && s.oemToggleTextActive]}>Original OEM</Text>
                  </TouchableOpacity>
                  <TouchableOpacity
                    style={[s.oemToggleBtn, !stockAdjustIsOem && s.oemToggleBtnActive]}
                    onPress={() => setStockAdjustIsOem(false)}>
                    <Text style={[s.oemToggleText, !stockAdjustIsOem && s.oemToggleTextActive]}>Generic / Compatible</Text>
                  </TouchableOpacity>
                </View>

                <TouchableOpacity style={s.saveVendorBtn} onPress={async () => {
                  await adjustStock();
                  try {
                    await fetch(`${API_URL}/products/${stockAdjustProduct.id}/oem`, {
                      method: 'PUT',
                      headers: { 'Content-Type': 'application/json' },
                      body: JSON.stringify({ is_oem: stockAdjustIsOem })
                    });
                  } catch {}
                }}>
                  <Text style={s.saveVendorBtnText}>Update Stock</Text>
                </TouchableOpacity>"""
if old3 in content:
    content = content.replace(old3, new3, 1)
    changes_made += 1
    print("3/4 Added OEM toggle UI + save logic")
else:
    print("3/4 FAILED")

# 4. Add matching styles (reuse pattern, add G-based styles if not already present)
old4_check = "oemToggleBtn:"
if old4_check not in content:
    old4 = "  card: {"
    new4 = """  oemToggleBtn: {
    flex: 1, paddingVertical: 12, borderRadius: 10,
    alignItems: 'center', borderWidth: 1,
    borderColor: 'rgba(34,197,94,0.2)',
    backgroundColor: 'rgba(34,197,94,0.05)',
  },
  oemToggleBtnActive: { backgroundColor: G, borderColor: G },
  oemToggleText: { fontSize: 12, fontWeight: 'bold', color: 'rgba(255,255,255,0.5)' },
  oemToggleTextActive: { color: '#fff' },
  card: {"""
    if old4 in content:
        content = content.replace(old4, new4, 1)
        changes_made += 1
        print("4/4 Added toggle button styles")
    else:
        print("4/4 FAILED - card anchor not found, styles may need manual addition")
else:
    changes_made += 1
    print("4/4 Styles already present - skipped")

with open(PATH, "w") as f:
    f.write(content)

print(f"\n{changes_made}/4 changes applied.")
