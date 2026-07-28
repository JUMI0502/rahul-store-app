import { useState, useEffect } from 'react';
import {
  StyleSheet, Text, View, TouchableOpacity,
  SafeAreaView, StatusBar, ScrollView, Linking,
  ActivityIndicator, RefreshControl
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import * as Haptics from 'expo-haptics';

const API_URL = 'https://rahul-auto-spares-backend.onrender.com';
const G = '#22C55E';

export default function AbandonedCartsScreen({ onBack }) {
  const [carts, setCarts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [sendingPhone, setSendingPhone] = useState(null);

  useEffect(() => { fetchCarts(); }, []);

  const fetchCarts = async () => {
    try {
      const r = await fetch(`${API_URL}/carts/abandoned?hours=3`);
      const d = await r.json();
      setCarts(d.abandoned_carts || []);
    } catch {
      setCarts([]);
    }
    setLoading(false);
  };

  const onRefresh = async () => {
    setRefreshing(true);
    await fetchCarts();
    setRefreshing(false);
  };

  const hoursSince = (dateStr) => {
    const diff = Date.now() - new Date(dateStr).getTime();
    return Math.floor(diff / (1000 * 60 * 60));
  };

  const sendNudge = async (cart) => {
    setSendingPhone(cart.customer_phone);
    Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light);
    const itemLines = cart.items.map(i => `- ${i.name} (x${i.qty})`).join('\n');
    const msg =
      `Hi ${cart.customer_name || 'there'}!\n\n` +
      `Looks like you left some items in your cart at New Rahul Auto Spares:\n\n` +
      `${itemLines}\n\n` +
      `Still interested? Come by anytime or reply here and we'll hold them for you!\n\n` +
      `Telugu Peta, Nandyal\n08514-244944`;

    Linking.openURL(`https://wa.me/91${cart.customer_phone}?text=${encodeURIComponent(msg)}`);

    try {
      await fetch(`${API_URL}/carts/${cart.customer_phone}/reminder-sent`, { method: 'POST' });
      fetchCarts();
    } catch {}
    setSendingPhone(null);
  };

  return (
    <SafeAreaView style={s.container}>
      <StatusBar barStyle="light-content" backgroundColor="#060E06" />
      <View style={s.header}>
        <TouchableOpacity style={s.backBtn} onPress={onBack}>
          <Ionicons name="arrow-back" size={16} color={G} />
        </TouchableOpacity>
        <View style={{ flex: 1 }}>
          <Text style={s.headerTitle}>Abandoned Carts</Text>
          <Text style={s.headerSub}>Customers who added items but didn't checkout</Text>
        </View>
      </View>

      {loading ? (
        <View style={s.centerBox}><ActivityIndicator color={G} /></View>
      ) : carts.length === 0 ? (
        <View style={s.centerBox}>
          <Ionicons name="cart-outline" size={48} color="rgba(255,255,255,0.2)" />
          <Text style={s.emptyText}>No abandoned carts right now</Text>
        </View>
      ) : (
        <ScrollView contentContainerStyle={{ padding: 14 }}
          refreshControl={<RefreshControl refreshing={refreshing} onRefresh={onRefresh} tintColor={G} />}>
          <Text style={s.countLabel}>{carts.length} cart(s) sitting idle (3+ hours)</Text>
          {carts.map(cart => (
            <View key={cart.customer_phone} style={s.card}>
              <View style={s.cardTop}>
                <Text style={s.name}>{cart.customer_name || 'Customer'}</Text>
                <Text style={s.hoursAgo}>{hoursSince(cart.updated_at)}h ago</Text>
              </View>
              <Text style={s.phone}>{cart.customer_phone}</Text>
              {cart.items.map((item, i) => (
                <Text key={i} style={s.itemLine}>· {item.name} × {item.qty}</Text>
              ))}
              {cart.reminder_sent && (
                <View style={s.sentBadge}>
                  <Ionicons name="checkmark" size={11} color={G} />
                  <Text style={s.sentBadgeText}>Nudge already sent</Text>
                </View>
              )}
              <TouchableOpacity
                style={[s.sendBtn, sendingPhone === cart.customer_phone && { opacity: 0.5 }]}
                disabled={sendingPhone === cart.customer_phone}
                onPress={() => sendNudge(cart)}>
                <Ionicons name="logo-whatsapp" size={16} color="#fff" />
                <Text style={s.sendBtnText}>Send Nudge</Text>
              </TouchableOpacity>
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
    borderBottomWidth: 1, borderBottomColor: 'rgba(34,197,94,0.15)',
    backgroundColor: '#0A160A',
  },
  backBtn: {
    backgroundColor: 'rgba(34,197,94,0.1)', borderRadius: 10,
    padding: 8, borderWidth: 1, borderColor: 'rgba(34,197,94,0.2)',
  },
  headerTitle: { fontSize: 17, fontWeight: 'bold', color: '#fff' },
  headerSub: { fontSize: 11, color: 'rgba(255,255,255,0.4)' },
  centerBox: { flex: 1, alignItems: 'center', justifyContent: 'center', gap: 10, padding: 40 },
  emptyText: { fontSize: 14, color: 'rgba(255,255,255,0.4)' },
  countLabel: { fontSize: 12, color: 'rgba(255,255,255,0.4)', marginBottom: 12 },
  card: {
    backgroundColor: '#0E1A0E', borderRadius: 14, padding: 14,
    marginBottom: 12, borderWidth: 1, borderColor: 'rgba(34,197,94,0.15)',
  },
  cardTop: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' },
  name: { fontSize: 15, fontWeight: 'bold', color: '#fff' },
  hoursAgo: { fontSize: 11, color: '#F59E0B', fontWeight: '600' },
  phone: { fontSize: 12, color: 'rgba(255,255,255,0.4)', marginTop: 2, marginBottom: 8 },
  itemLine: { fontSize: 13, color: 'rgba(255,255,255,0.7)', marginBottom: 2 },
  sentBadge: {
    flexDirection: 'row', alignItems: 'center', gap: 4, marginTop: 8,
    alignSelf: 'flex-start', backgroundColor: 'rgba(34,197,94,0.1)',
    borderRadius: 8, paddingHorizontal: 6, paddingVertical: 2,
  },
  sentBadgeText: { fontSize: 10, color: G },
  sendBtn: {
    flexDirection: 'row', alignItems: 'center', justifyContent: 'center', gap: 8,
    backgroundColor: '#25D366', borderRadius: 10, padding: 10, marginTop: 12,
  },
  sendBtnText: { color: '#fff', fontWeight: 'bold', fontSize: 13 },
});
