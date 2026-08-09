import { Text, View, TouchableOpacity, Modal, ScrollView, Alert, StyleSheet } from 'react-native';
import * as Haptics from 'expo-haptics';
import * as ImagePicker from 'expo-image-picker';

const G = '#C9A84C';

export const AVATAR_OPTIONS = [
  { id: 'owner',    emoji: '', label: 'Owner' },
  { id: 'star',     emoji: '⭐', label: 'Senior' },
  { id: 'worker',   emoji: '', label: 'Staff' },
  { id: 'mechanic', emoji: '', label: 'Mechanic' },
  { id: 'bike',     emoji: '️', label: 'Biker' },
  { id: 'gear',     emoji: '️', label: 'Technical' },
  { id: 'shield',   emoji: '️', label: 'Manager' },
  { id: 'rocket',   emoji: '', label: 'Fast' },
  { id: 'fire',     emoji: '', label: 'Hot' },
  { id: 'diamond',  emoji: '', label: 'Premium' },
  { id: 'trophy',   emoji: '', label: 'Champion' },
  { id: 'lion',     emoji: '', label: 'Leader' },
];

export default function AvatarPickerModal({ visible, currentAvatar, currentImage, onSelectEmoji, onSelectImage, onClose }) {

  const pickFromGallery = async () => {
    const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();
    if (status !== 'granted') {
      Alert.alert('Permission Needed', 'Please allow access to your photos to set a profile picture.');
      return;
    }
    const result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      aspect: [1, 1],
      quality: 0.7,
    });
    if (!result.canceled && result.assets?.[0]) {
      onSelectImage(result.assets[0].uri);
      onClose();
    }
  };

  const takePhoto = async () => {
    const { status } = await ImagePicker.requestCameraPermissionsAsync();
    if (status !== 'granted') {
      Alert.alert('Permission Needed', 'Please allow camera access to take a profile photo.');
      return;
    }
    const result = await ImagePicker.launchCameraAsync({
      allowsEditing: true,
      aspect: [1, 1],
      quality: 0.7,
    });
    if (!result.canceled && result.assets?.[0]) {
      onSelectImage(result.assets[0].uri);
      onClose();
    }
  };

  const removePhoto = () => {
    onSelectImage(null);
    onClose();
  };

  return (
    <Modal visible={visible} animationType="slide" transparent
      onRequestClose={onClose}>
      <View style={ap.overlay}>
        <View style={ap.sheet}>
          <View style={ap.handle} />
          <Text style={ap.title}>Change Profile Picture</Text>
          <Text style={ap.sub}>Pick from gallery, take a photo, or choose an emoji</Text>

          <View style={ap.photoRow}>
            <TouchableOpacity style={ap.photoBtn} onPress={pickFromGallery}
              activeOpacity={0.8}>
              <View style={[ap.photoBtnIcon, { backgroundColor: 'rgba(79,110,247,0.15)' }]}>
                <Text style={{ fontSize: 30 }}>️</Text>
              </View>
              <Text style={ap.photoBtnLabel}>Gallery</Text>
              <Text style={ap.photoBtnSub}>Pick from{'\n'}photos</Text>
            </TouchableOpacity>

            <TouchableOpacity style={ap.photoBtn} onPress={takePhoto}
              activeOpacity={0.8}>
              <View style={[ap.photoBtnIcon, { backgroundColor: 'rgba(201,168,76,0.15)' }]}>
                <Text style={{ fontSize: 30 }}></Text>
              </View>
              <Text style={ap.photoBtnLabel}>Camera</Text>
              <Text style={ap.photoBtnSub}>Take a{'\n'}selfie</Text>
            </TouchableOpacity>

            {currentImage && (
              <TouchableOpacity style={ap.photoBtn} onPress={removePhoto}
                activeOpacity={0.8}>
                <View style={[ap.photoBtnIcon, { backgroundColor: 'rgba(239,68,68,0.1)' }]}>
                  <Text style={{ fontSize: 30 }}>️</Text>
                </View>
                <Text style={[ap.photoBtnLabel, { color: '#EF4444' }]}>Remove</Text>
                <Text style={ap.photoBtnSub}>Use emoji{'\n'}instead</Text>
              </TouchableOpacity>
            )}
          </View>

          <View style={ap.divider}>
            <View style={ap.dividerLine} />
            <Text style={ap.dividerText}>or choose an emoji avatar</Text>
            <View style={ap.dividerLine} />
          </View>

          <ScrollView showsVerticalScrollIndicator={false}
            style={{ maxHeight: 220 }}>
            <View style={ap.grid}>
              {AVATAR_OPTIONS.map(opt => {
                const selected = !currentImage && currentAvatar === opt.emoji;
                return (
                  <TouchableOpacity key={opt.id}
                    style={[ap.option, selected && ap.optionSelected]}
                    onPress={() => {
                      Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Medium);
                      onSelectEmoji(opt.emoji);
                      onClose();
                    }}>
                    <Text style={ap.optionEmoji}>{opt.emoji}</Text>
                    <Text style={[ap.optionLabel, selected && { color: G }]}>
                      {opt.label}
                    </Text>
                    {selected && (
                      <View style={ap.checkBadge}>
                        <Text style={ap.checkText}></Text>
                      </View>
                    )}
                  </TouchableOpacity>
                );
              })}
            </View>
          </ScrollView>

          <TouchableOpacity style={ap.cancelBtn} onPress={onClose}>
            <Text style={ap.cancelText}>Cancel</Text>
          </TouchableOpacity>
        </View>
      </View>
    </Modal>
  );
}

const ap = StyleSheet.create({
  overlay: { flex: 1, backgroundColor: 'rgba(0,0,0,0.75)', justifyContent: 'flex-end' },
  sheet: {
    backgroundColor: '#0D1A0D', borderTopLeftRadius: 28, borderTopRightRadius: 28,
    padding: 20, paddingBottom: 34, borderTopWidth: 1, borderColor: 'rgba(201,168,76,0.2)',
  },
  handle: { width: 40, height: 4, borderRadius: 2, backgroundColor: 'rgba(255,255,255,0.2)', alignSelf: 'center', marginBottom: 16 },
  title: { fontSize: 18, fontWeight: 'bold', color: '#fff', textAlign: 'center', marginBottom: 4 },
  sub: { fontSize: 11, color: 'rgba(255,255,255,0.4)', textAlign: 'center', marginBottom: 18 },
  photoRow: { flexDirection: 'row', gap: 10, marginBottom: 18 },
  photoBtn: {
    flex: 1, backgroundColor: '#060E06', borderRadius: 16, padding: 12,
    alignItems: 'center', gap: 6, borderWidth: 1, borderColor: 'rgba(201,168,76,0.2)',
  },
  photoBtnIcon: { width: 56, height: 56, borderRadius: 14, alignItems: 'center', justifyContent: 'center', marginBottom: 2 },
  photoBtnLabel: { fontSize: 13, fontWeight: 'bold', color: '#fff' },
  photoBtnSub: { fontSize: 9, color: 'rgba(255,255,255,0.4)', textAlign: 'center', lineHeight: 13 },
  divider: { flexDirection: 'row', alignItems: 'center', gap: 8, marginBottom: 14 },
  dividerLine: { flex: 1, height: 1, backgroundColor: 'rgba(201,168,76,0.15)' },
  dividerText: { fontSize: 10, color: 'rgba(255,255,255,0.3)' },
  grid: { flexDirection: 'row', flexWrap: 'wrap', gap: 8, justifyContent: 'center', paddingBottom: 8 },
  option: {
    width: 70, backgroundColor: '#060E06', borderRadius: 14, padding: 8,
    alignItems: 'center', gap: 3, borderWidth: 1.5,
    borderColor: 'rgba(201,168,76,0.15)', position: 'relative',
  },
  optionSelected: { backgroundColor: 'rgba(201,168,76,0.1)', borderColor: G },
  optionEmoji: { fontSize: 26 },
  optionLabel: { fontSize: 8, color: 'rgba(255,255,255,0.4)', fontWeight: 'bold', textTransform: 'uppercase' },
  checkBadge: { position: 'absolute', top: -6, right: -6, width: 18, height: 18, borderRadius: 9, backgroundColor: G, alignItems: 'center', justifyContent: 'center' },
  checkText: { color: '#fff', fontSize: 10, fontWeight: 'bold' },
  cancelBtn: { marginTop: 14, backgroundColor: 'rgba(255,255,255,0.06)', borderRadius: 14, padding: 14, alignItems: 'center' },
  cancelText: { color: 'rgba(255,255,255,0.5)', fontWeight: 'bold', fontSize: 14 },
});
