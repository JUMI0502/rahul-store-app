import { useState, useEffect } from 'react';
import {
  StyleSheet, Text, View, TouchableOpacity,
  SafeAreaView, StatusBar, ScrollView, Linking,
  ActivityIndicator, RefreshControl
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import * as Haptics from 'expo-haptics';

const API_URL = 'https://rahul-auto-spares-backend.onrender.com';
const G = '#C9A84C';

export default function ServiceRemindersScreen({ onBack }) {
  const [dueCustomers, setDueCustomers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [sendingPhone, setSendingPhone] = useState(null);

  useEffect(() => { fetchDueCustomers(); }, []);

  const fetchDueCustomers = async () => {
    try {
      const r = await fetch(`${API_URL}/customers/service-due?days=60`);
      const d = await r.json();
      setDueCustomers(d.due_customers || []);
    } catch {
      setDueCustomers([]);
    }
    setLoading(false);
  };

  const onRefresh = async () => {
    setRefreshing(true);
    await fetchDueCustomers();
    setRefreshing(false);
  };

  const daysSince = (dateStr) => {
    const diff = Date.now() - new Date(dateStr).getTime();
    return Math.floor(diff / (1000 * 60 * 60 * 24));
  };

  const sendReminder = async (customer) => {
    setSendingPhone(customer.customer_phone);
    Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light);
    const days = daysSince(customer.last_order_date);
    const msg =
      `Hi ${customer.customer_name}!\n\n` +
      `It has been about ${days} days since your last visit to New Rahul Auto Spares. ` +
      `Regular checkups keep your bike running smoothly - come by anytime for a free bike health check ` +
      `or to pick up any parts you need.\n\n` +
      `Telugu Peta, Nandyal\n08514-244944`;

    Linking.openURL(`https://wa.me/91${customer.customer_phone}?text=${encodeURIComponent(msg)}`);

    try {
      await fetch(`${API_URL}/customers/${customer.customer_phone}/service-reminder-sent`, {
        method: 'POST'
      });
      fetchDueCustomers();
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
          <Text style={s.headerTitle}>Service Reminders</Text>
          <Text style={s.headerSub}>Customers due for a checkup</Text>
        </View>
      </View>

      {loading ? (
        <View style={s.centerBox}>
          <ActivityIndicator color={G} />
        </View>
      ) : dueCustomers.length === 0 ? (
        <View style={s.centerBox}>
          <Ionicons name="checkmark-circle-outline" size={48} color="rgba(255,255,255,0.2)" />
          <Text style={s.emptyText}>No customers due right now</Text>
          <Text style={s.emptySub}>Everyone has ordered recently</Text>
        </View>
      ) : (
        <ScrollView contentContainerStyle={{ padding: 14 }}
          refreshControl={<RefreshControl refreshing={refreshing} onRefresh={onRefresh} tintColor={G} />}>
          <Text style={s.countLabel}>{dueCustomers.length} customer(s) due (60+ days since last order)</Text>
          {dueCustomers.map(c => (
            <View key={c.customer_phone} style={s.card}>
              <View style={{ flex: 1 }}>
                <Text style={s.name}>{c.customer_name}</Text>
                <Text style={s.phone}>{c.customer_phone}</Text>
                <Text style={s.meta}>
                  {daysSince(c.last_order_date)} days since last order · {c.total_orders} order(s) total
                </Text>
                {c.reminder_sent_recently && (
                  <View style={s.sentBadge}>
                    <Ionicons name="checkmark" size={11} color={G} />
                    <Text style={s.sentBadgeText}>Reminder sent recently</Text>
                  </View>
                )}
              </View>
              <TouchableOpacity
                style={[s.sendBtn, sendingPhone === c.customer_phone && { opacity: 0.5 }]}
                disabled={sendingPhone === c.customer_phone}
                onPress={() => sendReminder(c)}>
                <Ionicons name="logo-whatsapp" size={18} color="#fff" />
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
    borderBottomWidth: 1, borderBottomColor: 'rgba(201,168,76,0.15)',
    backgroundColor: '#0A160A',
  },
  backBtn: {
    backgroundColor: 'rgba(201,168,76,0.1)', borderRadius: 10,
    padding: 8, borderWidth: 1, borderColor: 'rgba(201,168,76,0.2)',
  },
  headerTitle: { fontSize: 17, fontWeight: 'bold', color: '#fff' },
  headerSub: { fontSize: 11, color: 'rgba(255,255,255,0.4)' },
  centerBox: { flex: 1, alignItems: 'center', justifyContent: 'center', gap: 10, padding: 40 },
  emptyText: { fontSize: 15, color: 'rgba(255,255,255,0.5)', fontWeight: '600' },
  emptySub: { fontSize: 12, color: 'rgba(255,255,255,0.3)' },
  countLabel: { fontSize: 12, color: 'rgba(255,255,255,0.4)', marginBottom: 12 },
  card: {
    backgroundColor: '#0E1A0E', borderRadius: 14, padding: 14,
    marginBottom: 10, borderWidth: 1, borderColor: 'rgba(201,168,76,0.15)',
    flexDirection: 'row', alignItems: 'center', gap: 12,
  },
  name: { fontSize: 15, fontWeight: 'bold', color: '#fff' },
  phone: { fontSize: 12, color: 'rgba(255,255,255,0.4)', marginTop: 2 },
  meta: { fontSize: 11, color: 'rgba(255,255,255,0.35)', marginTop: 4 },
  sentBadge: {
    flexDirection: 'row', alignItems: 'center', gap: 4, marginTop: 6,
    alignSelf: 'flex-start', backgroundColor: 'rgba(201,168,76,0.1)',
    borderRadius: 8, paddingHorizontal: 6, paddingVertical: 2,
  },
  sentBadgeText: { fontSize: 10, color: G },
  sendBtn: {
    backgroundColor: '#25D366', borderRadius: 12,
    width: 44, height: 44, alignItems: 'center', justifyContent: 'center',
  },
});
