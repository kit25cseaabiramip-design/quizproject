from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# 15 Python-based questions
questions = [
    {"id":1, "q":"3**2 = ?", "op":["6","9","5"], "ans":"9"},
    {"id":2, "q":"Keyword to define function?", "op":["func","def","define"], "ans":"def"},
    {"id":3, "q":"len('Python') = ?", "op":["5","6","7"], "ans":"6"},
    {"id":4, "q":"Immutable data type?", "op":["list","tuple","set"], "ans":"tuple"},
    {"id":5, "q":"Dictionary symbol?", "op":["[]","{}","()"], "ans":"{}"},
    {"id":6, "q":"Floor division operator?", "op":["/","//","%"], "ans":"//"},
    {"id":7, "q":"bool(0) = ?", "op":["True","False","Error"], "ans":"False"},
    {"id":8, "q":"Exception keyword?", "op":["try","catch","handle"], "ans":"try"},
    {"id":9, "q":"Loop structure?", "op":["if","for","def"], "ans":"for"},
    {"id":10, "q":"range(3) output?", "op":["[1,2,3]","[0,1,2]","[0,1,2,3]"], "ans":"[0,1,2]"},
    {"id":11, "q":"Input function?", "op":["scan()","input()","get()"], "ans":"input()"},
    {"id":12, "q":"'a'*3 = ?", "op":["aaa","a3","error"], "ans":"aaa"},
    {"id":13, "q":"Python framework?", "op":["Flask","React","Angular"], "ans":"Flask"},
    {"id":14, "q":"Python file extension?", "op":[".py",".java",".html"], "ans":".py"},
    {"id":15, "q":"Comment symbol?", "op":["#","//","<!--"], "ans":"#"}
]

# Home page
@app.route('/')
def home():
    return render_template("index.html", questions=questions)

# Submit quiz
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get("name")
    score = 0

    # Calculate score
    for q in questions:
        user = request.form.get(str(q["id"]))
        if user == q["ans"]:
            score += 1

    # Save result
    with open("result.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, score])

    # Show result
    return render_template("result.html",
                           name=name,
                           score=score,
                           total=len(questions))

# Run app
if __name__ == "__main__":
    app.run(debug=True)
