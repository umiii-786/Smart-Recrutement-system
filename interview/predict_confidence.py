import pickle 
import cv2
import numpy as np
# import tensorflow as tf
from tensorflow import keras


def preprocess_single(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.GaussianBlur(image, (3,3), 0)
    image=cv2.resize(image,(96,96))
    return image.astype(np.float32) / 255.0


def predictConfidence(croped_image):
    
    model=pickle.load(open('./model/model_with_76.pkl','rb'))
    labels={'0':'confident', '1':'unconfident'}
    proced_image=preprocess_single(croped_image)
    print('ya ha shape ',proced_image.shape)
    print(np.array([proced_image]).shape)
    probablities=model.predict(np.array([proced_image]))
    predicted_val = (probablities > 0.5).astype("int32").flatten()
    print(predicted_val[0])
    label=labels[f'{predicted_val[0]}']
    return probablities[0]


def confidence_to_rating(probs):
    # extract probability values
    probs = np.array(probs)

    avg_conf = np.mean(probs)

    # convert to 1–5 scale
    if avg_conf < 0.2:
        rating = 1
    elif avg_conf < 0.4:
        rating = 2
    elif avg_conf < 0.6:
        rating = 3
    elif avg_conf < 0.8:
        rating = 4
    else:
        rating = 5

    return rating

async def FindSoftSkill(videopath, sample_rate_sec=1):
    cap = cv2.VideoCapture(videopath)

    fps = cap.get(cv2.CAP_PROP_FPS)

    print("Video FPS (metadata):", fps)

    probs = []

    frame_index = 0
    frame_interval = int(fps * sample_rate_sec) if fps > 0 else 30  # fallback

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # 🔥 Process only 1 frame per second (or per sample_rate_sec)
        if frame_index % frame_interval == 0:
            prob = predictConfidence(frame)
            print(prob)
            probs.append(float(prob[0]))

        frame_index += 1

    cap.release()

    print(probs)
    rating=confidence_to_rating(probs=probs)

    return rating