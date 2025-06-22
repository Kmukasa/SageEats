import React from "react";
import { View, StyleSheet } from "react-native";
import MapView, { Marker } from "react-native-maps";
import Constants from "expo-constants";

// Custom marker component for shorter, rounder markers
const CustomMarker = ({
  coordinate,
  title,
  description,
}: {
  coordinate: { latitude: number; longitude: number };
  title: string;
  description: string;
}) => (
  <Marker
    coordinate={coordinate}
    title={title}
    description={description}
    anchor={{ x: 0.5, y: 1 }}
  >
    <View style={styles.customMarker}>
      <View style={styles.markerInner} />
      <View style={styles.markerPointer} />
    </View>
  </Marker>
);

export default function Index() {
  // Restaurant data with coordinates
  const restaurants = [
    {
      id: 1,
      name: "Evelina",
      address: "211 DeKalb Ave, Brooklyn, NY 11205",
      latitude: 40.6895,
      longitude: -73.9678,
    },
    {
      id: 2,
      name: "Miss Ada",
      address: "184 DeKalb Ave, Brooklyn, NY 11205",
      latitude: 40.6897,
      longitude: -73.9691,
    },
    {
      id: 3,
      name: "Mango Bay",
      address: "271 Adelphi St, Brooklyn, NY 11205",
      latitude: 40.6876,
      longitude: -73.9714,
    },
  ];

  return (
    <View style={styles.container}>
      <MapView
        style={styles.map}
        initialRegion={{
          latitude: 40.6889,
          longitude: -73.9694,
          latitudeDelta: 0.01,
          longitudeDelta: 0.01,
        }}
      >
        {restaurants.map((restaurant) => (
          <CustomMarker
            key={restaurant.id}
            coordinate={{
              latitude: restaurant.latitude,
              longitude: restaurant.longitude,
            }}
            title={restaurant.name}
            description={restaurant.address}
          />
        ))}
      </MapView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
  },
  map: {
    flex: 1,
    width: "100%",
    height: "100%",
  },
  customMarker: {
    alignItems: "center",
    justifyContent: "center",
  },
  markerInner: {
    width: 20,
    height: 20,
    backgroundColor: "#FFA939",
    borderRadius: 10,
    borderWidth: 3,
    borderColor: "#FFFFFF",
    shadowColor: "#000",
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  markerPointer: {
    width: 0,
    height: 0,
    backgroundColor: "transparent",
    borderStyle: "solid",
    borderLeftWidth: 4,
    borderRightWidth: 4,
    borderTopWidth: 6,
    borderLeftColor: "transparent",
    borderRightColor: "transparent",
    borderTopColor: "#FFA939",
    marginTop: -1,
  },
});
