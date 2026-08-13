from flask import Flask, jsonify, request
import psycopg

app = Flask(__name__)

DB_CONFIG = {
    "dbname": "cloudnotes",
    "user": "cloudnotes_user",
    "password": "mani",
    "host": "localhost",
    "port": 5432
}


def get_db_connection():
    return psycopg.connect(**DB_CONFIG)


# Test PostgreSQL connection when Flask starts
try:
    conn = get_db_connection()
    print("PostgreSQL connection successful!")
    conn.close()
except Exception as e:
    print("PostgreSQL connection failed:", e)


# -------------------------
# HOME
# -------------------------

@app.route("/")
def home():
    return jsonify({
        "message": "CloudNotes API is running"
    })


# -------------------------
# HEALTH CHECK
# -------------------------

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


# -------------------------
# GET ALL NOTES
# -------------------------

@app.route("/notes", methods=["GET"])
def get_notes():

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, title, content FROM notes ORDER BY id"
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    notes = [
        {
            "id": row[0],
            "title": row[1],
            "content": row[2]
        }
        for row in rows
    ]

    return jsonify(notes), 200


# -------------------------
# CREATE NOTE
# -------------------------
@app.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json()

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO notes (title, content)
        VALUES (%s, %s)
        RETURNING id, title, content
        """,
        (data["title"], data["content"])
    )

    row = cur.fetchone()

    conn.commit()

    cur.close()
    conn.close()

    note = {
        "id": row[0],
        "title": row[1],
        "content": row[2]
    }

    return jsonify(note), 201

# -------------------------
# GET ONE NOTE
# -------------------------

@app.route("/notes/<int:note_id>", methods=["GET"])
def get_note(note_id):

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, title, content FROM notes WHERE id = %s",
        (note_id,)
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        return jsonify({
            "error": "Note not found"
        }), 404

    return jsonify({
        "id": row[0],
        "title": row[1],
        "content": row[2]
    }), 200


# -------------------------
# UPDATE NOTE
# -------------------------

@app.route("/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id):

    data = request.get_json()

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE notes
        SET title = %s, content = %s
        WHERE id = %s
        RETURNING id, title, content
        """,
        (data["title"], data["content"], note_id)
    )

    row = cur.fetchone()

    conn.commit()

    cur.close()
    conn.close()

    if row is None:
        return jsonify({
            "error": "Note not found"
        }), 404

    return jsonify({
        "id": row[0],
        "title": row[1],
        "content": row[2]
    }), 200


# -------------------------
# DELETE NOTE
# -------------------------

@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM notes WHERE id = %s RETURNING id",
        (note_id,)
    )

    row = cur.fetchone()

    conn.commit()

    cur.close()
    conn.close()

    if row is None:
        return jsonify({
            "error": "Note not found"
        }), 404

    return jsonify({
        "message": "Note deleted successfully"
    }), 200


# -------------------------
# START FLASK
# -------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)