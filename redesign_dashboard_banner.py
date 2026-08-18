with open('screens/MainStore.js', 'r') as f:
    content = f.read()

old = '''            {/* OWNER DASHBOARD BANNER */}
            {isOwner && (
              <View style={s.dashBanner}>
                <TouchableOpacity style={s.dashCard} onPress={() => setShowDashboard(true)}>
                  <View style={s.dashItem}>
                    <Text style={s.dashValue}>₹{(todayRevenue/1000).toFixed(1)}k</Text>
                    <Text style={s.dashLabel}>Today</Text>
                  </View>
                  <View style={s.dashDivider}/>
                  <View style={s.dashItem}>
                    <Text style={s.dashValue}>{todayOrders}</Text>
                    <Text style={s.dashLabel}>Orders</Text>
                  </View>
                  <View style={s.dashDivider}/>
                  <View style={s.dashItem}>
                    <Text style={[s.dashValue, { color: '#EF4444' }]}>{lowStockProducts.length}</Text>
                    <Text style={s.dashLabel}>Low Stock</Text>
                  </View>
                  <View style={s.dashDivider}/>
                  <View style={s.dashItem}>
                    <Text style={[s.dashValue, { color: '#F59E0B' }]}>
                      {orders.filter(o => o.status !== 'collected').length}
                    </Text>
                    <Text style={s.dashLabel}>Pending</Text>
                  </View>
                </TouchableOpacity>
                <View style={s.dashActions}>
                  <TouchableOpacity style={s.cashRegBtn} onPress={() => setShowCashRegister(true)}>
                    <Ionicons name="cash-outline" size={16} color="#C9A84C" />
                    <Text style={s.cashRegBtnText}>Cash Sale</Text>
                  </TouchableOpacity>
                  <TouchableOpacity style={s.reportBtn} onPress={sendDailyReport}>
                    <Ionicons name="logo-whatsapp" size={16} color="#25D366" />
                    <Text style={s.reportBtnText}>Report</Text>
                  </TouchableOpacity>
                </View>
              </View>
            )}'''

new = '''            {/* OWNER DASHBOARD BANNER */}
            {isOwner && (
              <View style={s.dashBanner}>
                <TouchableOpacity activeOpacity={0.85} onPress={() => setShowDashboard(true)}>
                  <View style={s.dashStatsRow}>
                    <StatCard icon="cash-outline" label="Today" value={`\u20b9${(todayRevenue/1000).toFixed(1)}k`} color="#C9A84C" />
                    <StatCard icon="receipt-outline" label="Orders" value={todayOrders} color="#4ADE80" />
                  </View>
                  <View style={s.dashStatsRow}>
                    <StatCard icon="alert-circle-outline" label="Low Stock" value={lowStockProducts.length} color="#EF4444" />
                    <StatCard icon="time-outline" label="Pending" value={orders.filter(o => o.status !== 'collected').length} color="#F59E0B" />
                  </View>
                </TouchableOpacity>
                <View style={s.dashActions}>
                  <TouchableOpacity style={s.cashRegBtn} onPress={() => setShowCashRegister(true)}>
                    <Ionicons name="cash-outline" size={16} color="#C9A84C" />
                    <Text style={s.cashRegBtnText}>Cash Sale</Text>
                  </TouchableOpacity>
                  <TouchableOpacity style={s.reportBtn} onPress={sendDailyReport}>
                    <Ionicons name="logo-whatsapp" size={16} color="#25D366" />
                    <Text style={s.reportBtnText}>Report</Text>
                  </TouchableOpacity>
                </View>
              </View>
            )}'''

if old in content:
    content = content.replace(old, new, 1)
    with open('screens/MainStore.js', 'w') as f:
        f.write(content)
    print("Applied - dashboard now uses rich StatCard tiles with icons and color coding")
else:
    print("Anchor not found")
