from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('model/spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('model/vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['email_text']
    data = vectorizer.transform([text])
    prediction = model.predict(data)[0]

    result = "Spam" if prediction == 0 else "Ham (Not Spam)"

    return render_template(
        'index.html',
        prediction_text=result,
        original_text=text
    )

if __name__ == '__main__':
    app.run(debug=True)
