from flask import Flask, render_template, request
from datetime import datetime
from json import load, dump

note_app = Flask(__name__)

def load_note():
	with open('note.json', 'r') as file:
		return load(file)

def save_note(data):
	with open('note.json', 'w') as file:
		dump(data, file)
	return True

notes = load_note()

@note_app.route("/", methods=["GET", "POST"])
def index():

	if request.method == "POST":
		title = request.form.get("title")
		note = request.form.get("note")
		today = datetime.now()
		notes[title] = {
			"note" : note,
			"date" : "Posted :"+f"{today.day}-{today.month}-{today.year}-{today.hour}"
		}
		save_note(notes)
	page = render_template('index.html', notes=notes)
	return page
#https://github.com/imanuelbunawan/note.git
"""
setup awal
1. git config --global user.name "azharnian"
2. git config --global user.email "anas.sty@gmail.com"

nanti push pertama akan diminta login
3. buat repository di akun github, copy link
4. git clone url_git_repo
5. copy file ke folder clonenya
6. masuk ke folder clone cd /git/noteappcupu
7. git add *
8. git commit -m "komentar update" *
9. git push (kalau pertama kali, login)
"""