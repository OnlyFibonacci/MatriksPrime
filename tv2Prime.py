import glob
import pandas as pd
from datetime import datetime as dt


def zamanHesapla(timestamp):
    return dt.fromtimestamp(timestamp)


def ikiBasamak(veri):
    return float(f"{veri:.2f}")

def listeyeDondur(veri):
    return pd.Series(map(lambda x: ikiBasamak(x), veri))


def dosyadakiCSVler():
    all_data = pd.DataFrame()
    for f in glob.glob("*.csv"):
        df = pd.read_csv(f, sep=",")
        df.drop([0], axis=0, inplace=True)
        all_data = all_data.append(df)
    return all_data



def excelYap(okunacakCsv):
    df = pd.read_csv(okunacakCsv)
    df.drop([0], axis=0, inplace=True)
    tarihler = pd.Series(map(lambda x: str(zamanHesapla(x).date()), df['time']))
    saatler = pd.Series(map(lambda x: zamanHesapla(x).time(), df['time']))

    total = pd.DataFrame(
        {'Tarih': tarihler, 'Saat': saatler, 'Acilis': listeyeDondur(df['open']), 'Yuksek': listeyeDondur(df['high']), 'Dusuk': listeyeDondur(df['low']),
         'Kapanis': listeyeDondur(df['close']), 'HacimLot': listeyeDondur(df['Volume']), 'AOrt': 0})
    writer = pd.ExcelWriter(okunacakCsv + '.xlsx')
    total.to_excel(writer, sheet_name='Sayfa1', index=False)
    writer.save()


for csv in glob.glob("*.csv"):
    excelYap(csv)





