from flask import Flask, jsonify, request

app = Flask(__name__)

notes = []


@app.route("/")
def home():
    return jsonify({
        "message": "CloudNotes API is running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json()

    note = {
        "id": len(notes) + 1,
        "title": data["title"],
        "content": data["content"]
    }

    notes.append(note)

    return jsonify(note), 201


@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes), 200


@app.route("/notes/<int:note_id>", methods=["GET"])
def get_note(note_id):
    for note in notes:
        if note["id"] == note_id:
            return jsonify(note), 200
            return jsonify({
                "error": "Note not found"
                }), 404

@app.route("/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    data = request.get_json()

    for note in notes:
        if note["id"] == note_id:
            note["title"] = data["title"]
            note["content"] = data["content"]

            return jsonify(note), 200

    return jsonify({
        "error": "Note not found"
    }), 404
    
    @app.route("/notes/<int:note_id>", methods=["DELETE"])
    def delete_note(note_id):
        for note in notes:
            if note["id"] == note_id:
                notes.remove(note)
                return jsonify({
                "message": "Note deleted successfully"
            }), 200

    return jsonify({
        "error": "Note not found"
    }), 404
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)