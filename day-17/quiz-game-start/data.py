import requests
import html

api_url = "https://opentdb.com/api.php?amount=20&category=9&type=boolean"
response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()

question_data = []

for question in data["results"]:
    question_text = html.unescape(question.get("question", "No question available"))
    correct_answer = html.unescape(question.get("correct_answer", "No answer available"))
    question_data.append({
        "text": question_text,
        "answer": correct_answer
    })

