import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('../../msd_full.csv')

df['duration'] = df['duration'] * 1000

df = df[df['year'] != 0]
df = df[df['popularity'] != 0]
df = df[df['tempo'] != 0]

def tempo_classify(tempo):
    if tempo <= 39:
        return 1
    elif tempo > 39 and tempo <= 45:
        return 2
    elif tempo > 45 and tempo <= 50:
        return 3
    elif tempo > 50 and tempo <= 65:
        return 4
    elif tempo > 65 and tempo <= 69:
        return 5
    elif tempo > 69 and tempo <= 77:
        return 6
    elif tempo > 77 and tempo <= 97:
        return 7
    elif tempo > 97 and tempo <= 109:
        return 8
    elif tempo > 109 and tempo <= 132:
        return 9
    elif tempo > 132 and tempo <= 140:
        return 10
    elif tempo > 140 and tempo <= 177:
        return 11
    elif tempo > 177:
        return 12
    else:
        return None

df['tempo'] = df['tempo'].apply(tempo_classify)

print(df['tempo'].unique())

conteo = df.groupby(['year', 'tempo']).size()

with open('conteo.txt', 'w') as f:
    for (year, tempo), count in conteo.items():
        f.write(f"Year: {year}, Tempo: {tempo}, Count: {count}\n")

print("Conteo guardado en 'conteo.txt'")

ax = conteo.plot(kind='bar', stacked=True, figsize=(12, 8))

plt.title('Conteo de Valores de Tempo por Año')
plt.xlabel('Año')
plt.ylabel('Conteo')
plt.legend(title='Tempo', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y')

# Mostrar el gráfico
plt.tight_layout()
plt.show()