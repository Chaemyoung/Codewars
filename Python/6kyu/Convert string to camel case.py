def to_camel_case(text):
    words = text.replace('-', '_').split('_')
    camel_case_words = [words[0]] + [word.capitalize() for word in words[1:]]
    camel_case_text = ''.join(camel_case_words)
    return camel_case_text
