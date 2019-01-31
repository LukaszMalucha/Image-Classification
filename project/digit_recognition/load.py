import os.path
from keras.models import model_from_json
import tensorflow as tf

my_path = os.path.abspath(os.path.dirname(__file__))
digit_model_json = os.path.join(my_path, "../../static/digit_recognition/digit_model.json")
digit_model_h5 = os.path.join(my_path, "../../static/digit_recognition/digit_model.h5")


## Compile graph from saved model
def init_model():
    json_file = open(digit_model_json, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(digit_model_h5)
    print("Model succesfully loaded")

    loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    graph = tf.get_default_graph()

    return loaded_model, graph
