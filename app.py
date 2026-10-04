from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

ANSWERS = {
    "python": "Python is a beginner-friendly programming language used for web development, automation, data analysis and AI.",
    "machine learning": "Machine Learning is a way of teaching computers to learn patterns from data and make predictions or decisions.",
    "database": "A database stores and organizes information so that applications can easily save, find and update data.",
    "html": "HTML is the standard language used to create the structure of web pages.",
    "css": "CSS is used to style web pages, including colors, spacing, fonts and layouts."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question", "").strip().lower()
    if not question:
        return jsonify({"answer": "Please enter a question."})
    for key, answer in ANSWERS.items():
        if key in question:
            return jsonify({"answer": answer})
    return jsonify({
        "answer": "I can help with basic topics such as Python, Machine Learning, Database, HTML and CSS. Try asking about one of these topics."
    })

@app.route("/quiz")
def quiz():
    questions = [
        {"q": "Which language is beginner-friendly and widely used in AI?", "options": ["Python", "HTML", "CSS", "SQL"], "answer": "Python"},
        {"q": "What does HTML mainly define?", "options": ["Web page structure", "Database", "Operating system", "Antivirus"], "answer": "Web page structure"},
        {"q": "What is used to store organized information?", "options": ["Database", "Browser", "Compiler", "Keyboard"], "answer": "Database"}
    ]
    return jsonify(questions)

@app.route("/study-plan")
def study_plan():
    return jsonify([
        {"day": "Day 1", "task": "Learn Python basics – variables, data types and input/output"},
        {"day": "Day 2", "task": "Practice if-else conditions and loops"},
        {"day": "Day 3", "task": "Learn functions and lists"},
        {"day": "Day 4", "task": "Practice basic coding problems"},
        {"day": "Day 5", "task": "Take a quiz and revise weak topics"}
    ])

if __name__ == "__main__":
    app.run(debug=True)
