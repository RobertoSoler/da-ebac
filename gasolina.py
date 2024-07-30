import pandas as pd
import matplotlib.pyplot as plt
gasolina_df = pd.read_csv("/content/da-ebac/gasolina.csv")
gasolina_df.head()
plt.plot(gasolina_df["venda"])
plt.savefig("gasolina.png",orientation ='landscape')
plt.show()