from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initialize a dictionary to store contacts
contacts = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']
    tags = request.form.getlist('tags')
    
    # Store the contact using a dictionary
    contacts[name] = {'phone': phone, 'tags': tags}
    return jsonify(success=True)

@app.route('/get_contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
