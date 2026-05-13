from flask import Flask, request, jsonify
 
app = Flask(__name__)

courses = [ 
         { "id" : 1 , "title" : "DevOps Engineering"
           , " instructor": "memoona amjad"}
         {"id" : 2 , "title" : "sofware Design ", 
          "instructor":"adnan shah"}]

  
@app.route('/api/health', methods=['GET'])
def get_health():
     return {"status":"ok"}


@app.route('/courses', methods=['GET'])
def get_students():
    return jsonify(courses)


@app.route('/courses/<int:id>', methods=['GET'])
def get_student(id):
    courses = courses.get(id)
    if courses:
        return jsonify({id: courses})
    else:
        return jsonify({"error": "course not found"}), 404


@app.route('/courses', methods=['POST'])
def add_course():
    data = request.get_json()
    if 'title' not in data:
        return jsonify({"error": "title is required"}), 400
    
    new_id = max(courses.keys()) + 1 if courses else 1
    courses[new_id] = {'title': data['title']}
    return jsonify({new_id: courses [new_id]}), 201

@app.route('/courses/<int:id>', methods=['PUT'])
def courses(id):
    data = request.get_json()
    if 'title' not in data:
        return jsonify({"error": "title is required"}), 400
    
    courses = courses.get(id)
    if courses:
        courses['name'] = data['name']
        return jsonify({id: courses})
    else:
        return jsonify({"error": "course not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

