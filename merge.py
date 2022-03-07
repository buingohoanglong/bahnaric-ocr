import os

path = 'manually_correct/'
files = os.listdir(path)
files.sort(key=lambda file_name: int(file_name[:-4]))

vi_sentences = []
ba_sentences = []
for file_name in files:
    with open(f'{path}{file_name}', encoding='utf-8', mode='r') as f:
        if int(file_name[:-4]) < 100:
            vi_sentences.extend(f.readlines())
        else:
            ba_sentences.extend(f.readlines())
print(len(vi_sentences))
print(len(ba_sentences))

with open(f'./suthihmong.vi', encoding='utf-8', mode='w') as f_vi:
    f_vi.writelines(vi_sentences)

with open(f'./suthihmong.ba', encoding='utf-8', mode='w') as f_ba:
    f_ba.writelines(ba_sentences)