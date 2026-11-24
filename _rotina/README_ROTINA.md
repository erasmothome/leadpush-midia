# Rotina semanal de Instagram da LeadPush (@lead.push)

Responsável: Erasmo Thomé (Sócio e Diretor de Expansão). Idioma: português do Brasil. Tom: profissional, direto, positivo, com cara de texto escrito por pessoa. Nunca usar travessão longo nem curto em nenhum texto (legendas, comentários, artes, mensagens). Postura de analista crítico: avaliar a própria entrega antes de enviar e evitar repetição de fórmulas entre semanas (identidade da marca sim, mesmice não).

## Objetivo
Toda segunda de manhã montar a semana inteira, o Erasmo aprova em uma mensagem, e tudo é agendado no Buffer para sair sozinho. Ele só publica manualmente os Stories e o primeiro comentário.

## Fluxo da segunda-feira
1. Rodar `bash _rotina/setup.sh` (recria fontes, logos, scripts e imagens).
2. Ler `_rotina/historico.md` (o que já foi publicado, formatos e músicas usados) para não repetir hook, formato, música nem estrutura.
3. Olhar o desempenho da semana anterior com `get_aggregated_post_metrics` e `list_posts` (Buffer, organização "My organization", id 6b04d058167cf430560a9957). Resumir em 3 linhas o que funcionou.
4. Montar o pacote da semana (mesmo calendário, formatos variados):
   - Quarta 18h: Reel curto "Funil da Semana #N" (alcance e seguidores). Mostrar um funil/recurso diferente a cada semana, usando telas reais do sistema.
   - Quinta 18h: carrossel 1080x1440 (salvamentos e comentários), tema útil e salvável.
   - Sexta 18h: Reel de formato diferente do da quarta (cliques para o WhatsApp).
   - Ajustar ao calendário (feriado, Black Friday, Cyber Monday, Natal, fim de mês). Se a semana tiver feriado ou data comercial, adaptar o tema.
   - Stories manuais nos mesmos dias (arte de fundo 1080x1920 com a parte de baixo livre para enquete, caixa de perguntas ou link), com horário e instrução de cada um.
   - Texto do primeiro comentário de cada post.
5. Construir as mídias, conferir cada frame ou slide (texto cortado, sobreposição, margem de segurança) e conferir fatos. Enviar o pacote ao Erasmo (SendUserMessage e SendUserFile) pedindo aprovação ou ajustes. Se ele não responder, não agendar nada.
6. Depois da aprovação: criar pasta `AAAA-MM-DD_semana-N` neste repositório com as mídias, fazer commit e push em main, e agendar os 3 posts no Buffer. Atualizar `historico.md`. Conferir com `list_posts` que os 3 estão com status scheduled e sem erro. Avisar o resultado e o que ele precisa fazer à mão.

## Buffer (já conectado)
- Canal Instagram: lead.push, id 6b04d14d8541f09ecb7fe730 (conta business).
- `create_post` com `schedulingType: automatic`, `mode: customScheduled`, `dueAt` em ISO 8601 com offset -03:00 (America/Sao_Paulo), nunca a fila.
- Reel: `assets: [{video:{url}}]`, `metadata.instagram: {type:"reel", shouldShareToFeed:true, isAiGenerated:false}`.
- Carrossel: `assets` com até 10 imagens, cada uma com altText, `metadata.instagram.type:"post"`.
- URL da mídia: `https://raw.githubusercontent.com/erasmothome/leadpush-midia/main/<pasta>/<arquivo>` (repositório público, funciona no Buffer).
- Não enviar `firstComment`: o plano gratuito recusa ("requires a paid plan"). O Erasmo posta o primeiro comentário à mão logo após a publicação.
- Plano gratuito: 3 canais, 10 posts agendados. Stories com enquete ou caixa de perguntas não são agendáveis.
- Música em alta do Instagram não entra por agendamento. Usar trilha original gerada com `scripts/music.py` e misturar no vídeo (comando no fim do arquivo). Uma trilha diferente para cada Reel, mudando bpm, semente e progressão.
- Arquivos de vídeo até cerca de 3 MB para poder subir pelo Chrome se for preciso (plano B: compor o post no Buffer aberto no Chrome do Erasmo).

## Regras de conteúdo
- Tom positivo no primeiro contato. Nada de medo, ameaça ou "quem não faz perde". Mostrar a solução.
- Não inventar número, depoimento, cliente ou resultado. Telas do sistema só reais. Dados de clientes (nome, telefone, foto) nas telas devem ser desfocados antes de qualquer publicação. A arte `assets/kanban_anon.png` já está anonimizada. Nunca commitar print original com dados de terceiros.
- Não escrever que a IA "não vem pronta". Verdade a usar: existe uma IA embutida no sistema que ensina o cliente (onde fica o Kanban, como fazer disparos, como subir uma base de clientes).
- A Lídia (apresentadora do Reel fixado) não leva rótulo de "assistente virtual". Se um vídeo usar pessoa gerada por IA, ligar o rótulo de IA no Buffer (`isAiGenerated: true`).
- "Resultados variam" permanece nos vídeos que mostram resultado.
- Chamada para ação: "Fale com um representante da LeadPush" e link na bio. Link do WhatsApp com mensagem pronta: `https://wa.me/5541991761993?text=Oi,+vim+pelo+Instagram+e+quero+falar+com+um+representante+da+LeadPush` (usar `+` no lugar de espaço, nunca `%20`).
- Máximo 5 hashtags por legenda. Legenda: primeira linha forte (é indexada na busca), pedido de envio ou salvamento, uma pergunta.
- Nome do perfil: "LeadPush | A Evolução do Disparo Inteligente". Alterar para "LeadPush | Automação e Disparo no WhatsApp" quando o Instagram liberar (14 dias de trava desde 23/11/2026).

## Identidade visual
- Paleta: fundo navy #0F1D35 e #0A1526, texto #EDF2FA, dourado #DCBB63 (gradiente #F3DE96, #DCBB63, #A9863F), apoio #94A6C4 e #16294B, papel claro nos slides de checklist.
- Fontes: Montserrat 800 e 600 para títulos, Inter 500 e 600 para texto (em `fonts/`).
- Logo: `assets/src/comslogan_escuro.png` e `simbolo_escuro.png` em fundo escuro; `comslogan_claro.png` e `simbolo_claro.png` em fundo claro. Nunca recriar o logo.
- Reels 1080x1920, 30 fps, h264, yuv420p, faixa de áudio obrigatória. Conteúdo importante entre y 250 e 1500. Carrossel 1080x1440. Stories 1080x1920 com margem livre em cima (250) e embaixo (340).
- Renderização: HTML mais Playwright, captura quadro a quadro e ffmpeg (ver scripts). Os scripts são modelos: trocar conteúdo, não repetir o mesmo layout toda semana.
- Telas reais do sistema em `assets/shots/` (fluxos, painel, disparo, menu, IA, tutorial, conexão, departamentos) e o Kanban em `assets/kanban_anon.png`. Pedir novas telas ao Erasmo quando faltar.

## Stories (manuais)
Cada semana entregar: arte de fundo, qual recurso do app colocar (enquete, caixa de perguntas, link, quiz, contagem regressiva), horário sugerido (cerca de 17h30 a arte, 18h05 compartilhar o post) e o texto de resposta. Só prometer no Story o que o Erasmo consegue cumprir.

## Outras alavancas semanais
Responder comentários na primeira hora, 10 comentários substantivos por dia em perfis de empresários brasileiros, impulsionar no domingo a melhor peça (só Brasil, versão "Saiba mais"), post em colaboração com Diogo e Francis quando fizer sentido, Reels de teste só em peças que não serão fixadas.
