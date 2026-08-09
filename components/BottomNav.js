import { Text, View, TouchableOpacity, StyleSheet } from 'react-native';
import * as Haptics from 'expo-haptics';
import { Ionicons } from '@expo/vector-icons';

export default function BottomNav({ active, onChange, newCount }) {
  const tabs = [
    { id: 'orders',  icon: 'receipt-outline',     label: 'Orders', badge: newCount },
    { id: 'stock',   icon: 'cube-outline',          label: 'Stock' },
    { id: 'scanner', icon: 'qr-code-outline',       label: 'Scan' },
    { id: 'vendors', icon: 'business-outline',      label: 'Vendors' },
    { id: 'reports', icon: 'bar-chart-outline',     label: 'Reports' },
    { id: 'profile', icon: 'person-circle-outline', label: 'Me' },
  ];
  return (
    <View style={nb.bar}>
      {tabs.map(tab => (
        <TouchableOpacity key={tab.id} style={nb.tab}
          onPress={() => {
            Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light);
            onChange(tab.id);
          }}>
          <View style={nb.iconWrap}>
            <Ionicons
              name={active === tab.id ? tab.icon.replace('-outline','') : tab.icon}
              size={22}
              color={active === tab.id ? '#C9A84C' : 'rgba(255,255,255,0.35)'}
            />
            {tab.badge > 0 && (
              <View style={nb.badge}>
                <Text style={nb.badgeText}>{tab.badge}</Text>
              </View>
            )}
          </View>
          <Text style={[nb.label, active === tab.id && nb.labelActive]}>
            {tab.label}
          </Text>
          {active === tab.id && <View style={nb.dot} />}
        </TouchableOpacity>
      ))}
    </View>
  );
}

const nb = StyleSheet.create({
  bar: {
    flexDirection: 'row', backgroundColor: '#060E06',
    borderTopWidth: 1, borderTopColor: 'rgba(201,168,76,0.25)',
    paddingBottom: 8, paddingTop: 10,
  },
  tab: { flex: 1, alignItems: 'center', paddingVertical: 2 },
  iconWrap: { position: 'relative', marginBottom: 3 },
  icon: { fontSize: 22 },
  badge: {
    position: 'absolute', top: -4, right: -8, backgroundColor: '#EF4444',
    borderRadius: 8, minWidth: 16, height: 16, alignItems: 'center',
    justifyContent: 'center', paddingHorizontal: 3,
  },
  badgeText: { color: '#fff', fontSize: 9, fontWeight: 'bold' },
  label: { fontSize: 10, color: 'rgba(255,255,255,0.3)', fontWeight: '600' },
  labelActive: { color: '#C9A84C' },
  dot: { width: 4, height: 4, borderRadius: 2, backgroundColor: '#C9A84C', marginTop: 2 },
});
