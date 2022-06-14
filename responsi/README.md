# RESPONSI WORKSHOP (Python)

```python
import numpy as np
import pandas as pd
import seaborn as sns
sns.set()
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv('day_wise.csv')
df.head()
```
Seaborn berfungsi untuk memproduksi visualisasi dengan Python dan 
memiliki beberapa kelebihan dibandingkan dengan Matplotlib yaitu, hasil 
visualisasi Seaborn diklaim lebih bagus dan indah juga menggunakan 
serangkaian kode yang lebih mudah. Seaborn adalah library 
untuk membuat grafik dan statistik dengan menggunakan Python. Library 
ini di bangun berdasarkan library matplotlib serta terintegrasi dengan 
struktur data pada panda.

pada kode diatas di gunakan untuk visualisasi data day_wise.csv

```python
df.info()
```
Df.info( ) berfungsi untuk melihat nomor index beserta tipe datanya