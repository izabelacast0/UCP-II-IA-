import pandas as pd
import os

# nomes dos arquivos csv que você já gerou (sem o .csv no final)
llms = ["chatgpt", "gemini", "deepseek", "claude", "perplexity"]

pasta = os.path.dirname(os.path.abspath(__file__))
saida = os.path.join(pasta, "PRs_LLMs.xlsx")

with pd.ExcelWriter(saida, engine="openpyxl") as writer:
    for nome in llms:
        caminho_csv = os.path.join(pasta, f"{nome}.csv")
        df = pd.read_csv(caminho_csv)
        df.to_excel(writer, sheet_name=nome, index=False)
        print(f"Aba '{nome}' criada com {len(df)} linhas")

print(f"\nPlanilha salva em: {saida}")