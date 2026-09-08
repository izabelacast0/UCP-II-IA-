## ChatGPT
PR: https://github.com/faker-js/faker/pull/2658
Link da conversa: https://chat.openai.com/share/bbb3bb28-cb2d-436e-beb8-af36537c0897

O desenvolvedor estava ajustando a configuração de fim de linha (eol=lf) 
de um arquivo .gitattributes. Ele usou o ChatGPT como referência, ao lado 
da documentação oficial do Git, para entender a diferença de comportamento 
entre a opção "text eol=lf" e a alternativa mais simples "-text" antes de 
decidir qual aplicar. O LLM funcionou aqui como apoio para pesquisa/estudo 
de um conceito técnico, não para gerar o código da mudança em si.

## Perplexity
PR: https://github.com/ImagingDataCommons/gcp-dicomweb-proxy/pull/1
Link da conversa: https://www.perplexity.ai/search/i-am-trying-to-deploy-a-google-BjRoJupjQ2eup440PQOEAQ

O desenvolvedor usou o Perplexity para resolver um problema de deploy 
relacionado ao Google Cloud (o projeto é um proxy DICOMweb hospedado no GCP). 
Ele credita explicitamente o Perplexity como "co-autor" da solução no 
comentário da PR, e confirma que a abordagem sugerida funcionou. Aqui o LLM 
foi usado como assistente de debugging/configuração de infraestrutura, com 
o link da conversa citado como fonte da solução aplicada.

## Gemini
PR: https://github.com/p-doom/jasmine/pull/128
Link da conversa: https://g.co/gemini/share/c06c2e6f3281

O desenvolvedor estava corrigindo um bug na aplicação do positional encoding 
(PE) num modelo Transformer usado num projeto de pesquisa (jasmine). Ele usou 
o Gemini para confirmar/entender a arquitetura correta: que o positional 
encoding deve ser aplicado uma única vez, nos embeddings de entrada, antes 
de entrarem nos blocos do Transformer — não repetidamente dentro de cada 
bloco (STBlock), como o código fazia antes. O link da conversa foi citado 
como referência técnica que embasou a correção aplicada no commit.

## Claude
PR: https://github.com/afeather07/recovery-together/pull/6
Link da sessão: https://claude.ai/code/session_01X1Vo3j5uNDVuugLZBYjenL

Nota: o link é de uma sessão do Claude Code (claude.ai/code/session/...), 
um padrão diferente de claude.ai/share/ usado na busca original — mas ainda 
assim é um exemplo direto de uso do Claude.

Essa PR foi inteiramente gerada pelo Claude Code: o dono do repositório pediu 
que o e-mail de notificação deixasse explícito que os dados nunca são 
vendidos/compartilhados. O Claude entendeu que a funcionalidade já existia 
parcialmente e ajustou apenas o texto de privacidade em três lugares onde o 
e-mail é solicitado/descrito. Aqui o LLM não apenas orientou o desenvolvedor 
— ele escreveu e aplicou o código da mudança diretamente.

## DeepSeek
PR: https://github.com/hrydgard/ppsspp/pull/21648
Link da conversa: https://chat.deepseek.com/share/980xe4c2ue35te8cy2

O desenvolvedor usou o DeepSeek para ajudar a otimizar o rasterizador por 
software (soft GPU) do emulador PPSSPP, removendo 2 casos desnecessários do 
fast path relacionados a depth/fog. O próprio título da PR credita a 
sugestão ao DeepSeek. O link da conversa foi citado como justificativa 
técnica de que o impacto na performance seria mínimo, já que os casos 
removidos são raros e o fallback continua funcional. O mantenedor do 
projeto revisou e aprovou a mudança.
