import shutil

PATH = "screens/MainStore.js"

with open(PATH, "r") as f:
    content = f.read()

shutil.copy(PATH, PATH + ".backup11")
print(f"Backup saved to {PATH}.backup11")

changes_made = 0

# 1. State
old = "  const [showStaffManager, setShowStaffManager] = useState(false);"
new = """  const [showStaffManager, setShowStaffManager] = useState(false);
  const [showMechanicApprovals, setShowMechanicApprovals] = useState(false);
  const [mechanics, setMechanics] = useState([]);
  const [mechanicsPendingCount, setMechanicsPendingCount] = useState(0);
  const [loadingMechanics, setLoadingMechanics] = useState(false);"""

if old in content:
    content = content.replace(old, new, 1)
    changes_made += 1
    print("1/6 Added state")
else:
    print("1/6 FAILED - anchor not found")

# 2. Fetch/approve functions - anchor near fetchAllStaff
old2 = "  const addNewStaff = async () => {"
new2 = """  const fetchMechanics = async () => {
    setLoadingMechanics(true);
    try {
      const r = await fetch(`${API_URL}/mechanics`);
      const d = await r.json();
      setMechanics(d.mechanics || []);
      setMechanicsPendingCount(d.pending || 0);
    } catch { setMechanics([]); }
    setLoadingMechanics(false);
  };

  const respondToMechanic = async (id, status) => {
    try {
      const r = await fetch(`${API_URL}/mechanics/${id}/approve`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status, approved_by: staff?.name })
      });
      if (!r.ok) throw new Error('failed');
      Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success);
      fetchMechanics();
    } catch {
      Alert.alert('Error', 'Could not update mechanic status');
    }
  };

  const addNewStaff = async () => {"""

if old2 in content:
    content = content.replace(old2, new2, 1)
    changes_made += 1
    print("2/6 Added functions")
else:
    print("2/6 FAILED - anchor not found")

# 3. Button in Reports tab, right after Staff Manager button
old3 = """                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {/* ACTIVITY LOG */}"""

new3 = """                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {/* MECHANIC APPROVALS */}
            {(isOwner || isSenior) && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => { fetchMechanics(); setShowMechanicApprovals(true); }}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="construct" size={22} color="#F59E0B" />
                  <View>
                    <Text style={s.customerHistoryBtnTitle}>Mechanic Approvals</Text>
                    <Text style={s.customerHistoryBtnSub}>
                      {mechanicsPendingCount > 0 ? `${mechanicsPendingCount} pending request(s)` : 'Review mechanic access requests'}
                    </Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {/* ACTIVITY LOG */}"""

if old3 in content:
    content = content.replace(old3, new3, 1)
    changes_made += 1
    print("3/6 Added button")
else:
    print("3/6 FAILED - anchor not found")

# 4. The modal itself - insert right before Staff Manager modal
old4 = "      <Modal visible={showStaffManager} animationType=\"slide\""
new4 = """      <Modal visible={showMechanicApprovals} animationType="slide"
        onRequestClose={() => setShowMechanicApprovals(false)}>
        <SafeAreaView style={[s.container]}>
          <StatusBar barStyle="light-content" />
          <View style={s.rewardsHeader}>
            <TouchableOpacity onPress={() => setShowMechanicApprovals(false)}>
              <Ionicons name="arrow-back" size={22} color="#fff" />
            </TouchableOpacity>
            <Text style={s.rewardsHeaderTitle}>Mechanic Approvals</Text>
          </View>
          <ScrollView contentContainerStyle={{ padding: 16 }}>
            {loadingMechanics ? (
              <Text style={{ color: 'rgba(255,255,255,0.4)', textAlign: 'center', marginTop: 30 }}>Loading...</Text>
            ) : mechanics.length === 0 ? (
              <Text style={{ color: 'rgba(255,255,255,0.4)', textAlign: 'center', marginTop: 30 }}>No mechanic requests yet.</Text>
            ) : (
              mechanics.map(m => (
                <View key={m.id} style={s.detailCard}>
                  <View style={s.detailRow}>
                    <Text style={s.detailLabel}>Name</Text>
                    <Text style={s.detailValue}>{m.name}</Text>
                  </View>
                  <View style={s.detailRow}>
                    <Text style={s.detailLabel}>Phone</Text>
                    <Text style={s.detailValue}>{m.phone}</Text>
                  </View>
                  {m.shop_name ? (
                    <View style={s.detailRow}>
                      <Text style={s.detailLabel}>Shop</Text>
                      <Text style={s.detailValue}>{m.shop_name}</Text>
                    </View>
                  ) : null}
                  {m.area ? (
                    <View style={s.detailRow}>
                      <Text style={s.detailLabel}>Area</Text>
                      <Text style={s.detailValue}>{m.area}</Text>
                    </View>
                  ) : null}
                  <View style={[s.detailRow, { borderBottomWidth: 0 }]}>
                    <Text style={s.detailLabel}>Status</Text>
                    <Text style={[s.detailValue, {
                      color: m.status === 'approved' ? G : m.status === 'rejected' ? '#EF4444' : '#F59E0B'
                    }]}>{m.status.toUpperCase()}</Text>
                  </View>
                  {m.status === 'pending' && (
                    <View style={{ flexDirection: 'row', gap: 10, marginTop: 12 }}>
                      <TouchableOpacity
                        style={{ flex: 1, backgroundColor: G, borderRadius: 10, padding: 12, alignItems: 'center' }}
                        onPress={() => respondToMechanic(m.id, 'approved')}>
                        <Text style={{ color: '#060E06', fontWeight: '700' }}>Approve</Text>
                      </TouchableOpacity>
                      <TouchableOpacity
                        style={{ flex: 1, backgroundColor: 'rgba(239,68,68,0.15)', borderRadius: 10, padding: 12, alignItems: 'center', borderWidth: 1, borderColor: '#EF4444' }}
                        onPress={() => respondToMechanic(m.id, 'rejected')}>
                        <Text style={{ color: '#EF4444', fontWeight: '700' }}>Reject</Text>
                      </TouchableOpacity>
                    </View>
                  )}
                </View>
              ))
            )}
          </ScrollView>
        </SafeAreaView>
      </Modal>

      <Modal visible={showStaffManager} animationType="slide\""""

if old4 in content:
    content = content.replace(old4, new4, 1)
    changes_made += 1
    print("4/6 Added modal")
else:
    print("4/6 FAILED - anchor not found")

with open(PATH, "w") as f:
    f.write(content)

print(f"\n{changes_made}/4 changes applied.")
