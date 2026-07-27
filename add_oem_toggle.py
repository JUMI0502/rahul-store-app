import shutil

PATH = "screens/AddProductScreen.js"

with open(PATH, "r") as f:
    content = f.read()

shutil.copy(PATH, PATH + ".backup")
print(f"Backup saved to {PATH}.backup")

changes_made = 0

# 1. Add state
old1 = "  const [stockQty, setStockQty]       = useState('');"
new1 = """  const [stockQty, setStockQty]       = useState('');
  const [isOem, setIsOem]             = useState(false);"""
if old1 in content:
    content = content.replace(old1, new1, 1)
    changes_made += 1
    print("1/3 Added isOem state")
else:
    print("1/3 FAILED")

# 2. Include in save payload
old2 = """        stock_qty:     parseInt(stockQty) || 0,
      };"""
new2 = """        stock_qty:     parseInt(stockQty) || 0,
        is_oem:        isOem,
      };"""
if old2 in content:
    content = content.replace(old2, new2, 1)
    changes_made += 1
    print("2/3 Added is_oem to save payload")
else:
    print("2/3 FAILED")

# 3. Add the toggle UI in Product Details card, after Stock Quantity field
old3 = """          <Text style={s.label}>Stock Quantity</Text>
          <TextInput style={s.input}
            value={stockQty} onChangeText={setStockQty}
            placeholder="0"
            placeholderTextColor="rgba(255,255,255,0.25)"
            keyboardType="numeric" />
        </View>"""
new3 = """          <Text style={s.label}>Stock Quantity</Text>
          <TextInput style={s.input}
            value={stockQty} onChangeText={setStockQty}
            placeholder="0"
            placeholderTextColor="rgba(255,255,255,0.25)"
            keyboardType="numeric" />

          <Text style={s.label}>Part Type</Text>
          <View style={{ flexDirection: 'row', gap: 10 }}>
            <TouchableOpacity
              style={[s.oemToggleBtn, isOem && s.oemToggleBtnActive]}
              onPress={() => setIsOem(true)}>
              <Text style={[s.oemToggleText, isOem && s.oemToggleTextActive]}>Original OEM</Text>
            </TouchableOpacity>
            <TouchableOpacity
              style={[s.oemToggleBtn, !isOem && s.oemToggleBtnActive]}
              onPress={() => setIsOem(false)}>
              <Text style={[s.oemToggleText, !isOem && s.oemToggleTextActive]}>Generic / Compatible</Text>
            </TouchableOpacity>
          </View>
        </View>"""
if old3 in content:
    content = content.replace(old3, new3, 1)
    changes_made += 1
    print("3/3 Added OEM/Generic toggle UI")
else:
    print("3/3 FAILED")

# 4. Add the toggle button styles
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
    print("4/4 FAILED")

with open(PATH, "w") as f:
    f.write(content)

print(f"\n{changes_made}/4 changes applied.")
