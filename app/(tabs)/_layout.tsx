import React from "react";
import { Stack } from "expo-router";
import { Text } from "react-native";
import { useFonts } from "expo-font";
import { StatusBar } from "expo-status-bar";

export default function TabLayout() {
  const [fontsLoaded] = useFonts({
    Limelight: require("@/assets/fonts/Limelight-Regular.ttf"),
  });
  return (
    <>
      <StatusBar style="dark" backgroundColor="#B0DA9A" />
      <Stack
        screenOptions={{
          headerTitleAlign: "center",
          headerTitle: (props) => (
            <Text
              style={{
                fontFamily: "Limelight",
                fontSize: 40,
                color: "#000",
                textAlign: "center",
              }}
            >
              SAFE PLATES
            </Text>
          ),
          headerStyle: {
            backgroundColor: "#B0DA9A",
          },
          headerShadowVisible: true,
        }}
      >
        <Stack.Screen
          name="index"
          options={{
            title: "Home",
          }}
        />
      </Stack>
    </>
  );
}
