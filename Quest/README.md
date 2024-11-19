pip install tensorflow numpy
۱. تنظیم بک‌اند برای مدل TensorFlow
مدل TensorFlow باید به یک سرویس بک‌اند (مثل Flask یا FastAPI در Python) متصل شود تا Angular بتواند از طریق API با آن ارتباط برقرار کند.

ایجاد بک‌اند با FastAPI:
یک فایل Python برای بک‌اند ایجاد کنید:

app.py:

اجرای سرور FastAPI:

pip install uvicorn

uvicorn app:app --reload
سرور شما در حال اجرا خواهد بود (معمولاً روی http://127.0.0.1:8000).


pip install fastapi

________________________________
#for create chat_model.h5: 
python questAI.py

________________________________
#how to run:
cd Quest
uvicorn app:app --reload

cd FormToExcel
ng serve