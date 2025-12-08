from tensorflow.keras import models, layers, activations, initializers

model = models.Sequential([
    layers.Input(shape=(28,28,3)), # 28x28x1
    layers.Conv2D(10, kernel_size=(3,3), strides=(1,1), padding='same'), # 10 @ 28x28
    layers.Flatten(), # 7840
    layers.Dense(64, activation=activations.relu, kernel_initializer=initializers.RandomNormal()), # 64
    layers.Dense(24, activation=activations.softmax, kernel_initializer=initializers.RandomNormal()) # 24
])