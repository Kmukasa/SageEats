import { Text, View, StyleSheet, Button } from "react-native";
import { Link } from "expo-router";

export default function Index() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>SageEats</Text>
      <Button
        title="Get Started"
        onPress={() => console.log("Pressed get started")}
      />
      <Link href="/about" style={styles.aboutLink}>
        Go to about
      </Link>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    justifyContent: "center",
    alignItems: "center",
  },
  text: {
    fontSize: 20,
    fontWeight: "bold",
    color: "#25292e",
  },
  aboutLink: {
    marginTop: 20,
    padding: 10,
    fontSize: 20,
    textDecorationLine: "underline",
    color: "#f58026",
  },
});
