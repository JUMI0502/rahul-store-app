changes = 0

# 1. MainStore.js - pass staff down to AddProductScreen
with open('screens/MainStore.js', 'r') as f:
    content = f.read()

old1 = '''    <AddProductScreen
      onBack={() => setShowAddProduct(false)}
      onProductAdded={() => { fetchProducts(); setShowAddProduct(false); }}
    />'''
new1 = '''    <AddProductScreen
      onBack={() => setShowAddProduct(false)}
      onProductAdded={() => { fetchProducts(); setShowAddProduct(false); }}
      staff={staff}
    />'''
if old1 in content:
    content = content.replace(old1, new1, 1)
    changes += 1
    print("1/4: MainStore now passes staff to AddProductScreen")
else:
    print("FAILED 1/4")

old2 = '''                    await fetch(`${API_URL}/products/${stockAdjustProduct.id}/oem`, {
                      method: 'PUT',
                      headers: { 'Content-Type': 'application/json' },
                      body: JSON.stringify({ is_oem: stockAdjustIsOem })
                    });'''
new2 = '''                    await fetch(`${API_URL}/products/${stockAdjustProduct.id}/oem`, {
                      method: 'PUT',
                      headers: { 'Content-Type': 'application/json', 'x-staff-session-token': staff?.sessionToken || '' },
                      body: JSON.stringify({ is_oem: stockAdjustIsOem })
                    });'''
if old2 in content:
    content = content.replace(old2, new2, 1)
    changes += 1
    print("2/4: OEM toggle now sends session token")
else:
    print("FAILED 2/4")

with open('screens/MainStore.js', 'w') as f:
    f.write(content)

# 2. AddProductScreen.js - accept staff prop, send it on both calls
with open('screens/AddProductScreen.js', 'r') as f:
    content2 = f.read()

old3 = '''export default function AddProductScreen({ onBack, onProductAdded }) {'''
new3 = '''export default function AddProductScreen({ onBack, onProductAdded, staff }) {'''
if old3 in content2:
    content2 = content2.replace(old3, new3, 1)
    changes += 1
    print("3/4: AddProductScreen now accepts staff prop")
else:
    print("FAILED 3/4")

old4 = '''      const r = await fetch(`${API_URL}/products`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });'''
new4 = '''      const r = await fetch(`${API_URL}/products`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'x-staff-session-token': staff?.sessionToken || '' },
        body: JSON.stringify(payload),
      });'''
if old4 in content2:
    content2 = content2.replace(old4, new4, 1)
    changes += 1
    print("4/5: add_product call now sends session token")
else:
    print("FAILED 4/5")

old5 = '''          await fetch(`${API_URL}/products/${productId}/upload-image`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ image_base64: imageBase64 }),
          });'''
new5 = '''          await fetch(`${API_URL}/products/${productId}/upload-image`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'x-staff-session-token': staff?.sessionToken || '' },
            body: JSON.stringify({ image_base64: imageBase64 }),
          });'''
if old5 in content2:
    content2 = content2.replace(old5, new5, 1)
    changes += 1
    print("5/5: image upload call now sends session token")
else:
    print("FAILED 5/5")

with open('screens/AddProductScreen.js', 'w') as f:
    f.write(content2)

print(f"\n{changes}/5 applied")
