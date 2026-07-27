import shutil

PATH = "App.js"

with open(PATH, "r") as f:
    content = f.read()

shutil.copy(PATH, PATH + ".backup3")
print(f"Backup saved to {PATH}.backup3")

# Remove duplicate NativeModules import lines - keep only the first
import_line = "import { NativeModules } from 'react-native';\n"
count = content.count(import_line)
print(f"Found {count} NativeModules import lines")
if count > 1:
    first_idx = content.find(import_line)
    before = content[:first_idx + len(import_line)]
    after = content[first_idx + len(import_line):]
    after = after.replace(import_line, "")
    content = before + after
    print(f"Removed {count - 1} duplicate import lines")

# Remove duplicate startOrderAlertListener function blocks - keep only the first
func_block = """function startOrderAlertListener() {
  Notifications.addNotificationReceivedListener((notification) => {
    const data = notification.request?.content?.data;
    const body = notification.request?.content?.body || '';
    if (data?.type === 'new_order' && NativeModules.OrderAlertModule) {
      const amountMatch = body.match(/Rs\\.?\\s*([0-9,.]+)/);
      const amount = amountMatch ? amountMatch[1] : '';
      NativeModules.OrderAlertModule.showOrderAlert(
        data.custom_id || 'New Order',
        amount
      );
    }
  });
}

"""

func_count = content.count(func_block)
print(f"Found {func_count} startOrderAlertListener function blocks")
if func_count > 1:
    first_idx = content.find(func_block)
    before = content[:first_idx + len(func_block)]
    after = content[first_idx + len(func_block):]
    after = after.replace(func_block, "")
    content = before + after
    print(f"Removed {func_count - 1} duplicate function blocks")

with open(PATH, "w") as f:
    f.write(content)

print("Cleanup complete.")
