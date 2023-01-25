def get_interview(text_uri):
    with open(text_uri, 'r', encoding='utf-8') as f:
        return f.read()