from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def game_of_guess():
    f = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <form action="/" method="POST">
        <label>
            <input name="hidden" type="number" value="too small" required>
            <button type="submit">Too Small</button>
            <input name="hidden" type="number" value="too big" required>
            <button type="submit">Too Big</button>
            <input name="hidden" type="number" value="you win" required>
            <button type="submit">You Won!</button>            
        </label>
    </form>
</body>
</html>
    """


    if request.method == 'POST':
        user_answer = request.form["hidden"]

    return f


if __name__ == "__main__":
    app.run(debug=True, port=5031)