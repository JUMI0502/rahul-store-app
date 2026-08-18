import shutil

PATH = "screens/QRScannerScreen.js"

with open(PATH, "r") as f:
    content = f.read()

shutil.copy(PATH, PATH + ".backup")
print(f"Backup saved to {PATH}.backup")

changes_made = 0

old1 = "export default function QRScannerScreen({ onScanned, onClose }) {"
new1 = "export default function QRScannerScreen({ onScanned, onClose, mode = 'order' }) {"
if old1 in content:
    content = content.replace(old1, new1, 1)
    changes_made += 1
    print("1/3 Made mode a prop")
else:
    print("1/3 FAILED")

old2 = """        <Text style={s.headerTitle}>Scan Order QR</Text>"""
new2 = """        <Text style={s.headerTitle}>{mode === 'product' ? 'Scan Product Barcode' : 'Scan Order QR'}</Text>"""
if old2 in content:
    content = content.replace(old2, new2, 1)
    changes_made += 1
    print("2/3 Made header title mode-aware")
else:
    print("2/3 FAILED")

old3 = """          barcodeScannerSettings={{ barcodeTypes: ['qr'] }}"""
new3 = """          barcodeScannerSettings={{ barcodeTypes: mode === 'product' ? ['ean13', 'ean8', 'upc_a', 'upc_e', 'code128', 'qr'] : ['qr'] }}"""
if old3 in content:
    content = content.replace(old3, new3, 1)
    changes_made += 1
    print("3/3 Made barcode types mode-aware")
else:
    print("3/3 FAILED")

with open(PATH, "w") as f:
    f.write(content)

print(f"\n{changes_made}/3 changes applied.")
