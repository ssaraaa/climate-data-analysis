import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Veriyi yükle
csv_path = 'data/GlobalLandTemperaturesByCountry.csv'
df = pd.read_csv(csv_path)

print('İlk 5 satır:')
print(df.head())

print('\nVeri seti hakkında bilgi:')
df.info()

print('\nEksik veri sayısı:')
print(df.isnull().sum())

# Türkiye verisi
print('\nTürkiye verisi hazırlanıyor...')
turkiye = df[df['Country'] == 'Turkey'].copy()
turkiye['dt'] = pd.to_datetime(turkiye['dt'])
turkiye['year'] = turkiye['dt'].dt.year

# Yıllık ortalama sıcaklık
yillik_ortalama = turkiye.groupby('year')['AverageTemperature'].mean()

plt.figure(figsize=(12,6))
sns.lineplot(x=yillik_ortalama.index, y=yillik_ortalama.values)
plt.title("Türkiye'de Yıllara Göre Ortalama Sıcaklık")
plt.xlabel('Yıl')
plt.ylabel('Ortalama Sıcaklık (°C)')
plt.grid(True)
plt.tight_layout()
plt.savefig('turkiye_yillik_sicaklik.png')
plt.show()

print("Grafik 'turkiye_yillik_sicaklik.png' olarak kaydedildi.") 