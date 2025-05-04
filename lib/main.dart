import 'package:flutter/material.dart';

void main() {
  runApp( MyApp() ); 
}
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.blue,
          title: Text('Pokeventures'),),
        body: Container(
          child: const Text('Welcome to PokeVenture'),
          margin: const EdgeInsets.all(50),
          padding: const EdgeInsets.all(50),
          ),
      )
    );
  }
}