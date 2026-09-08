# Exercício - Consumindo LLMs via API

Script em Python que usa a API GraphQL do GitHub para buscar pull requests
mescladas que citam links de compartilhamento de conversas com LLMs:
ChatGPT, Gemini, DeepSeek, Claude e Perplexity.

## Arquivos

- `consulta_github_prs.py` — script de coleta dos dados
- `chatgpt.csv`, `gemini.csv`, `deepseek.csv`, `claude.csv`, `perplexity.csv` — PRs coletadas por LLM
- `PRs_LLMs.xlsx` — dados organizados em planilha, uma aba por LLM
- `analise.md` — análise de uma PR de cada LLM, verificando como a conversa foi usada para ajudar na tarefa


