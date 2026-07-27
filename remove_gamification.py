import shutil

PATH = "screens/MainStore.js"

with open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

shutil.copy(PATH, PATH + ".backup15")
print(f"Backup saved to {PATH}.backup15")

changes_made = 0

# 1. Remove GoalRing function + its styles entirely (confirmed dead code, never rendered)
old1 = """function GoalRing({ current, target }) {
  const pct = Math.round(Math.min(current / target, 1) * 100);
  const scaleAnim = useRef(new Animated.Value(0.8)).current;
  useEffect(() => {
    Animated.spring(scaleAnim, { toValue: 1, tension: 50, friction: 7, useNativeDriver: true }).start();
  }, [current]);
  return (
    <Animated.View style={[gr.container, { transform: [{ scale: scaleAnim }] }]}>
      <View style={gr.left}>
        <Text style={gr.title}>🎯 Daily Goal</Text>
        <View style={gr.ring}>
          <View style={gr.ringBg} />
          <View style={[gr.ringFill, {
            borderTopColor: pct > 25 ? G : 'transparent',
            borderRightColor: pct > 50 ? G : 'transparent',
            borderBottomColor: pct > 75 ? G : 'transparent',
            borderLeftColor: pct > 0 ? G : 'transparent',
          }]} />
          <View style={gr.ringCenter}>
            <Text style={gr.ringPct}>{pct}%</Text>
            <Text style={gr.ringLabel}>done</Text>
          </View>
        </View>
      </View>
      <View style={gr.right}>
        {[
          { label: 'Earned', value: `₹${current >= 1000 ? (current/1000).toFixed(1)+'k' : current.toFixed(0)}`, color: G },
          { label: 'Target', value: `₹${(target/1000).toFixed(0)}k`, color: '#fff' },
          { label: 'Left', value: `₹${Math.max(0,target-current) >= 1000 ? ((Math.max(0,target-current))/1000).toFixed(1)+'k' : Math.max(0,target-current).toFixed(0)}`, color: '#F59E0B' },
        ].map((r, i) => (
          <View key={i} style={gr.statRow}>
            <Text style={gr.statLabel}>{r.label}</Text>
            <Text style={[gr.statVal, { color: r.color }]}>{r.value}</Text>
          </View>
        ))}
        {pct >= 100 && (
          <View style={gr.metBadge}><Text style={gr.metText}>🎉 Goal Met!</Text></View>
        )}
      </View>
    </Animated.View>
  );
}
const gr = StyleSheet.create({
  container: {
    backgroundColor: '#0D1A0D', borderRadius: 20, padding: 16,
    flexDirection: 'row', gap: 16, alignItems: 'center',
    marginBottom: 12, borderWidth: 1, borderColor: 'rgba(34,197,94,0.25)',
  },
  left: { alignItems: 'center' },
  title: { fontSize: 12, fontWeight: 'bold', color: '#fff', marginBottom: 10 },
  ring: { width: 90, height: 90, position: 'relative', alignItems: 'center', justifyContent: 'center' },
  ringBg: { position: 'absolute', width: 90, height: 90, borderRadius: 45, borderWidth: 8, borderColor: 'rgba(34,197,94,0.15)' },
  ringFill: { position: 'absolute', width: 90, height: 90, borderRadius: 45, borderWidth: 8, borderTopColor: G, borderRightColor: G, borderBottomColor: G, borderLeftColor: G },
  ringCenter: { alignItems: 'center' },
  ringPct: { fontSize: 20, fontWeight: 'bold', color: G },
  ringLabel: { fontSize: 9, color: 'rgba(255,255,255,0.4)' },
  right: { flex: 1, gap: 8 },
  statRow: { flexDirection: 'row', justifyContent: 'space-between', paddingBottom: 8, borderBottomWidth: 1, borderBottomColor: 'rgba(34,197,94,0.08)' },
  statLabel: { fontSize: 12, color: 'rgba(255,255,255,0.4)' },
  statVal: { fontSize: 14, fontWeight: 'bold', color: '#fff' },
  metBadge: { backgroundColor: 'rgba(34,197,94,0.15)', borderRadius: 10, padding: 8, alignItems: 'center', borderWidth: 1, borderColor: 'rgba(34,197,94,0.3)' },
  metText: { color: G, fontWeight: 'bold', fontSize: 13 },
});

// ── STAFF LEADERBOARD ──
"""
if old1 in content:
    content = content.replace(old1, "", 1)
    changes_made += 1
    print("1/3 Removed GoalRing (dead code)")
else:
    print("1/3 FAILED")

# 2. Remove StaffLeaderboard function + its styles entirely
old2 = """function StaffLeaderboard({ orders }) {
  const staffScores = {};
  orders.forEach(order => {
    if (order.collected_by && typeof order.collected_by === 'string') {
      const name = order.collected_by.split(' ')[0];
      if (!staffScores[name]) staffScores[name] = { orders: 0, revenue: 0 };
      staffScores[name].orders++;
      staffScores[name].revenue += parseFloat(order.total_amount || 0);
    }
    if (order.packed_by && typeof order.packed_by === 'string' && order.packed_by !== order.collected_by) {
      const name = order.packed_by.split(' ')[0];
      if (!staffScores[name]) staffScores[name] = { orders: 0, revenue: 0 };
      staffScores[name].orders += 0.5;
    }
  });
  const ranked = Object.entries(staffScores)
    .map(([name, data]) => ({ name, ...data }))
    .sort((a, b) => b.orders - a.orders).slice(0, 5);
  if (ranked.length === 0) return null;
  const medals = ['🥇','🥈','🥉','4️⃣','5️⃣'];
  const medalColors = ['#FFC107','#9CA3AF','#CD7C3E','#fff','#fff'];
  const maxOrders = ranked[0]?.orders || 1;
  return (
    <View style={lb.container}>
      <View style={lb.headerRow}>
        <Text style={lb.title}>🏅 Staff Leaderboard</Text>
        <Text style={lb.sub}>This Month</Text>
      </View>
      {ranked.map((staff, i) => (
        <View key={staff.name} style={lb.row}>
          <Text style={[lb.medal, { color: medalColors[i] }]}>{medals[i]}</Text>
          <View style={{ flex: 1 }}>
            <View style={lb.rowTop}>
              <Text style={[lb.name, i===0&&{color:'#FFC107'}]}>{staff.name}</Text>
              <Text style={lb.orders}>{Math.floor(staff.orders)} orders</Text>
            </View>
            <View style={lb.barBg}>
              <View style={[lb.barFill, { width: `${(staff.orders/maxOrders)*100}%`, backgroundColor: i===0?'#FFC107':G }]} />
            </View>
            <Text style={lb.revenue}>₹{staff.revenue.toFixed(0)} revenue</Text>
          </View>
        </View>
      ))}
    </View>
  );
}
const lb = StyleSheet.create({
  container: { backgroundColor: '#0D1A0D', borderRadius: 16, padding: 16, marginBottom: 12, borderWidth: 1, borderColor: 'rgba(34,197,94,0.15)' },
  headerRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 14 },
  title: { fontSize: 14, fontWeight: 'bold', color: '#fff' },
  sub: { fontSize: 11, color: 'rgba(255,255,255,0.3)' },
  row: { flexDirection: 'row', alignItems: 'center', gap: 10, marginBottom: 14 },
  medal: { fontSize: 22, width: 30 },
  rowTop: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 6 },
  name: { fontSize: 14, fontWeight: 'bold', color: '#fff' },
  orders: { fontSize: 12, color: G, fontWeight: 'bold' },
  barBg: { height: 6, backgroundColor: 'rgba(34,197,94,0.1)', borderRadius: 3, overflow: 'hidden', marginBottom: 4 },
  barFill: { height: '100%', borderRadius: 3 },
  revenue: { fontSize: 10, color: 'rgba(255,255,255,0.35)' },
});

"""
if old2 in content:
    content = content.replace(old2, "", 1)
    changes_made += 1
    print("2/3 Removed StaffLeaderboard")
else:
    print("2/3 FAILED")

# 3. Remove the render call site
old3 = "            <StaffLeaderboard orders={orders} />\n\n"
if old3 in content:
    content = content.replace(old3, "", 1)
    changes_made += 1
    print("3/3 Removed StaffLeaderboard render call")
else:
    print("3/3 FAILED")

with open(PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\n{changes_made}/3 changes applied.")
