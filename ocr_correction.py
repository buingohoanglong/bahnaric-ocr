import os
from unicodedata import normalize

dict = {
    'ð': 'ơ̆', 
    'ẽ': 'ĕ', 
    '¡': 'i', 
    'mĩ': 'mĭ', 
    'ợ': 'ơ', 
    'ồ': 'ŏ', 
    'ố': 'ơ̆', 
    'ỗ': 'ô̆', 
    'ơi': 'ơĭ', 
    'ổi': 'ôĭ', 
    'š': 'ĕ', 
    'Š': 'ê̆', 
    'ủ': 'ŭ', 
    'Ủ': 'Ŭ', 
    'ũ': 'ŭ', 
    'Ũ': 'Ŭ',
    # new
    '“': '\'',
    # 'ỡ': 'ơ\u0306',
    # 'ã': 'ă',
    # 'a\u0308': 'ă',
    # 'ĩ': 'i\u0306',
    # 'ữ': 'ư\u0306',
    # 'ờ': 'ơ\u0306',
    # 'ừ': 'ư\u0306',
    # 'í': 'i\u0306',
    # 'ễ': 'ê\u0306',
    # 'ị': 'i',
    # 'ụ': 'u',
    # 'o\u0308': 'o\u0306',
    # 'ù': 'u\u0306',
    # 'õ': 'o\u0306',
    '\u0300': '\u0306',
    '\u0301': '\u0306',
    '\u0303': '\u0306',
    '\u0309': '\u0306',
    '\u0323': '',
    '\u0308': '\u0306'
}

def ocr_correction(text):
    text = normalize('NFD', text)
    for original, replace in dict.items():
        text = text.replace(normalize('NFD', original), normalize('NFD', replace))
    return normalize('NFC', text)

path = 'C:/Users/meeph/Downloads/OCR_result-20220214T095437Z-001/OCR_result/manually_correct/'
new_path = 'manually_correct/'
files = os.listdir(path)
files.sort(key=lambda file_name: int(file_name[:-4]))

for file_name in files:
    if int(file_name[:-4]) >= 100:
        lines = []
        with open(f'{path}{file_name}', encoding='utf-8', mode='r') as f:
            lines = f.readlines()
            lines = [ocr_correction(l) for l in lines]
            for l in lines:
                print(l)
        with open(f'{new_path}{file_name}', encoding='utf-8', mode='w') as f:
            f.writelines(lines)
            
