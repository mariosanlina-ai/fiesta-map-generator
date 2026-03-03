import tensorflow as tf
from tensorflow import keras

class NeuralNetworkTrainer:
    def __init__(self):
        # Initialize the model
        self.model = self.build_model()

    def build_model(self):
        # Build a sequential model
        model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28, 28)),  # Adjust input shape to your data
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(10, activation='softmax')
        ])
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        return model

    def train(self, x_train, y_train, epochs=5):
        # Train the model
        self.model.fit(x_train, y_train, epochs=epochs)

    def evaluate(self, x_test, y_test):
        # Evaluate the model
        test_loss, test_acc = self.model.evaluate(x_test, y_test)
        print(f'\nTest accuracy: {test_acc}')

# Example of usage:
# trainer = NeuralNetworkTrainer()
# trainer.train(training_data, training_labels)
# trainer.evaluate(test_data, test_labels)