from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    # Randomly position the small clickable image
    position = {
        'top': f"{random.randint(0, 90)}%",
        'left': f"{random.randint(0, 90)}%"
    }
    return render_template('index.html', position=position)

if __name__ == '__main__':
    app.run(debug=True)

