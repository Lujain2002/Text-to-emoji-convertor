from flask import Flask, render_template, request

app = Flask(__name__)


emojis = {
    "sad": "😒", "happy": "😄", "laugh": "🤣", "love": "❤️", "angry": "🤬",
    "cry": "😭", "scared": "😨", "computer": "💻", "clap": "👏", "engineer": "👩‍💻",
    "thinking": "🤔", "car": "🚗", "cool": "😎", "sleepy": "😴", "money": "💸",
    "sun": "☀️", "doctor": "👩‍⚕️", "police": "👮‍♀️", "thumbs up": "👍", "night": "🌃",
    "moon": "🌑", "clock": "🕛", "party": "🎉", "pizza": "🍕", "meat": "🥩",
    "fruits": "🍈", "apple": "🍎", "orange": "🍊", "fire": "🔥", "star": "⭐",
    "angelic": "😇", "winking": "😉", "crazy": "🤪", "oops": "🤭", "shhh": "🤫",
    "exhausted": "😩", "tired": "😩", "shocked": "🤯", "injured": "🤕",
    "sick": "🤒", "strong": "💪", "superhero": "🦸", "ok": "👌", "handshake": "🤝",
    "amazed": "🤩", "waiting": "⏳", "calendar": "📅", "phone": "📱", "camera": "📷",
    "burger": "🍔", "fries": "🍟", "salad": "🥗", "chocolate": "🍫", "cake": "🎂",
    "airplane": "✈️", "bicycle": "🚲", "bus": "🚌", "rain": "🌧️", "rainbow": "🌈",
    "home": "🏠", "book": "📖", "bed": "🛏️", "boy": "👦", "girl": "👧", "family": "👨‍👩‍👧","cat":"🐈",
}


def text_to_emoji(text):
    words = text.lower().split() 
    converted_text = " ".join([emojis.get(word, " ") for word in words])  
    return converted_text


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_text = request.form["text"]  
        emoji_text = text_to_emoji(user_text)  
        return render_template("index.html", user_text=user_text, emoji_text=emoji_text)
    return render_template("index.html", user_text="", emoji_text="")

if __name__ == "__main__":
    app.run(debug=True)
