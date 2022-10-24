from flask import Flask, request

app = Flask(__name__)

start = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Game Of Guess 3</title>
</head>
<body>
    <form action="/" method="POST">
    <div>Think about number between 1 and 1000. I will guess it in 10 moves.</div>
        <label>
            <input name="min_web" type="hidden" value="{}">
            <input name="max_web" type="hidden" value="{}">
            <input name="start" type="hidden" value="start">
            <button type="submit">Start</button>
        </label>
    </form>
</body>
</html>
    """

answer = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Game Of Guess 3</title>
</head>
<body>
<div>I guess it's {}</div>
<form action="/" method="POST">
    <label>
        <input name="answer_web" type="submit" value="too small">
    </label>
    <label>
        <input name="answer_web" type="submit" value="too big">
    </label>
    <label>
        <input name="answer_web" type="submit" value="you won">
    </label>
    <label>
        <input name="guess_web" type="hidden" value="{}">           
        <input name="min_web" type="hidden" value="{}">
        <input name="max_web" type="hidden" value="{}">
    </label>
</form>
</body>
</html>
"""

won = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Game Of Guess 3</title>
</head>
<body>
    <div>I Won! Your number is: {}</div>
</body>
</html>
    """


@app.route('/', methods=['GET', 'POST'])
def game_of_guess_3():
    if request.method == "GET":
        return start.format(0, 1000)
    else:
        if request.form.get("start") == "start":
            minimum = int(request.form.get("min_web"))
            maximum = int(request.form.get("max_web"))
            guess = (maximum - minimum) // 2 + minimum
            return answer.format(guess, guess, minimum, maximum)
        else:
            maximum = int(request.form.get("max_web"))
            minimum = int(request.form.get("min_web"))
            guess = int(request.form.get("guess_web"))
            if request.form.get("answer_web") == "too small":
                minimum = guess
            elif request.form.get("answer_web") == "too big":
                maximum = guess
            elif request.form.get("answer_web") == "you won":
                guess = guess
                return won.format(guess)

            guess = (maximum - minimum) // 2 + minimum
            return answer.format(guess, guess, minimum, maximum)


if __name__ == "__main__":
    app.run(debug=True, port=5031)
