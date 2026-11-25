# Codeforces Duels

Codeforces Duels is a small website where two people compete on the same Codeforces problem. Both players start at the same time, and whoever solves the problem first wins.

## Why I made it

Solving problems alone can get boring, and it is hard to stay motivated. A duel makes practice more like a game: you have an opponent, a timer, and a clear goal. I made this project for people who already use Codeforces and want to train together with a friend.

## What it does now

- Shows the duel page with two players and a "Start duel" button.
- Starts a timer when the duel begins.
- Checks if a player has solved a problem. The server asks the Codeforces API for the player's submissions and looks for an accepted one. Right now the problem is fixed to 1A, because I am still testing.

## How to run it

1. Install Python and the libraries: `pip install flask requests`
2. Run `python app.py`
3. Open `http://127.0.0.1:5000` in the browser.
4. To test the check, open `http://127.0.0.1:5000/check?handle=YOUR_HANDLE`. It returns JSON that says if the handle has solved the problem.

## Files

- `app.py` - Flask server with the main page and the `/check` route.
- `cf.py` - functions that talk to the Codeforces API.
- `templates/index.html` - the duel page.
- `static/script.js` - button and timer.
- `static/style.css` - styles.

## Plans

- Let players enter their own handles.
- Pick a random problem for each duel.
- Check both players automatically and show the winner.
- Add more features later.
