from flask import Flask, request, jsonify, send_from_directory
from models import db, Passenger
import hashlib

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

# Create the table if it doesn't exist
with app.app_context():
    db.create_all()

def add_passenger_to_db(data):
    hash_value = hashlib.sha256(str(data).encode()).hexdigest()
    is_transported = int(hash_value, 16) % 2 == 1
    status = 'transported' if is_transported else 'safe'
    passenger = Passenger(hash=hash_value, status=status, **data)
    db.session.add(passenger)
    db.session.commit()
    return status

def get_transported_count():
    return Passenger.query.filter_by(status='transported').count()

@app.route('/api/submit', methods=['POST'])
def submit():
    data = request.get_json()
    status = add_passenger_to_db(data)
    return jsonify({'status': status})

@app.route('/api/count_transported', methods=['GET'])
def count_transported():
    count = get_transported_count()
    return jsonify({'count': count})

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)