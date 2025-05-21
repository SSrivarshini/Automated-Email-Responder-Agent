from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import pandas as pd
from transformers import pipeline
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

candidate_labels = ['spam', 'enquiry', 'complaint', 'support']

responses = {
    'spam': "This email seems like spam. No action needed.",
    'enquiry': "Thank you for your enquiry. We will get back to you shortly.",
    'complaint': "We're sorry for the inconvenience. Your complaint has been noted.",
    'support': "Our support team will assist you with your issue shortly."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    file = request.files['file']
    if file.filename == '':
        return 'No file selected'

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    df = pd.read_csv(filepath)

    predicted_labels = []
    generated_responses = []

    for email in df['text']:
        result = classifier(email, candidate_labels)
        label = result['labels'][0]
        predicted_labels.append(label)
        generated_responses.append(responses[label])

    df['predicted_label'] = predicted_labels
    df['generated_response'] = generated_responses

    result_filename = f"result_{file.filename}"
    result_path = os.path.join(RESULT_FOLDER, result_filename)
    df.to_csv(result_path, index=False)

    return render_template("result.html", data=df.to_dict(orient='records'), filename=result_filename)

@app.route('/submit_feedback/<filename>', methods=['POST'])
def submit_feedback(filename):
    # Get feedback responses
    feedbacks = request.form.getlist('edited_response')

    result_path = os.path.join(RESULT_FOLDER, filename)
    df = pd.read_csv(result_path)
    
    if len(feedbacks) == len(df):
        df['refined_response'] = feedbacks
        df.to_csv(result_path, index=False)

    return redirect(url_for('download_file', filename=filename))

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(RESULT_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
