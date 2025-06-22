import React from "react";
import { View, Text, StyleSheet } from "react-native";

export default function SafePlatesHeader() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>SAFE PLATES</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: "#B5D6B2",
    paddingVertical: 16,
    alignItems: "center",
    justifyContent: "center",
  },
  title: {
    fontSize: 28,
    fontWeight: "bold",
    letterSpacing: 3,
    color: "#2d3748",
    textAlign: "center",
  },
});
