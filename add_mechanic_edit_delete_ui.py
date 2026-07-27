import shutil

PATH = "screens/MainStore.js"

with open(PATH, "r") as f:
    content = f.read()

shutil.copy(PATH, PATH + ".backup12")
print(f"Backup saved to {PATH}.backup12")

changes_made = 0

# 1. Add edit-mode state
old = "  const [loadingMechanics, setLoadingMechanics] = useState(false);"
new = """  const [loadingMechanics, setLoadingMechanics] = useState(false);
  const [editingMechanicId, setEditingMechanicId] = useState(null);
  const [editMechanicName, setEditMechanicName] = useState('');
  const [editMechanicPhone, setEditMechanicPhone] = useState('');
  const [editMechanicShop, setEditMechanicShop] = useState('');
  const [editMechanicArea, setEditMechanicArea] = useState('');"""

if old in content:
    content = content.replace(old, new, 1)
    changes_made += 1
    print("1/4 Added edit state")
else:
    print("1/4 FAILED")

# 2. Add update/delete functions
old2 = "  const respondToMechanic = async (id, status) => {"
new2 = """  const updateMechanic = async (id) => {
    try {
      const r = await fetch(`${API_URL}/mechanics/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: editMechanicName,
          phone: editMechanicPhone,
          shop_name: editMechanicShop,
          area: editMechanicArea
        })
      });
      if (!r.ok) throw new Error('failed');
      setEditingMechanicId(null);
      Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success);
      fetchMechanics();
    } catch {
      Alert.alert('Error', 'Could not update mechanic');
    }
  };

  const deleteMechanic = (id, name) => {
    Alert.alert('Delete Mechanic?', `Remove ${name} permanently?`, [
      { text: 'Cancel', style: 'cancel' },
      { text: 'Delete', style: 'destructive', onPress: async () => {
        try {
          const r = await fetch(`${API_URL}/mechanics/${id}`, { method: 'DELETE' });
          if (!r.ok) throw new Error('failed');
          Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success);
          fetchMechanics();
        } catch {
          Alert.alert('Error', 'Could not delete mechanic');
        }
      }}
    ]);
  };

  const respondToMechanic = async (id, status) => {"""

if old2 in content:
    content = content.replace(old2, new2, 1)
    changes_made += 1
    print("2/4 Added functions")
else:
    print("2/4 FAILED")

# 3. Replace the card rendering to support edit mode + add edit/delete icons
old3 = '''              mechanics.map(m => (
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
              ))'''

new3 = '''              mechanics.map(m => (
                <View key={m.id} style={s.detailCard}>
                  {editingMechanicId === m.id ? (
                    <>
                      <TextInput style={s.input} value={editMechanicName} onChangeText={setEditMechanicName} placeholder="Name" placeholderTextColor="rgba(255,255,255,0.3)" />
                      <TextInput style={s.input} value={editMechanicPhone} onChangeText={setEditMechanicPhone} placeholder="Phone" placeholderTextColor="rgba(255,255,255,0.3)" />
                      <TextInput style={s.input} value={editMechanicShop} onChangeText={setEditMechanicShop} placeholder="Shop Name" placeholderTextColor="rgba(255,255,255,0.3)" />
                      <TextInput style={s.input} value={editMechanicArea} onChangeText={setEditMechanicArea} placeholder="Area" placeholderTextColor="rgba(255,255,255,0.3)" />
                      <View style={{ flexDirection: 'row', gap: 10, marginTop: 12 }}>
                        <TouchableOpacity style={{ flex: 1, backgroundColor: G, borderRadius: 10, padding: 12, alignItems: 'center' }}
                          onPress={() => updateMechanic(m.id)}>
                          <Text style={{ color: '#060E06', fontWeight: '700' }}>Save</Text>
                        </TouchableOpacity>
                        <TouchableOpacity style={{ flex: 1, backgroundColor: 'rgba(255,255,255,0.08)', borderRadius: 10, padding: 12, alignItems: 'center' }}
                          onPress={() => setEditingMechanicId(null)}>
                          <Text style={{ color: '#fff', fontWeight: '700' }}>Cancel</Text>
                        </TouchableOpacity>
                      </View>
                    </>
                  ) : (
                    <>
                      <View style={{ flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' }}>
                        <Text style={s.addRewardFormTitle}>{m.name}</Text>
                        <View style={{ flexDirection: 'row', gap: 14 }}>
                          <TouchableOpacity onPress={() => {
                            setEditingMechanicId(m.id);
                            setEditMechanicName(m.name);
                            setEditMechanicPhone(m.phone);
                            setEditMechanicShop(m.shop_name || '');
                            setEditMechanicArea(m.area || '');
                          }}>
                            <Ionicons name="create-outline" size={20} color="#4F6EF7" />
                          </TouchableOpacity>
                          <TouchableOpacity onPress={() => deleteMechanic(m.id, m.name)}>
                            <Ionicons name="trash-outline" size={20} color="#EF4444" />
                          </TouchableOpacity>
                        </View>
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
                    </>
                  )}
                </View>
              ))'''

if old3 in content:
    content = content.replace(old3, new3, 1)
    changes_made += 1
    print("3/4 Replaced card rendering with edit/delete support")
else:
    print("3/4 FAILED - anchor not found")

with open(PATH, "w") as f:
    f.write(content)

print(f"\n{changes_made}/3 changes applied.")
