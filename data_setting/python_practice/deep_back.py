import cv2
import numpy as np
from segmentation_models import Unet
from segmentation_models.backbones import get_preprocessing
from segmentation_models.losses import bce_jaccard_loss
from segmentation_models.metrics import iou_score

# 객체 이미지와 배경 이미지 로드
object_image = cv2.imread('./img/010.jpg')
background_image = cv2.imread('./img/030.jpg')

# U-Net 모델 불러오기
BACKBONE = 'resnet34'
preprocess_input = get_preprocessing(BACKBONE)
model = Unet(BACKBONE, classes=1, activation='sigmoid')
model.load_weights('unet_weights.h5')  # 미리 학습된 가중치 불러오기

# 객체 이미지 전처리 및 예측
input_image = cv2.resize(object_image, (256, 256))
input_image = preprocess_input(input_image)
input_image = np.expand_dims(input_image, axis=0)
mask = model.predict(input_image)[0]

# 마스크 이미지 이진화 처리
mask = (mask > 0.5).astype(np.uint8) * 255

# 마스크와 배경 이미지 합성
mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
result = cv2.bitwise_and(object_image, mask)
background = cv2.bitwise_and(background_image, 255 - mask)
composite_image = cv2.add(result, background)

# 결과 이미지 출력
cv2.imshow('Composite Image', composite_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
