import shutil

PATH = "App.js"

with open(PATH, "r") as f:
    content = f.read()

shutil.copy(PATH, PATH + ".backup4")
print(f"Backup saved to {PATH}.backup4")

old = "  const saved = await AsyncStorage.getItem('staff_profile');"
new = "  const saved = await AsyncStorage.getItem('staff_profile');"

# Find where to insert the global fetch wrapper - right after imports, before component
import re
match = re.search(r"(import[^\n]*\n)+", content)
if match:
    insert_pos = match.end()
    wrapper = """
const API_SECRET_KEY = 'zFWqAraDGYhsNzIe76vXOm0hifitH1bxLmQ6S-8qeN8';
const API_BASE = 'https://rahul-auto-spares-backend.onrender.com';

const originalFetch = global.fetch;
global.fetch = (url, options = {}) => {
  if (typeof url === 'string' && url.startsWith(API_BASE)) {
    options.headers = { ...(options.headers || {}), 'x-api-key': API_SECRET_KEY };
  }
  return originalFetch(url, options);
};
"""
    content = content[:insert_pos] + wrapper + content[insert_pos:]
    with open(PATH, "w") as f:
        f.write(content)
    print("Added global fetch wrapper with API key successfully.")
else:
    print("Could not find import block - no changes made.")
