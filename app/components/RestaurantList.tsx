import React from "react";
import {
  View,
  Text,
  FlatList,
  TouchableOpacity,
  StyleSheet,
  Image,
} from "react-native";
import { Restaurant } from "../../types";

interface RestaurantListProps {
  restaurants: Restaurant[];
  onRestaurantPress?: (restaurant: Restaurant) => void;
}

export default function RestaurantList({
  restaurants,
  onRestaurantPress,
}: RestaurantListProps) {
  const renderRestaurant = ({ item }: { item: Restaurant }) => (
    <TouchableOpacity
      style={styles.restaurantCard}
      onPress={() => onRestaurantPress?.(item)}
    >
      <View style={styles.restaurantInfo}>
        <Text style={styles.restaurantName}>{item.name}</Text>
        <Text style={styles.restaurantAddress}>{item.address}</Text>
        {item.cuisine && (
          <Text style={styles.restaurantCuisine}>{item.cuisine}</Text>
        )}
        {item.rating && (
          <Text style={styles.restaurantRating}>⭐ {item.rating}</Text>
        )}
      </View>
      <TouchableOpacity style={styles.openMenuButton}>
        <Text style={styles.openMenuText}>Open Menu</Text>
      </TouchableOpacity>
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      <FlatList
        data={restaurants}
        renderItem={renderRestaurant}
        keyExtractor={(item) => item.id}
        showsVerticalScrollIndicator={false}
        contentContainerStyle={styles.listContainer}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
  },
  listContainer: {
    padding: 16,
    paddingBottom: 100,
  },
  restaurantCard: {
    backgroundColor: "#fff",
    borderRadius: 12,
    padding: 16,
    marginBottom: 16,
    shadowColor: "#000",
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
  },
  restaurantInfo: {
    flex: 1,
  },
  restaurantName: {
    fontSize: 18,
    fontWeight: "bold",
    color: "#2d3748",
    marginBottom: 4,
  },
  restaurantAddress: {
    fontSize: 14,
    color: "#718096",
    marginBottom: 4,
  },
  restaurantCuisine: {
    fontSize: 14,
    color: "#4a5568",
    marginBottom: 4,
  },
  restaurantRating: {
    fontSize: 14,
    color: "#f56500",
  },
  openMenuButton: {
    backgroundColor: "#ff8c42",
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 20,
  },
  openMenuText: {
    color: "#fff",
    fontSize: 14,
    fontWeight: "600",
  },
});
