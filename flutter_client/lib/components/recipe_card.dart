import 'package:baking_client/models/recipe.dart';
import 'package:flutter/material.dart';
import 'package:transparent_image/transparent_image.dart';

class RecipeCard extends StatelessWidget {
  const RecipeCard({
    Key? key,
    required this.recipe,
  }) : super(key: key);

  final Recipe recipe;

  @override
  Widget build(BuildContext context) {
    return Container(
      child: getCard(context),
    );
  }

  _getImage(BuildContext context) {
    if (recipe.imageUrl == null || recipe.imageUrl!.isEmpty) {
      return Stack(children: <Widget>[
        Center(
            child: Ink.image(
          image: const AssetImage('assets/images/bread_placeholder.jpeg'),
          fit: BoxFit.cover,
        ))
      ]);
    } else {
      final FadeInImage breadImage = FadeInImage.memoryNetwork(
        placeholder: kTransparentImage,
        image: recipe.imageUrl ?? '',
        fit: BoxFit.cover,
      );

      return Stack(
        children: <Widget>[
          const Center(child: CircularProgressIndicator()),
          SizedBox(
            width: MediaQuery.of(context).size.width,
            height: MediaQuery.of(context).size.height,
            child: breadImage,
          )
        ],
      );
    }
  }

  Card getCard(BuildContext context) {
    return Card(
        elevation: 15.0,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(15),
        ),
        child: Column(
          children: [
            ListTile(
                title: Text(recipe.name),
                // subtitle: Text(recipe.description),
                trailing: SizedBox(
                  child: Chip(
                    backgroundColor: Colors.transparent,
                    avatar: const CircleAvatar(
                      backgroundColor: Colors.transparent,
                      child: IconTheme(
                        data: IconThemeData(color: Colors.blue),
                        child: Icon(Icons.water),
                      ),
                    ),
                    label: Text(recipe.hydration.toString() + "%"),
                  ),
                )),
            SizedBox(
              height: 200.0,
              child: _getImage(context),
            ),
            Container(
              padding: const EdgeInsets.all(16.0),
              alignment: Alignment.centerLeft,
              child: Text(recipe.description),
            ),
            ButtonBar(
              children: [
                TextButton(
                  child: const Text('BAKE'),
                  onPressed: () {/* ... */},
                ),
              ],
            )
          ],
        ));
  }
}
