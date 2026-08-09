import { Text, View, StyleSheet } from 'react-native';
import { Ionicons } from '@expo/vector-icons';

export default function StatCard({ icon, label, value, color }) {
  return (
    <View style={[sc.card, { borderColor: color + '30' }]}>
      <View style={[sc.iconBox, { backgroundColor: color + '15' }]}>
        <Ionicons name={icon} size={20} color={color} />
      </View>
      <Text style={sc.label}>{label}</Text>
      <Text style={[sc.value, { color }]}>{value}</Text>
    </View>
  );
}

const sc = StyleSheet.create({
  card: {
    flex: 1, backgroundColor: '#0D1A0D', borderRadius: 14,
    padding: 14, alignItems: 'center', gap: 6, borderWidth: 1,
  },
  iconBox: { width: 40, height: 40, borderRadius: 10, alignItems: 'center', justifyContent: 'center' },
  icon: { fontSize: 20 },
  label: { fontSize: 10, color: 'rgba(255,255,255,0.35)', letterSpacing: 1, textTransform: 'uppercase', textAlign: 'center' },
  value: { fontSize: 24, fontWeight: 'bold' },
});
