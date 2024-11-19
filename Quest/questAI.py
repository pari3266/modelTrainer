import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# داده‌های آموزشی
questions = [
    "محصول شما چیست؟",
    "چطور از محصول استفاده کنیم؟",
    "هزینه محصول چقدر است؟",
    "آیا ارسال رایگان دارید؟",
    "چند روز طول می‌کشد تا محصول برسد؟"
]

answers = [
    "محصول ما یک دستگاه هوشمند خانگی است.",
    "برای استفاده، دستگاه را به برق متصل کنید و اپلیکیشن ما را نصب کنید.",
    "هزینه محصول 1 میلیون تومان است.",
    "بله، برای خریدهای بالای 500 هزار تومان ارسال رایگان داریم.",
    "ارسال معمولاً 3 تا 5 روز کاری طول می‌کشد."
]

# پیش‌پردازش داده‌ها
tokenizer = Tokenizer()
tokenizer.fit_on_texts(questions + answers)
vocab_size = len(tokenizer.word_index) + 1

# تبدیل سوال‌ها و جواب‌ها به توکن
questions_seq = tokenizer.texts_to_sequences(questions)
answers_seq = tokenizer.texts_to_sequences(answers)

# تعیین حداکثر طول و پدینگ توالی‌ها
max_len = max(len(seq) for seq in questions_seq + answers_seq)
questions_padded = pad_sequences(questions_seq, maxlen=max_len, padding='post')
answers_padded = pad_sequences(answers_seq, maxlen=max_len, padding='post')

# آماده‌سازی داده‌های ورودی و خروجی
answers_input = answers_padded[:, :-1]  # حذف آخرین کلمه برای ورودی
answers_target = answers_padded[:, 1:]  # حذف اولین کلمه برای هدف
answers_target = answers_target.reshape(-1, max_len - 1)  # تغییر شکل هدف

# ساخت مدل
model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=64, input_length=max_len - 1),
    Bidirectional(LSTM(64, return_sequences=True)),
    Dense(vocab_size, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# آموزش مدل
model.fit(answers_input, answers_target, epochs=100, verbose=2)

# ذخیره مدل به صورت .h5
model.save("chat_model.h5")
print("مدل با موفقیت ذخیره شد.")
