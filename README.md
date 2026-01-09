# Spam Mail Detection using Machine Learning

This project implements a **Spam Email Detection system** using **Machine Learning and Natural Language Processing (NLP)**.  
The system classifies emails as **Spam** or **Ham (Not Spam)** using supervised learning models trained on textual data.

A **web-based interface** is developed using **HTML and CSS** to allow users to check emails in real time.

---

## 🔍 Project Overview
Spam emails pose serious security and productivity risks.  
This project aims to automatically identify spam emails by learning patterns from labeled email datasets using machine learning algorithms.

The full ML pipeline is implemented, including **text preprocessing, feature extraction, model training, evaluation, and prediction**.

---

## 🧠 Machine Learning Models Used

### ✅ Primary Model
- **Multinomial Naive Bayes**
  - Well-suited for text classification
  - Efficient and fast for large vocabularies
  - Commonly used in spam detection systems

### 🔁 Model Comparison
- **Logistic Regression**
  - Used to evaluate and compare performance
  - Helps understand linear decision boundaries in text classification

---

## ⚙️ ML Workflow
1. Load and explore dataset
2. Text preprocessing
   - Convert text to lowercase
   - Remove punctuation and unnecessary symbols
3. Feature extraction
   - **CountVectorizer** (Bag of Words model)
4. Train-test data splitting
5. Model training using supervised learning
6. Model evaluation using accuracy score
7. Predict spam/ham for user input

---

## 🌐 Web Application
- Built using **HTML and CSS**
- Simple, clean user interface
- Users can enter email content and receive instant predictions
- Backend logic connects the ML model to the UI

> Model files (`.pkl`) are intentionally **not included** to keep the implementation transparent and educational.

---

## 🧰 Technologies Used

### Programming & ML
- Python
- NumPy
- Pandas
- Scikit-learn

### NLP
- CountVectorizer
- Text preprocessing techniques

### Web Development
- HTML
- CSS
- Flask (for backend integration)

---

## 📂 Project Structure
