# Codeforces Duels

Codeforces Duels is a website where two people compete on the same Codeforces problem. The task is given to both users at the same time and the winner is determined according to who solved it faster.

## Reasons why I created it

It might be boring to solve problems alone and you might find it hard to motivate yourself. In case of a duel, your training becomes something of a game – there is an opponent, there is a timer and there is a goal. This project is intended for those who uses Codeforces and wants to train with a friend.

## Algorithm

1. Every participant enters their Codeforces handle.
2. A server randomly picks up the problem which is not solved by either of the participants.
3. When a user presses "Start Duel" button the timer starts running.
4. A server monitors both of the submissions of the users by means of Codeforces API.
5. In case of an accepted submission by one of the players the winner is announced along with the duration of the duel.

## Running the website

1. Install Python, flask and requests using pip: pip install flask requests
2. Run python app.py
3. Open http://127.0.0.1:5000 in the browser.

## Files used

- app.py - Flask server and routing.
- cf.py - functions communicating with Codeforces API.
- templates/index.html - duel webpage.
- static/script.js - buttons, timer and submission checking.
- static/style.css - styles.

## Issues encountered

- It was necessary to account for limitations in Codeforces API to avoid excessive usage of the queries to the website so submissions are checked not so frequently.
- Some of the possible cases include wrong handles and participants with no submissions therefore the error message is given instead of crashing the website.
- The project gave me some experience in creating small-scale server and working with the API.
