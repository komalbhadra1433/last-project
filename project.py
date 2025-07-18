mood_to_color = {
    "happy": "yellow",
    "sad": "blue",
    "angry": "red",
    "stressed": "blue",
    "relaxed": "green",
    "energetic": "red",
    "peaceful": "green",
    "romantic": "pink",
    "serious": "black"
}
color_to_outfit = {
    "red": "red t-shirt and jeans",
    "blue": "blue hoodie and sneakers",
    "yellow": "yellow sundress or yellow t-shirt",
    "green": "green kurta or green polo shirt",
    "black": "black formal suit or black dress",
    "pink": "pink top and white pants"
}

mood = input("How are you feeling today? ").lower()

if mood in mood_to_color:
    color = mood_to_color[mood]
    outfit = color_to_outfit.get(color, "a simple outfit in " + color)
    print("Recommended outfit color:", color)
    print("You can wear:", outfit)
else:
    print("Mood not recognized. Try happy, sad, relaxed, energetic, etc.")
