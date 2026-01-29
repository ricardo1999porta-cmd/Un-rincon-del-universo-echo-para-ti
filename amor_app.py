from flask import Flask, render_template_string
import random
import os

app = Flask(__name__)

frases = [
"Tu sonrisa es mi lugar favorito.",
"Contigo todo tiene sentido.",
"Eres mi casualidad más bonita.",
"Mi mundo es mejor desde que llegaste.",
"Tu abrazo es mi paz.",
"Si existes tú, todo vale la pena.",
"Eres mi pensamiento feliz automático.",
"Gracias por existir en mi vida.",
"Eres mi persona favorita.",
"Mi corazón aprendió tu nombre."
]

while len(frases) < 500:
    frases.append(random.choice(frases) + " ❤️")

html = """
<!DOCTYPE html>
<html>
<head>
<title>Para Allison 💖</title>
<style>
body {background: linear-gradient(to right, #ff9a9e, #fad0c4);
text-align:center; font-family:Arial; margin-top:20%; color:white;}
.frase {font-size:28px; margin:30px;}
button {padding:15px 30px; font-size:18px; border:none;
border-radius:10px; background:white; color:#ff4e8a;}
</style>
</head>
<body>
<h1>💌 Un rincón del universo hecho para Allison 💌</h1>
<div class="frase">{{ frase }}</div>
<form method="get">
<button>Otra frase 💖</button>
</form>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html, frase=random.choice(frases))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

        
