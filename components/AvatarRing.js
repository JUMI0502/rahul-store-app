import { Text, View, TouchableOpacity, Image, StyleSheet } from 'react-native';

const G = '#C9A84C';

export default function AvatarRing({ avatar, profileImage, size = 90, onPress }) {
  const imgSize = size - 4;
  return (
    <TouchableOpacity
      style={[avr.ring, { width: size, height: size, borderRadius: size / 2 }]}
      onPress={onPress} activeOpacity={0.8} disabled={!onPress}>
      {profileImage ? (
        <Image
          source={{ uri: profileImage }}
          style={{ width: imgSize, height: imgSize, borderRadius: imgSize / 2 }}
          resizeMode="cover"
        />
      ) : (
        <Text style={{ fontSize: size * 0.48 }}>{avatar}</Text>
      )}
      {onPress && (
        <View style={avr.badge}>
          <Text style={{ fontSize: 11 }}></Text>
        </View>
      )}
    </TouchableOpacity>
  );
}

const avr = StyleSheet.create({
  ring: {
    backgroundColor: 'rgba(201,168,76,0.1)', borderWidth: 2, borderColor: G,
    alignItems: 'center', justifyContent: 'center', marginBottom: 6,
    position: 'relative', overflow: 'visible',
  },
  badge: {
    position: 'absolute', bottom: -4, right: -4, width: 26, height: 26,
    borderRadius: 13, backgroundColor: '#0D1A0D', alignItems: 'center',
    justifyContent: 'center', borderWidth: 1.5, borderColor: G,
  },
});
