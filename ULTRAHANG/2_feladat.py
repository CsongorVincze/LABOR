import matplotlib.pyplot as plt

# 1. táblázat adatai: Az adó-vevő páros átviteli karakterisztikájának mérési adatai.
freq1 = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
amp1 = [10.0, 11.0, 10.0, 10.5, 9.5, 10.0, 9.5, 11.0, 174.0, 12.0, 11.5, 10.5, 10.0, 11.5, 10.0, 11.0, 10.5, 9.5, 9.5, 10.5, 9.5]

# 2. táblázat adatai: Rezonanciafrekvencia körüli adatpontok.
freq2 = [38.0, 39.0, 39.2, 39.4, 39.6, 39.8, 40.0, 40.2, 40.25, 40.26, 40.27, 40.28, 40.29, 40.3, 40.4, 40.5, 41.0]
amp2 = [35.0, 70.0, 78.5, 98.0, 118.0, 152.5, 172.0, 204.5, 208.5, 203.5, 202.0, 203.0, 201.0, 201.0, 189.5, 184.5, 67.5]

def plot_data():
    plt.figure(figsize=(6, 5))
    plt.plot(freq1, amp1, marker='o', linestyle='-', color='b')
    plt.title('Átviteli karakterisztika (Széles sáv)')
    plt.xlabel('Frekvencia [kHz]')
    plt.ylabel('Amplitúdó [mV]')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('2_feladat_diagram1.pdf')
    plt.close()

    plt.figure(figsize=(6, 5))
    plt.plot(freq2, amp2, marker='s', linestyle='-', color='r')
    plt.title('Rezonanciafrekvencia környezete')
    plt.xlabel('Frekvencia [kHz]')
    plt.ylabel('Amplitúdó [mV]')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('2_feladat_diagram2.pdf')
    plt.close()

if __name__ == '__main__':
    plot_data()

if __name__ == '__main__':
    plot_data()
