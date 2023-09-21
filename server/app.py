from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import Bakery, BakedGood, db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

migrate=Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return "Index for Bakery and Baked Goods API"

@app.route('/baked_goods', methods=['POST'])
def create_baked_good():
   
    new_baked_good = BakedGood(
        name=request.form.get("name"),
        price=request.form.get("price"),
        bakery_id=request.form.get("bakery_id")
        
        )

    db.session.add(new_baked_good)
    db.session.commit()
    new_baked_good_dict = new_baked_good_dict.to_dict()

    response = make_response(
        jsonify(new_baked_good_dict),
        201
        )

    return response


#update a bakery's name
@app.route('/bakeries/<int:id>', methods=['PATCH'])
def update_bakery_name(id):
    bakery_name = Bakery.query.filter_by(id=id).first()

    for attr in request.form:
        setattr(bakery_name, attr, request.form.get(attr))

    db.session.add(bakery_name)
    db.session.commit()

    bakery_name_dict = review.to_dict()

    response = make_response(
        jsonify(bakery_name_dict),
        200
        )

    return response


# delete a baked good
@app.route('/baked_goods/<int:id>', methods=['DELETE'])
def delete_baked_good(id):
    baked_good = BakedGood.query.get(id)
    if baked_good is None:
        return jsonify({'error': 'Baked good not found'}), 404

    db.session.delete(baked_good)
    db.session.commit()

    return jsonify({'message': 'Baked good deleted successfully'})

if __name__ == '__main__':
    app.run(port==5555)