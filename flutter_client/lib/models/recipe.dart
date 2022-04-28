class Recipe {
  final String name;
  final String description;
  final int id;
  final int hydration;
  final String? imageUrl;
  final String? cdnUrl;

  const Recipe(
      {required this.name,
      required this.id,
      required this.description,
      required this.imageUrl,
      required this.cdnUrl,
      required this.hydration});

  factory Recipe.fromJson(Map<String, dynamic> json) {
    return Recipe(
      name: json['name'],
      description: json['description'],
      id: json['id'],
      hydration: json['hydration'],
      imageUrl: json['image_url'],
      cdnUrl: json['cdn_url'],
    );
  }
}
