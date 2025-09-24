import pandas as pd

#criar dados de vendas
gastos = {
    "Categoria": ["Alimentação", "Transporte", "Lazer", "Moradia", "Alimentação", "Transporte"],
    "Descrição": ["Supermercado", "Uber", "Cinema", "Aluguel", "Restaurante", "Ônibus"],
    "Valor": [250.00, 35.50, 50.00, 1200.00, 80.00, 5.00],
    "Data": ["2025-09-10", "2025-09-11", "2025-09-12", "2025-09-13", "2025-09-14", "2025-09-15"]
}

#Criar um dataframe (tabela)
gt = pd.DataFrame(gastos)

resumo = gt.groupby("Categoria")["Valor"].sum().reset_index()
print(gt)
print(resumo)

#Salvando as variáveis em um arquivo do excel
gt.to_excel("despesas.xlsx", index=False)
resumo.to_excel("resumo_despesas.xlsx", index=False)