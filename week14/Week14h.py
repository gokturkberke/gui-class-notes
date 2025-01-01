# Install matplotlib: https://matplotlib.org/stable/
# Pie chart

import matplotlib.pyplot as plt

labels = ["Python", "Java", "C++", "JavaScript"]
sizes = [40, 30, 20, 10]
# Bir dilin daha belirgin olmasını sağlamak için patlatma (explode) kullanıyoruz
# Python dilinin diliminin biraz dışarıya patlatılmasını sağlıyoruz
explode = [0.1, 0, 0, 0]

fig, ax = plt.subplots()

ax.pie(sizes, labels=labels, explode=explode, 
       autopct="%.1f%%", # Yüzdeyi bir ondalıklı olarak gösteriyoruz
       shadow=True,  # Grafiğe gölge ekliyoruz
       startangle=90) # Grafiği saat yönünün tersine 90 derece döndürüyoruz

ax.set_title("Pie Chart")

plt.show()