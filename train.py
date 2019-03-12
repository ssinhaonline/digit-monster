import tensorflow as tf
import ConfigParser

# Read configurations
config = ConfigParser.RawConfigParser()
config.read("resources/digit-monster.properties")

def train():
    # Import dataset 28x28 images of handwritten digits
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # Normalize training and test sets
    x_train = tf.keras.utils.normalize(x_train, axis=1)
    x_test = tf.keras.utils.normalize(x_test, axis=1)

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
    model.compile(optimizer="adam",
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])
    model.fit(x_train, y_train, epochs=3)

    # Evaluate model against test set
    val_loss, val_acc = model.evaluate(x_test, y_test)
    print val_loss
    print val_acc

    # Save model at path
    output_file_path = "{}{}".format(config.get("ModelArtefacts", "model.path"),
                                     config.get("ModelArtefacts", "model.name"))
    model.save(output_file_path)
    print "Model saved at: {}".format(output_file_path)

if __name__ == "__main__":
    train()