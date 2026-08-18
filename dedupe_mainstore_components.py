with open('screens/MainStore.js', 'r') as f:
    content = f.read()

changes = 0

# 1. Add imports for the 4 new components, right after the existing screen imports
old1 = """import SalesDashboardScreen from './SalesDashboardScreen';
import { generateInvoice, shareInvoice } from '../utils/invoice';"""
new1 = """import SalesDashboardScreen from './SalesDashboardScreen';
import { generateInvoice, shareInvoice } from '../utils/invoice';
import BottomNav from '../components/BottomNav';
import StatCard from '../components/StatCard';
import AvatarRing from '../components/AvatarRing';
import AvatarPickerModal from '../components/AvatarPickerModal';"""
if old1 in content:
    content = content.replace(old1, new1, 1)
    changes += 1
    print("1/6: imports added")
else:
    print("FAILED 1/6")

# 2. Remove the AVATAR_OPTIONS constant (moved into AvatarPickerModal.js)
start2 = "const AVATAR_OPTIONS = ["
end2 = "\n];\n"
idx2 = content.find(start2)
if idx2 != -1:
    end_idx2 = content.find(end2, idx2) + len(end2)
    content = content[:idx2] + content[end_idx2:]
    changes += 1
    print("2/6: AVATAR_OPTIONS constant removed (now lives in AvatarPickerModal.js)")
else:
    print("FAILED 2/6")

with open('screens/MainStore.js', 'w') as f:
    f.write(content)

print(f"\n{changes}/2 applied so far - continuing with function removals next")
