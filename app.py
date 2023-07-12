from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    content = db.Column(db.String(120))

    def __init__(self, title, content):
        self.title = title
        self.content = content

class NoteSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('title', 'content', 'id')

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)


# endpoint to create new note
@app.route("/note", methods=["POST"])
def add_note():
    title = request.json['title']
    content = request.json['content']
    new_note = Note(title, content)
    db.session.add(new_note)
    db.session.commit()
    return note_schema.jsonify(new_note)

# endpoint to show all notes
@app.route("/note", methods=["GET"])
def get_note():
    all_notes = Note.query.all()
    result = notes_schema.dump(all_notes)
    return jsonify(result)

# endpoint to get note detail by id
@app.route("/note/<id>", methods=["GET"])
def note_detail(id):
    note = Note.query.get(id)
    return note_schema.jsonify(note)

# endpoint to update note
@app.route("/note/<id>", methods=["PUT"])
def note_update(id):
    note = Note.query.get(id)
    title = request.json['title']
    content = request.json['content']

    note.title = title
    note.content = content

    db.session.commit()
    return note_schema.jsonify(note)

# endpoint to delete note
@app.route("/note/<id>", methods=["DELETE"])
def note_delete(id):
    note = Note.query.get(id)
    db.session.delete(note)
    db.session.commit()

    return note_schema.jsonify(note)

if __name__ == '__main__':
    app.run(debug=True)
