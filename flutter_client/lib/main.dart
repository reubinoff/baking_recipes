import 'package:flutter/material.dart';
import 'package:baking_client/homepage.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    const appTitle = 'Baking';
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: "Baking",
      theme: ThemeData(
        primarySwatch: Colors.brown,
        fontFamily: "Pacifico",
      ),
      home: const HomePage(
        title: appTitle,
      ),
    );
  }
}
