import streamlit as st
from PIL import Image
import numpy as np

# YOLOv8 (Ultralytics)
try:
    from ultralytics import YOLO
    model = YOLO("model/yolov8n.pt")  # تأكد إن الملف موجود أو عامل download_weights
except Exception as e:
    st.error("⚠️ لم يتم تحميل نموذج YOLOv8. تأكد من وجود الملف model/yolov8n.pt أو سكربت التحميل.")
    model = None

# إعداد الصفحة
st.set_page_config(
    page_title="Protect Your Children",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Protect Your Children — AI + IoT Child Safety System")
st.write("نظام ذكي يعتمد على **YOLOv8 + Arduino** للكشف عن الأطفال في مناطق خطرة أو اكتشاف أدوات حادة.")

# رفع صورة
uploaded_file = st.file_uploader("📤 ارفع صورة (jpg, jpeg, png)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # عرض الصورة الأصلية
    img = Image.open(uploaded_file)
    st.image(img, caption="📷 الصورة المرفوعة", use_column_width=True)

    if model is not None:
        # تشغيل النموذج
        results = model.predict(np.array(img))

        # استخراج الصورة مع المربعات
        annotated_img = results[0].plot()

        st.image(annotated_img, caption="✅ النتيجة بعد الكشف", use_column_width=True)

        # لو عايز تضيف تفاصيل إضافية
        st.subheader("🔎 التفاصيل:")
        for r in results[0].boxes:
            cls = int(r.cls[0])
            conf = float(r.conf[0])
            st.write(f"- Detected: {model.names[cls]} (conf: {conf:.2f})")

# تشغيل الكاميرا (اختياري)
if st.button("🎥 افتح الكاميرا"):
    st.write("⚠️ تشغيل الكاميرا غير مدعوم على Streamlit Cloud. استخدم محليًا فقط.")
