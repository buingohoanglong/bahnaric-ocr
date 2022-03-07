from unicodedata import normalize

file = 'manually_correct/102.txt'

font_map = {
    'a\\': 'ă',
    'â\\': 'â\u0306',
    'o\\': 'o\u0306',
    'ô\\': 'ô\u0306',
    'ơ\\': 'ơ\u0306',
    'u\\': 'u\u0306',
    'ư\\': 'ư\u0306',
    'i\\': 'i\u0306',
    'e\\': 'e\u0306',
    'ê\\': 'ê\u0306',
    'A\\': 'Ă',
    'Â\\': 'Â\u0306',
    'O\\': 'O\u0306',
    'Ô\\': 'Ô\u0306',
    'Ơ\\': 'Ơ\u0306',
    'U\\': 'U\u0306',
    'Ư\\': 'ư\u0306',
    'I\\': 'I\u0306',
    'E\\': 'E\u0306',
    'Ê\\': 'Ê\u0306'
}

def taynguyenfont_correction(text):
    for k in font_map:
        text = text.replace(k, font_map[k])
    return text

with open(file, encoding='utf-8', mode='r') as f:
    lines = f.readlines()
    for line in lines:
        print(taynguyenfont_correction(line))