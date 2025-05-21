"""
helpers.py - Utility functions and reusable components for the email classification agent.
Note: These are not used in app.py but demonstrate how logic could be modularized.
"""

from transformers import pipeline

# Load the zero-shot classifier
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define possible labels for classification
candidate_labels = ['spam', 'enquiry', 'complaint', 'support']

# Predefined responses based on classification label
responses = {
    'spam': "This email seems like spam. No action needed.",
    'enquiry': "Thank you for your enquiry. We will get back to you shortly.",
    'complaint': "We're sorry for the inconvenience. Your complaint has been noted.",
    'support': "Our support team will assist you with your issue shortly."
}

def classify_email(email_text):
    """
    Classify a single email and return the label and response.
    """
    result = classifier(email_text, candidate_labels)
    label = result['labels'][0]
    return label, responses[label]
