import sys
from playwright.sync_api import sync_playwright

SRC = '/home/claude/ig_week/src/'
OUT = '/home/claude/ig_week/car/'

CSS = '''
@font-face{font-family:Mont;font-weight:500;src:url(file:///root/.fonts/montserrat-latin-500-normal.ttf)}
@font-face{font-family:Mont;font-weight:600;src:url(file:///root/.fonts/montserrat-latin-600-normal.ttf)}
@font-face{font-family:Mont;font-weight:700;src:url(file:///root/.fonts/montserrat-latin-700-normal.ttf)}
@font-face{font-family:Mont;font-weight:800;src:url(file:///root/.fonts/montserrat-latin-800-normal.ttf)}
@font-face{font-family:Int;font-weight:400;src:url(file:///root/.fonts/inter-latin-400-normal.ttf)}
@font-face{font-family:Int;font-weight:500;src:url(file:///root/.fonts/inter-latin-500-normal.ttf)}
@font-face{font-family:Int;font-weight:600;src:url(file:///root/.fonts/inter-latin-600-normal.ttf)}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1440px;overflow:hidden}
.s{position:relative;width:1080px;height:1440px;overflow:hidden}
.paper{background:#EDF2FA;color:#0F1D35}
.navy{background:#0F1D35;color:#EDF2FA}
.gold{background:linear-gradient(135deg,#F3DE96 0%,#DCBB63 52%,#A9863F 100%)}
.goldtxt{color:#DCBB63}
.lab{font-family:Mont;font-weight:600;font-size:25px;letter-spacing:.2em;text-transform:uppercase}
.top{position:absolute;left:96px;right:96px;top:92px;display:flex;justify-content:space-between;align-items:center}
.paper .lab{color:#4F6283}
.navy .lab{color:#94A6C4}
.num{position:absolute;left:96px;top:170px;font-family:Mont;font-weight:800;font-size:250px;line-height:1;color:#0F1D35;letter-spacing:-.02em}
.bar{position:absolute;left:100px;top:432px;width:132px;height:10px;border-radius:5px}
h1,h2{font-family:Mont;font-weight:800}
h2{position:absolute;left:96px;top:476px;width:890px;font-size:76px;line-height:1.04;letter-spacing:-.01em}
.body{position:absolute;left:96px;top:600px;width:840px;font-family:Int;font-weight:500;font-size:38px;line-height:1.38;color:#4F6283}
.panel{position:absolute;left:96px;right:96px;top:820px;height:430px;background:#0F1D35;border-radius:40px;overflow:hidden}
.foot{position:absolute;left:96px;right:96px;bottom:84px;display:flex;justify-content:space-between;align-items:center}
.foot img{height:60px}
.dots{display:flex;gap:12px}
.dots i{display:block;width:18px;height:18px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#F3DE96,#DCBB63 55%,#A9863F)}
.bub{position:absolute;font-family:Int;font-weight:500;font-size:34px;line-height:1.3;padding:26px 34px;border-radius:30px;max-width:640px}
.in{background:#EDF2FA;color:#0F1D35;border-bottom-left-radius:8px}
.out{background:#5B93D6;color:#0A1526;border-bottom-right-radius:8px}
.meta{font-family:Int;font-weight:500;font-size:24px;color:#94A6C4;position:absolute}
.chip{position:absolute;font-family:Mont;font-weight:600;font-size:24px;letter-spacing:.12em;text-transform:uppercase;padding:12px 24px;border-radius:999px;border:2px solid #DCBB63;color:#DCBB63}
'''

def page(inner, cls):
    return '<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body><div class="s %s">%s</div></body></html>' % (CSS, cls, inner)

def top(label, i):
    return '<div class="top"><span class="lab">%s</span><span class="lab">%02d / 08</span></div>' % (label, i)

def foot():
    return '<div class="foot"><img src="file://%ssimbolo_claro.png"><div class="dots"><i></i><i></i><i></i></div></div>' % SRC

def check(i, num, title, body, panel):
    return page(top('Checagem %s de 06' % num, i) +
        '<div class="num">%s</div><div class="bar gold"></div><h2>%s</h2><div class="body">%s</div>' % (num, title, body) +
        '<div class="panel">%s</div>' % panel + foot(), 'paper')

# ---- panels ----
p1 = '''
<div class="chip" style="left:48px;top:48px">Conexão</div>
<div class="bub in" style="left:48px;top:140px;font-weight:600">API oficial da Meta</div>
<div style="position:absolute;left:48px;top:300px;display:flex;align-items:center;gap:18px"><span style="width:24px;height:24px;border-radius:50%" class="gold"></span><span style="font-family:Int;font-weight:600;font-size:34px;color:#EDF2FA">Conectado e pronto para enviar</span></div>
'''
p2 = '''
<div class="meta" style="left:48px;top:40px">Contato · 09:41</div>
<div class="bub in" style="left:48px;top:84px">Quero receber as ofertas da loja.</div>
<div class="chip" style="left:48px;top:214px">Consentimento registrado</div>
<div class="bub out" style="right:48px;top:306px;font-size:30px">Combinado, Ana! Só o que você pediu.</div>
'''
p3 = '''
<div style="position:absolute;left:96px;top:70px;bottom:70px;width:6px;background:#DCBB63;border-radius:3px"></div>
<div class="bub in" style="left:136px;top:50px;width:560px;padding:20px 30px"><b style="font-family:Mont;font-weight:700">Oferta</b> · Black Friday</div>
<div class="bub in" style="left:136px;top:170px;width:560px;padding:20px 30px"><b style="font-family:Mont;font-weight:700">Retorno</b> · Quem respondeu</div>
<div class="bub in" style="left:136px;top:290px;width:560px;padding:20px 30px"><b style="font-family:Mont;font-weight:700">Pós-venda</b> · Quem comprou</div>
<div style="position:absolute;left:88px;top:78px;width:22px;height:22px;border-radius:50%" class="gold"></div>
<div style="position:absolute;left:88px;top:198px;width:22px;height:22px;border-radius:50%" class="gold"></div>
<div style="position:absolute;left:88px;top:318px;width:22px;height:22px;border-radius:50%" class="gold"></div>
'''
def tick(x, h, t):
    return ('<div style="position:absolute;left:%dpx;bottom:96px;width:92px;height:%dpx;border-radius:18px 18px 0 0" class="gold"></div>'
            '<div class="meta" style="left:%dpx;bottom:50px;font-size:26px">%s</div>') % (x, h, x+14, t)
p4 = (tick(84,110,'09h') + tick(284,170,'11h') + tick(484,130,'14h') + tick(684,200,'17h') +
      '<div class="meta" style="left:48px;top:40px;font-size:28px">Envios ao longo do dia</div>'
      '<div style="position:absolute;left:48px;right:48px;bottom:96px;height:2px;background:#4F6283"></div>')
p5 = '''
<div class="meta" style="left:48px;top:44px">Modelo de mensagem</div>
<div class="bub out" style="left:48px;top:96px;font-size:36px;max-width:760px">Oi, {{nome}}! Sua oferta de Black Friday chegou.</div>
<div class="chip" style="left:48px;top:300px">Aprovado pela Meta</div>
'''
def col(x, title, cards):
    s = '<div style="position:absolute;left:%dpx;top:36px;width:262px;bottom:36px;background:#16294B;border-radius:26px;padding:22px 20px">' % x
    s += '<div style="font-family:Mont;font-weight:700;font-size:24px;letter-spacing:.1em;text-transform:uppercase;color:#DCBB63;margin-bottom:20px">%s</div>' % title
    for c in cards:
        s += '<div style="background:#EDF2FA;color:#0F1D35;border-radius:18px;padding:18px 20px;margin-bottom:16px;font-family:Int;font-weight:600;font-size:28px">%s</div>' % c
    return s + '</div>'
p6 = col(24, 'Respondeu', ['Ana', 'Carlos']) + col(313, 'Negociando', ['Marina']) + col(602, 'Comprou', ['Rafael'])

cover = page(
    top('Black Friday · Checklist', 1) +
    '<h1 style="position:absolute;left:96px;top:250px;width:890px;font-size:112px;line-height:1.02;letter-spacing:-.015em">Seu WhatsApp está <span class="goldtxt">pronto</span> para a Black Friday?</h1>'
    '<div style="position:absolute;left:96px;top:800px;width:800px;font-family:Int;font-weight:500;font-size:42px;line-height:1.35;color:#94A6C4">6 checagens para fazer hoje.</div>'
    '<div class="bub in" style="left:96px;top:980px;font-size:36px;max-width:700px">Vocês têm oferta de Black Friday?</div>'
    '<div class="bub in" style="left:96px;top:1120px;padding:24px 34px;display:flex;gap:12px;align-items:center"><span style="width:16px;height:16px;border-radius:50%;background:#94A6C4;display:block"></span><span style="width:16px;height:16px;border-radius:50%;background:#94A6C4;display:block"></span><span style="width:16px;height:16px;border-radius:50%;background:#94A6C4;display:block"></span></div>'
    '<div class="lab" style="position:absolute;right:96px;bottom:92px;color:#DCBB63">Arraste</div>',
    'navy')

cta = page(
    top('Para fechar', 8) +
    '<h1 style="position:absolute;left:96px;top:300px;width:890px;font-size:104px;line-height:1.03;letter-spacing:-.015em">Faltou algum <span class="goldtxt">ponto</span>?</h1>'
    '<div style="position:absolute;left:96px;top:690px;width:840px;font-family:Int;font-weight:500;font-size:44px;line-height:1.38;color:#EDF2FA">Fale com um representante da LeadPush pelo link da bio e deixe o seu WhatsApp pronto a tempo.</div>'
    '<div style="position:absolute;left:96px;top:1010px;width:840px;font-family:Int;font-weight:500;font-size:34px;line-height:1.4;color:#94A6C4">Salve este checklist para conferir amanhã.</div>'
    '<div class="gold" style="position:absolute;left:96px;top:1130px;width:120px;height:10px;border-radius:5px"></div>'
    '<img src="file://%scomslogan_escuro.png" style="position:absolute;left:96px;bottom:88px;height:112px">' % SRC,
    'navy')

slides = [
    cover,
    check(2, '01', 'API oficial', 'Seu número conectado pelo caminho que a Meta reconhece, e não por atalhos.', p1),
    check(3, '02', 'Consentimento', 'Só contatos que aceitaram receber a sua mensagem. É o ponto de partida de uma operação dentro das regras.', p2),
    check(4, '03', 'Mensagens por funil', 'Cada contato recebe a sequência certa, e não a mesma mensagem para todo mundo.', p3),
    check(5, '04', 'Cadência controlada', 'Envios distribuídos no ritmo certo, e não tudo de uma vez. Quem responde é atendido sem fila.', p4),
    check(6, '05', 'Modelos aprovados', 'Os modelos de mensagem passam pela aprovação da Meta. Deixe tudo aprovado antes do dia.', p5),
    check(7, '06', 'Histórico e Kanban', 'Veja quem respondeu, quem está negociando e quem comprou, sem planilha.', p6),
    cta,
]

with sync_playwright() as p:
    b = p.chromium.launch(args=['--allow-file-access-from-files'])
    pg = b.new_page(viewport={'width': 1080, 'height': 1440}, device_scale_factor=1)
    for i, h in enumerate(slides, 1):
        f = '/home/claude/ig_week/car/s%d.html' % i
        open(f, 'w').write(h)
        pg.goto('file://' + f)
        pg.wait_for_timeout(500)
        pg.screenshot(path=OUT + 'slide_%02d.png' % i)
    b.close()
print('ok')
