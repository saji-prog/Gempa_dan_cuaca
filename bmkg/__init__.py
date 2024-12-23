import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd

def data():
    url = 'https://www.bmkg.go.id/'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    dirasakan = []
    qwerty = soup.find_all('p', class_='mt-4 text-xl lg:text-2xl font-bold text-black-primary')
    for a in qwerty:
        print(a.text)#dirasakan
        dirasakan.append(a.text.strip())

    data = []
    sdf = soup.find_all('div', class_='px-4 py-3 border border-[#CBD5E1] rounded-xl')
    for b in sdf:
        print(b.text)#data
        data.append(b.text.strip())

    waktu = []
    zxc = soup.find_all('p', class_='mt-2 text-sm leading-[22px] font-medium text-gray-primary')
    for c in zxc:
        print(c.text)#waktu
        waktu.append(c.text.strip())

    daerah = []
    q1q = soup.find_all('h3', class_='text-xl font-medium')
    for d in q1q:
        print(d.text)#daerah
        daerah.append(d.text.strip())

    cuaca = []
    q2q = soup.find_all('p', class_='text-sm font-medium')
    for e in q2q:
        print(e.text)#cuaca
        cuaca.append(e.text.strip())

    suhu = []
    q3q = soup.find_all('p', class_='text-[32px] leading-[48px] font-bold mt-0.5')
    for f in q3q:
        print(f.text)#suhu
        suhu.append(f.text.strip())

    max_length = max(len(dirasakan), len(data), len(waktu), len(daerah), len(cuaca), len(suhu))
    dirasakan.extend([np.nan] * (max_length -  len(dirasakan)))
    data.extend([np.nan] * (max_length - len(data)))
    waktu.extend([np.nan] * (max_length - len(waktu)))
    daerah.extend([np.nan] * (max_length - len(daerah)))
    cuaca.extend([np.nan] * (max_length - len(cuaca)))
    suhu.extend([np.nan] * (max_length - len(suhu)))

    data = {
        'dirasakan': dirasakan,
        'daerah': daerah,
        'waktu': waktu,
        'cuaca': cuaca,
        'suhu': suhu
    }

    df = pd.DataFrame(data)
    file_path_excel = 'adadf1.xlsx'
    df.to_excel(file_path_excel, index=False)
    print('dadi', file_path_excel)
