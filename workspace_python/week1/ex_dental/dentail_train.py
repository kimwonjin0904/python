import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
from keras.applications import VGG16
from keras import Sequential
from keras.layers import Flatten, Dense, Dropout
from keras.preprocessing.image import ImageDataGenerator

# 데이터 경로 설정
#train_dir = '../../dataset/dental_image/train'
#test_dir = '../../dataset/dental_image/test'
train_dir = '../../dataset/whale'
test_dir = '../../dataset/whale_split'
# 데이터 증강 설정
train_datagen = ImageDataGenerator(
    rotation_range=180,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    vertical_flip=True,
    brightness_range=[0.5, 1.5]
)
test_datagen = ImageDataGenerator()

# 데이터 로딩
train_generator = train_datagen.flow_from_directory(
    train_dir, target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)
test_generator = test_datagen.flow_from_directory(
    test_dir, target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)
class_num = len(train_generator.class_indices)
print('labels:', train_generator.class_indices)
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
for layer in base_model.layers:
    layer.trainable = False

# Fine-tuning을 위한 모델 구성
model = Sequential([
    base_model,
    Flatten(),
    Dense(1024, activation='relu'),
    Dropout(0.5),
    Dense(class_num, activation='softmax')
])
model.summary()
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])

# 모델 학습
history = model.fit(
    train_generator,
    steps_per_epoch=len(train_generator),
    epochs=100,
    validation_data=test_generator,
    validation_steps=len(test_generator)
)

# 모델 저장
model.save('whale20.h5')

# 학습 결과 시각화
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(history.history['acc'], label='train acc')
plt.plot(history.history['val_acc'], label='val acc')
plt.xlabel('epochs')
plt.ylabel('acc')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='val loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()

plt.tight_layout()
plt.show()
