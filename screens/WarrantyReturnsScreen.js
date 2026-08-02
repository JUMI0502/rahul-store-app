import { useState, useEffect } from 'react';
import {
  StyleSheet, Text, View, TouchableOpacity,
  SafeAreaView, StatusBar, ScrollView, TextInput,
  ActivityIndicator, RefreshControl, Alert
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import * as Haptics from 'expo-haptics';

const API_URL = 'https://rahul-auto-spares-backend.onrender.com';
const G = '#C9A84C';

const STATUS_COLORS = { pending: '#F59E0B', resolved: 'G', rejected: '#EF4444' };

export default function WarrantyReturnsScreen({ onBack, staff }) {
  const [claims, setClaims] = useState([]);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [filter, setFilter] = useState('pending');
  const [showNewForm, setShowNewForm] = useState(false);
  const [resolvingClaim, setResolvingClaim] = useState(null);

  const [orderId, setOrderId] = useState('');
  const [productName, setProductName] = useState('');
  const [customerName, setCustomerName] = useState('');
  const [customerPhone, setCustomerPhone] = useState('');
  const [issueDescription, setIssueDescription] = useState('');

  const [resolutionType, setResolutionType] = useState('replaced');
  const [resolutionNotes, setResolutionNotes] = useState('');

  useEffect(() => { fetchClaims(); }, [filter]);

  const fetchClaims = async () => {
    try {
      const statusParam = filter === 'all' ? '' : `?status=${filter}`;
      const r = await fetch(`${API_URL}/warranty-claims${statusParam}`);
      const d = await r.json();
      setClaims(d.claims || []);
    } catch {
      setClaims([]);
    }
    setLoading(false);
  };

  const onRefresh = async () => {
    setRefreshing(true);
    await fetchClaims();
    setRefreshing(false);
  };

  const submitClaim = async () => {
    if (!customerName.trim() || !productName.trim() || !issueDescription.trim()) {
      Alert.alert('Missing info', 'Please fill in customer name, product, and issue description.');
      return;
    }
    try {
      const r = await fetch(`${API_URL}/warranty-claims`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          order_id: orderId ? parseInt(orderId) : null,
          product_name: productName.trim(),
          customer_name: customerName.trim(),
          customer_phone: customerPhone.trim(),
          issue_description: issueDescription.trim()
        })
      });
      if (!r.ok) throw new Error('failed');
      Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success);
      setOrderId(''); setProductName(''); setCustomerName('');
      setCustomerPhone(''); setIssueDescription('');
      setShowNewForm(false);
      setFilter('pending');
      fetchClaims();
    } catch {
      Alert.alert('Error', 'Could not log claim');
    }
  };

  const resolveClaim = async (claimId) => {
    try {
      const r = await fetch(`${API_URL}/warranty-claims/${claimId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          status: 'resolved',
          resolution_type: resolutionType,
          resolution_notes: resolutionNotes.trim(),
          resolved_by: staff?.name || 'Staff'
        })
      });
      if (!r.ok) throw new Error('failed');
      Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success);
      setResolvingClaim(null);
      setResolutionNotes('');
      fetchClaims();
    } catch {
      Alert.alert('Error', 'Could not update claim');
    }
  };

  const rejectClaim = async (claimId) => {
    Alert.alert('Reject Claim?', 'This marks the claim as not covered/rejected.', [
      { text: 'Cancel', style: 'cancel' },
      { text: 'Reject', style: 'destructive', onPress: async () => {
        try {
          await fetch(`${API_URL}/warranty-claims/${claimId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ status: 'rejected', resolved_by: staff?.name || 'Staff' })
          });
          fetchClaims();
        } catch {
          Alert.alert('Error', 'Could not update claim');
        }
      }}
    ]);
  };

  if (showNewForm) return (
    <SafeAreaView style={s.container}>
      <StatusBar barStyle="light-content" backgroundColor="#060E06" />
      <View style={s.header}>
        <TouchableOpacity style={s.backBtn} onPress={() => setShowNewForm(false)}>
          <Ionicons name="arrow-back" size={16} color={G} />
        </TouchableOpacity>
        <Text style={s.headerTitle}>New Claim</Text>
      </View>
      <ScrollView contentContainerStyle={{ padding: 16 }}>
        <Text style={s.label}>Order ID (optional)</Text>
        <TextInput style={s.input} value={orderId} onChangeText={setOrderId}
          placeholder="e.g. 42" placeholderTextColor="rgba(255,255,255,0.25)" keyboardType="numeric" />

        <Text style={s.label}>Product / Part *</Text>
        <TextInput style={s.input} value={productName} onChangeText={setProductName}
          placeholder="e.g. Brake Shoe - Hero Splendor" placeholderTextColor="rgba(255,255,255,0.25)" />

        <Text style={s.label}>Customer Name *</Text>
        <TextInput style={s.input} value={customerName} onChangeText={setCustomerName}
          placeholder="Customer name" placeholderTextColor="rgba(255,255,255,0.25)" />

        <Text style={s.label}>Customer Phone</Text>
        <TextInput style={s.input} value={customerPhone} onChangeText={setCustomerPhone}
          placeholder="10-digit number" placeholderTextColor="rgba(255,255,255,0.25)" keyboardType="phone-pad" />

        <Text style={s.label}>Issue Description *</Text>
        <TextInput style={[s.input, { height: 90, textAlignVertical: 'top' }]} value={issueDescription}
          onChangeText={setIssueDescription} placeholder="What's wrong with the part?"
          placeholderTextColor="rgba(255,255,255,0.25)" multiline />

        <TouchableOpacity style={s.saveBtn} onPress={submitClaim}>
          <Text style={s.saveBtnText}>Log Claim</Text>
        </TouchableOpacity>
      </ScrollView>
    </SafeAreaView>
  );

  return (
    <SafeAreaView style={s.container}>
      <StatusBar barStyle="light-content" backgroundColor="#060E06" />
      <View style={s.header}>
        <TouchableOpacity style={s.backBtn} onPress={onBack}>
          <Ionicons name="arrow-back" size={16} color={G} />
        </TouchableOpacity>
        <View style={{ flex: 1 }}>
          <Text style={s.headerTitle}>Warranty & Returns</Text>
          <Text style={s.headerSub}>Track defect claims and resolutions</Text>
        </View>
        <TouchableOpacity style={s.newBtn} onPress={() => setShowNewForm(true)}>
          <Ionicons name="add" size={20} color="#060E06" />
        </TouchableOpacity>
      </View>

      <View style={s.filterRow}>
        {['pending', 'resolved', 'rejected', 'all'].map(f => (
          <TouchableOpacity key={f}
            style={[s.filterChip, filter === f && s.filterChipActive]}
            onPress={() => setFilter(f)}>
            <Text style={[s.filterChipText, filter === f && s.filterChipTextActive]}>
              {f.charAt(0).toUpperCase() + f.slice(1)}
            </Text>
          </TouchableOpacity>
        ))}
      </View>

      {loading ? (
        <View style={s.centerBox}><ActivityIndicator color={G} /></View>
      ) : claims.length === 0 ? (
        <View style={s.centerBox}>
          <Ionicons name="shield-checkmark-outline" size={48} color="rgba(255,255,255,0.2)" />
          <Text style={s.emptyText}>No {filter !== 'all' ? filter : ''} claims</Text>
        </View>
      ) : (
        <ScrollView contentContainerStyle={{ padding: 14 }}
          refreshControl={<RefreshControl refreshing={refreshing} onRefresh={onRefresh} tintColor={G} />}>
          {claims.map(claim => (
            <View key={claim.id} style={s.card}>
              <View style={s.cardTop}>
                <Text style={s.productName}>{claim.product_name}</Text>
                <View style={[s.statusBadge, { backgroundColor: (STATUS_COLORS[claim.status] || G) + '20' }]}>
                  <Text style={[s.statusBadgeText, { color: STATUS_COLORS[claim.status] || G }]}>
                    {claim.status.toUpperCase()}
                  </Text>
                </View>
              </View>
              <Text style={s.customerLine}>{claim.customer_name} · {claim.customer_phone || 'no phone'}</Text>
              {claim.order_id ? <Text style={s.orderLine}>Order #{claim.order_id}</Text> : null}
              <Text style={s.issueText}>{claim.issue_description}</Text>
              <Text style={s.dateText}>{new Date(claim.created_at).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' })}</Text>

              {claim.status === 'resolved' && (
                <View style={s.resolvedBox}>
                  <Text style={s.resolvedText}>
                    Resolved: {claim.resolution_type} · {claim.resolved_by}
                  </Text>
                  {claim.resolution_notes ? <Text style={s.resolvedNotes}>{claim.resolution_notes}</Text> : null}
                </View>
              )}

              {claim.status === 'pending' && resolvingClaim === claim.id && (
                <View style={s.resolveForm}>
                  <View style={{ flexDirection: 'row', gap: 8, marginBottom: 10 }}>
                    {['replaced', 'refunded', 'repaired'].map(t => (
                      <TouchableOpacity key={t}
                        style={[s.typeChip, resolutionType === t && s.typeChipActive]}
                        onPress={() => setResolutionType(t)}>
                        <Text style={[s.typeChipText, resolutionType === t && s.typeChipTextActive]}>
                          {t.charAt(0).toUpperCase() + t.slice(1)}
                        </Text>
                      </TouchableOpacity>
                    ))}
                  </View>
                  <TextInput style={s.notesInput} value={resolutionNotes} onChangeText={setResolutionNotes}
                    placeholder="Notes (optional)" placeholderTextColor="rgba(255,255,255,0.25)" />
                  <TouchableOpacity style={s.confirmResolveBtn} onPress={() => resolveClaim(claim.id)}>
                    <Text style={s.confirmResolveBtnText}>Confirm Resolution</Text>
                  </TouchableOpacity>
                </View>
              )}

              {claim.status === 'pending' && resolvingClaim !== claim.id && (
                <View style={{ flexDirection: 'row', gap: 10, marginTop: 12 }}>
                  <TouchableOpacity style={s.resolveBtn} onPress={() => setResolvingClaim(claim.id)}>
                    <Text style={s.resolveBtnText}>Resolve</Text>
                  </TouchableOpacity>
                  <TouchableOpacity style={s.rejectBtn} onPress={() => rejectClaim(claim.id)}>
                    <Text style={s.rejectBtnText}>Reject</Text>
                  </TouchableOpacity>
                </View>
              )}
            </View>
          ))}
          <View style={{ height: 40 }} />
        </ScrollView>
      )}
    </SafeAreaView>
  );
}

const s = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#060E06' },
  header: {
    flexDirection: 'row', alignItems: 'center', padding: 14, gap: 12,
    borderBottomWidth: 1, borderBottomColor: 'rgba(201,168,76,0.15)',
    backgroundColor: '#0A160A',
  },
  backBtn: {
    backgroundColor: 'rgba(201,168,76,0.1)', borderRadius: 10,
    padding: 8, borderWidth: 1, borderColor: 'rgba(201,168,76,0.2)',
  },
  headerTitle: { fontSize: 17, fontWeight: 'bold', color: '#fff' },
  headerSub: { fontSize: 11, color: 'rgba(255,255,255,0.4)' },
  newBtn: { backgroundColor: G, borderRadius: 10, padding: 8 },
  filterRow: { flexDirection: 'row', padding: 12, gap: 8, borderBottomWidth: 1, borderBottomColor: 'rgba(201,168,76,0.1)' },
  filterChip: { flex: 1, paddingVertical: 8, borderRadius: 10, alignItems: 'center', borderWidth: 1, borderColor: 'rgba(201,168,76,0.2)' },
  filterChipActive: { backgroundColor: G, borderColor: G },
  filterChipText: { fontSize: 12, color: 'rgba(255,255,255,0.4)', fontWeight: '700' },
  filterChipTextActive: { color: '#fff' },
  centerBox: { flex: 1, alignItems: 'center', justifyContent: 'center', gap: 10, padding: 40 },
  emptyText: { fontSize: 14, color: 'rgba(255,255,255,0.4)' },
  card: {
    backgroundColor: '#0E1A0E', borderRadius: 14, padding: 14,
    marginBottom: 12, borderWidth: 1, borderColor: 'rgba(201,168,76,0.15)',
  },
  cardTop: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 },
  productName: { fontSize: 15, fontWeight: 'bold', color: '#fff', flex: 1 },
  statusBadge: { borderRadius: 8, paddingHorizontal: 8, paddingVertical: 3 },
  statusBadgeText: { fontSize: 10, fontWeight: 'bold' },
  customerLine: { fontSize: 12, color: 'rgba(255,255,255,0.5)', marginBottom: 2 },
  orderLine: { fontSize: 11, color: 'rgba(255,255,255,0.35)', marginBottom: 6 },
  issueText: { fontSize: 13, color: 'rgba(255,255,255,0.7)', marginTop: 4, lineHeight: 18 },
  dateText: { fontSize: 10, color: 'rgba(255,255,255,0.3)', marginTop: 8 },
  resolvedBox: { marginTop: 10, backgroundColor: 'rgba(201,168,76,0.08)', borderRadius: 8, padding: 8 },
  resolvedText: { fontSize: 12, color: G, fontWeight: '600' },
  resolvedNotes: { fontSize: 11, color: 'rgba(255,255,255,0.5)', marginTop: 4 },
  resolveBtn: { flex: 1, backgroundColor: G, borderRadius: 10, padding: 10, alignItems: 'center' },
  resolveBtnText: { color: '#060E06', fontWeight: 'bold', fontSize: 12 },
  rejectBtn: { flex: 1, backgroundColor: 'rgba(239,68,68,0.15)', borderRadius: 10, padding: 10, alignItems: 'center', borderWidth: 1, borderColor: '#EF4444' },
  rejectBtnText: { color: '#EF4444', fontWeight: 'bold', fontSize: 12 },
  resolveForm: { marginTop: 12, paddingTop: 12, borderTopWidth: 1, borderTopColor: 'rgba(201,168,76,0.1)' },
  typeChip: { flex: 1, paddingVertical: 8, borderRadius: 8, alignItems: 'center', borderWidth: 1, borderColor: 'rgba(201,168,76,0.2)' },
  typeChipActive: { backgroundColor: G, borderColor: G },
  typeChipText: { fontSize: 11, color: 'rgba(255,255,255,0.5)', fontWeight: '600' },
  typeChipTextActive: { color: '#fff' },
  notesInput: {
    backgroundColor: 'rgba(255,255,255,0.05)', borderRadius: 8, padding: 10,
    color: '#fff', fontSize: 13, borderWidth: 1, borderColor: 'rgba(201,168,76,0.2)', marginBottom: 10,
  },
  confirmResolveBtn: { backgroundColor: G, borderRadius: 10, padding: 10, alignItems: 'center' },
  confirmResolveBtnText: { color: '#060E06', fontWeight: 'bold', fontSize: 13 },
  label: { fontSize: 12, color: 'rgba(255,255,255,0.5)', marginBottom: 6, marginTop: 12 },
  input: {
    backgroundColor: 'rgba(255,255,255,0.05)', borderRadius: 10, padding: 12,
    color: '#fff', fontSize: 14, borderWidth: 1, borderColor: 'rgba(201,168,76,0.2)',
  },
  saveBtn: { backgroundColor: G, borderRadius: 12, padding: 16, alignItems: 'center', marginTop: 24 },
  saveBtnText: { color: '#060E06', fontWeight: 'bold', fontSize: 15 },
});
