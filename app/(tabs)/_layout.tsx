import React from "react";
import { Tabs } from "expo-router";
import { Text } from "react-native";
import Ionicons from "@expo/vector-icons/Ionicons";
import { useFonts } from "expo-font";
import { StatusBar } from "expo-status-bar";

export default function TabLayout() {
  const [fontsLoaded] = useFonts({
    Limelight: require("@/assets/fonts/Limelight-Regular.ttf"),
  });
  return (
    <>
      <StatusBar style="dark" backgroundColor="#B0DA9A" />
      <Tabs
        screenOptions={{
          tabBarActiveTintColor: "#000",
          tabBarInactiveTintColor: "#000",
          headerTitle: (props) => (
            <Text
              style={{
                fontFamily: "Limelight",
                fontSize: 45,
                color: "#000",
              }}
            >
              SAFE PLATES
            </Text>
          ),
          headerStyle: {
            backgroundColor: "#B0DA9A",
            height: 110,
          },
          headerShadowVisible: true,
          tabBarStyle: {
            backgroundColor: "#B0DA9A",
          },
        }}
      >
        <Tabs.Screen
          name="index"
          options={{
            title: "Home",
            tabBarIcon: ({ color, focused }) => (
              <Ionicons
                name={focused ? "home-sharp" : "home-outline"}
                color={color}
                size={24}
              />
            ),
          }}
        />
        <Tabs.Screen
          name="search"
          options={{
            title: "Search",
            tabBarIcon: ({ color, focused }) => (
              <Ionicons
                name={focused ? "search-sharp" : "search-outline"}
                color={color}
                size={24}
              />
            ),
          }}
        />
        <Tabs.Screen
          name="profile"
          options={{
            title: "Profile",
            tabBarIcon: ({ color, focused }) => (
              <Ionicons
                name={focused ? "person-sharp" : "person-outline"}
                color={color}
                size={24}
              />
            ),
          }}
        />
      </Tabs>
    </>
  );
}
