with open('screens/MainStore.js', 'r') as f:
    content = f.read()

changes = 0

old1 = '''      const r = await fetch(`${API_URL}/products/${stockAdjustProduct.id}/stock`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ stock_qty: parseInt(stockAdjustQty) })
      });'''
new1 = '''      const r = await fetch(`${API_URL}/products/${stockAdjustProduct.id}/stock`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', 'x-staff-session-token': staff?.sessionToken || '' },
        body: JSON.stringify({ stock_qty: parseInt(stockAdjustQty) })
      });'''
if old1 in content:
    content = content.replace(old1, new1, 1)
    changes += 1
    print("1/3: adjustStock now sends session token")
else:
    print("FAILED 1/3")

old2 = '''      await fetch(`${API_URL}/products/${productId}/stock`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ stock_qty: newQty })
      });'''
new2 = '''      await fetch(`${API_URL}/products/${productId}/stock`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', 'x-staff-session-token': staff?.sessionToken || '' },
        body: JSON.stringify({ stock_qty: newQty })
      });'''
if old2 in content:
    content = content.replace(old2, new2, 1)
    changes += 1
    print("2/3: updateStock now sends session token")
else:
    print("FAILED 2/3")

old3 = '''      await fetch(`${API_URL}/products/${productId}/price`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mrp, selling_price: selling })
      });'''
new3 = '''      await fetch(`${API_URL}/products/${productId}/price`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', 'x-staff-session-token': staff?.sessionToken || '' },
        body: JSON.stringify({ mrp, selling_price: selling })
      });'''
if old3 in content:
    content = content.replace(old3, new3, 1)
    changes += 1
    print("3/3: price update now sends session token")
else:
    print("FAILED 3/3")

with open('screens/MainStore.js', 'w') as f:
    f.write(content)

print(f"\n{changes}/3 applied")
