# pip install matplotlib
import matplotlib.pyplot as plt
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
qtdTI = [60,   52,   76,   89,  108,   95]
qtdRH = [40,   72,   17,   28,   87,   56]
valores = []

plt.plot(meses, valores)
plt.plot(meses, qtdTI, label='TI', color='blue', linestyle="-", marker=".")
plt.plot(meses, qtdRH, label='RH', color='#00ff00', linestyle="--", marker="o")
plt.title('Chamados Abertos')
plt.xlabel('Meses')
plt.ylabel('Quantidade')
plt.legend()
plt.show()


plt.bar(meses, qtdTI, label='TI', color='blue', linestyle="-")
plt.bar(meses, qtdRH, label='RH', color='#00ff00', linestyle="--")
plt.title('Chamados Abertos')
plt.xlabel('Meses')
plt.ylabel('Quantidade')
plt.legend()
plt.show()

navegadores = ['Chrome', 'Firefox', 'Edge']
qtd = [1200, 600, 200]
cores = ['red', 'orange', 'blue']
plt.pie(qtd, labels=navegadores, colors=cores)
plt.show()
