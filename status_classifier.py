# status_classifier.py
def classify_status(text):
    text = text.strip().lower()
    if not text or text in ['n/a', 'na', 'none']:
        return 'N/A'
    if '在校生' in text or 'in study' in text or 'student' in text:
        return 'In study'
    if '已工作' in text or 'working' in text:
        return 'Working'
    return 'N/A'
