# 🔗 URL Shortener Flask App

This is a **deployable URL Shortener web application** built using **Flask and SQLite**. It allows users to:

✅ Enter a long URL  
✅ Generates a unique short code  
✅ Saves it in the database  
✅ Redirects short URL visits to the original URL

---

---

## 💻 Technologies Used

- Python 3
- Flask
- Flask SQLAlchemy
- HTML, CSS

---

## 🗂️ Project Structure

app.py
templates/
└── index.html
urls.db
requirements.txt


---

## 📌 How to Run Locally

1. Clone the repo:

```bash
git clone https://github.com/Nabeel1537/URL_Shortener.git
cd URL_Shortener
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt

python app.py

Visit http://127.0.0.1:5000/ in your browser.

✨ Future Improvements
Custom user-defined short codes

Real-time analytics for clicks

User authentication for managing their links

📝 License
MIT License

✍️ Author
Nabeel Ahmed
