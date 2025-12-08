import cv2
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras import utils
import PIL
from PIL import UnidentifiedImageError

folder = os.path.abspath("./SimpleTest")

images = [
    os.path.join(folder, f)
    for f in os.listdir(folder)
]

model = load_model('model.keras')

count = 0

for image in images:
    try:
        img = image
        img = utils.load_img(img, target_size=(28, 28))

        img_array = utils.img_to_array(img)

        img_array = np.expand_dims(img_array, axis=0)

        pred = model.predict(img_array, verbose=0)

        predict_value = os.path.splitext(os.path.basename(images[np.argmax(pred)]))[0]
        real_value = os.path.splitext(os.path.basename(image))[0]
        print('Predict: ', predict_value, 'Real: ', real_value, '\t-> ', predict_value == real_value)
        if (predict_value == real_value):
            count += 1
    except UnidentifiedImageError:
        continue;

print(f"Acertos: {count}")