import tensorflow as tf
import numpy as np
import ConfigParser

# Read configurations
config = ConfigParser.RawConfigParser()
config.read("resources/digit-monster.properties")

def predict(X):
    try:
        # Load model
        model_file_path = "{}{}".format(config.get("ModelArtefacts", "model.path"),
                                        config.get("ModelArtefacts", "model.name"))
        model = tf.keras.models.load_model(model_file_path)
    except:
        raise Exception("Could not load trained model")

    # Convert to numpy array as per TF model requirements
    X = np.array(X)

    # Normalize image vector
    X_normalized = tf.keras.utils.normalize(X, axis=1)

    # Predict probability of labels and consider label with highest P
    prediction_probabilities = model.predict(X_normalized)
    return np.argmax(prediction_probabilities, axis=1).tolist()