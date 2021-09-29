from flask import Flask,render_template,jsonify

import model

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict/<car>')
def get_car_value(car):
    """
    Args:
        car ([type]): [description]
        example: http://127.0.0.1:5000/predict/15000,20,Toyota,Blue
    
    Returns:
        [type]: [description]
    """
    car = list(car.split(","))

    brand = car[2]
    color = car[3]

    # removing original values in the incoming list
    car.pop(3)
    car.pop(2)

    # change to integers
    for i,c in enumerate(car):
        car[i] = int(car[i])

    cars = model.load_data() # works
    # print(cars[0:3])

    encoded_brand = model.brand_converter(cars.copy(),brand)
    encoded_color = model.color_converter(cars.copy(),color)

    print(f"""
        Encoded Brand: {encoded_brand}
        Encoded Color: {encoded_color}
    """)

    car = car+encoded_brand+encoded_color
    print("Car Input: ",car)

    prediction_value = model.predict_worth(car)
    print('Predicted Value',prediction_value)

    return jsonify(prediction_value[0])


@app.route('/getbrands/')
def get_brands():
    cars = model.load_data() # works
    # print(cars[0:3])

    brands = cars['brand'].value_counts().index.to_list()

    return jsonify(brands)

@app.route('/getcolors/')
def get_colors():
    cars = model.load_data() # works
    # print(cars[0:3])

    colors = cars['color'].value_counts().index.to_list()

    return jsonify(colors)

@app.route('/foo')
def serve_foo():
    return 'This page is served via Flask!'


if __name__=='__main__':
    app.run(debug=True)