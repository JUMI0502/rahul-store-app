with open('screens/MainStore.js', 'r') as f:
    content = f.read()

start_marker = "// ── BOTTOM NAV ──\nfunction BottomNav"
end_marker = "// ══════════════════════════════════\n// MAIN COMPONENT"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
    removed_char_count = end_idx - start_idx
    content = content[:start_idx] + content[end_idx:]
    with open('screens/MainStore.js', 'w') as f:
        f.write(content)
    print(f"Applied - removed {removed_char_count} characters (4 duplicate component definitions)")
else:
    print(f"FAILED - start_idx={start_idx}, end_idx={end_idx}")
