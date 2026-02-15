import React, { useState } from "react";
import { View, Button, Image, Alert } from "react-native";
import * as ImagePicker from "expo-image-picker";

export default function HomeScreen() {
  const [imageUri, setImageUri] = useState<string | null>(null);

  const pickImage = async () => {
    const permissionResult =
      await ImagePicker.requestMediaLibraryPermissionsAsync();

    if (!permissionResult.granted) {
      Alert.alert("Permission required!");
      return;
    }

    const result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      quality: 1,
    });

    if (!result.canceled) {
      const uri = result.assets[0].uri;
      setImageUri(uri);
      console.log("Selected Image URI:", uri);
    }
  };

  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Button title="Pick an Image" onPress={pickImage} />

      {imageUri && (
        <Image
          source={{ uri: imageUri }}
          style={{ width: 300, height: 300, marginTop: 20 }}
        />
      )}
    </View>
  );
}
