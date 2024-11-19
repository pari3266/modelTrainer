from fastapi import FastAPI
from pydantic import BaseModel
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from fastapi.middleware.cors import CORSMiddleware

# ایجاد اپلیکیشن FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# لود کردن مدل
model = load_model("chat_model.h5")

# تعریف داده‌های اولیه
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

# ایجاد Tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(questions + answers)
max_len = 10  # حداکثر طول سوال‌ها

# مدل درخواست
class QuestionRequest(BaseModel):
    question: str

# پیش‌بینی پاسخ
@app.post("/predict")
def predict(request: QuestionRequest):
    question = request.question
    question_seq = tokenizer.texts_to_sequences([question])
    question_padded = pad_sequences(question_seq, maxlen=max_len, padding='post')
    prediction = model.predict(question_padded)
    predicted_seq = prediction.argmax(axis=-1)[0]
    response = tokenizer.sequences_to_texts([predicted_seq.tolist()])[0]

    return {"answer": response}