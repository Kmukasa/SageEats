import React from "react";
import { StyleSheet, View, Text } from "react-native";
import { Restaurant, MapRegion } from "../types";

interface GoogleMapComponentProps {
  restaurants: Restaurant[];
  region: MapRegion;
  onMarkerPress?: (restaurant: Restaurant) => void;
}

export default function GoogleMapComponent({
  restaurants,
  region,
  onMarkerPress,
}: GoogleMapComponentProps) {
  // For now, show a placeholder until we properly configure the map
  return (
    <View style={styles.container}>
      <View style={styles.mapPlaceholder}>
        <Text style={styles.placeholderText}>🗺️ Map View</Text>
        <Text style={styles.placeholderSubtext}>
          {restaurants.length} restaurants in this area
        </Text>
        <Text style={styles.instructionText}>
          Add your Google Maps API key to app.json to enable map functionality
        </Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  map: {
    width: "100%",
    height: "100%",
  },
  mapPlaceholder: {
    flex: 1,
    backgroundColor: "#f0f4f8",
    justifyContent: "center",
    alignItems: "center",
    padding: 20,
    borderRadius: 12,
    margin: 16,
    borderWidth: 2,
    borderColor: "#e2e8f0",
    borderStyle: "dashed",
  },
  placeholderText: {
    fontSize: 24,
    fontWeight: "bold",
    color: "#4a5568",
    marginBottom: 8,
  },
  placeholderSubtext: {
    fontSize: 16,
    color: "#718096",
    marginBottom: 16,
    textAlign: "center",
  },
  instructionText: {
    fontSize: 14,
    color: "#a0aec0",
    textAlign: "center",
    lineHeight: 20,
  },
});
