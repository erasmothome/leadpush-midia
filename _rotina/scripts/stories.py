from playwright.sync_api import sync_playwright
SRC='/home/claude/ig_week/src/'
CSS='''@font-face{font-family:Mont;font-weight:800;src:url(file:///root/.fonts/montserrat-latin-800-normal.ttf)}
@font-face{font-family:Mont;font-weight:600;src:url(file:///root/.fonts/montserrat-latin-600-normal.ttf)}
@font-face{font-family:Int;font-weight:500;src:url(file:///root/.fonts/inter-latin-500-normal.ttf)}
*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1920px;background:#0F1D35}
#c{position:relative;width:1080px;height:1920px;background:linear-gradient(180deg,#0F1D35,#0A1526);overflow:hidden}
.a{position:absolute}.lab{font-family:Mont;font-weight:600;font-size:30px;letter-spacing:.2em;text-transform:uppercase;color:#DCBB63}
.h{font-family:Mont;font-weight:800;color:#EDF2FA;letter-spacing:-.015em}.g{color:#DCBB63}
.p{font-family:Int;font-weight:500;font-size:44px;line-height:1.35;color:#C9D4E6}
.ln{height:6px;width:120px;background:linear-gradient(90deg,#F3DE96,#A9863F);border-radius:4px}'''
def page(body): return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div id="c">{body}</div></body></html>'
logo=f'<img class="a" src="file://{SRC}comslogan_escuro.png" style="left:90px;top:270px;width:420px">'
S={
'Story_quarta_enquete':logo+'<div class="a lab" style="left:90px;top:620px">Pergunta rápida</div><div class="a h" style="left:90px;top:690px;width:900px;font-size:92px;line-height:1.06">Hoje, seus leads ficam em <span class="g">planilha, caderno</span> ou <span class="g">sistema?</span></div><div class="a ln" style="left:90px;top:1130px"></div><div class="a p" style="left:90px;top:1170px;width:900px">Vote abaixo. Eu conto o resultado amanhã.</div>',
'Story_quinta_caixa_perguntas':logo+'<div class="a lab" style="left:90px;top:620px">Pergunte à LeadPush</div><div class="a h" style="left:90px;top:690px;width:900px;font-size:92px;line-height:1.06">Qual a sua maior dúvida sobre <span class="g">disparo no WhatsApp?</span></div><div class="a ln" style="left:90px;top:1180px"></div><div class="a p" style="left:90px;top:1220px;width:900px">Mande a pergunta. Eu respondo aqui nos próximos Stories.</div>',
'Story_sexta_link':logo+'<div class="a lab" style="left:90px;top:600px">Black Friday</div><div class="a h" style="left:90px;top:670px;width:900px;font-size:100px;line-height:1.05">Seu WhatsApp está <span class="g">pronto?</span></div><div class="a p" style="left:90px;top:1010px;width:900px">Fale agora com um representante da LeadPush e organize suas respostas hoje.</div><div class="a ln" style="left:90px;top:1190px"></div>',
}
with sync_playwright() as p:
    b=p.chromium.launch(args=['--allow-file-access-from-files']); pg=b.new_page(viewport={'width':1080,'height':1920})
    for n,body in S.items():
        open(f'stories/{n}.html','w').write(page(body)); pg.goto(f'file:///home/claude/ig_week/stories/{n}.html'); pg.wait_for_timeout(500)
        pg.screenshot(path=f'stories/{n}.png')
    b.close()
from PIL import Image
ims=[Image.open(f'stories/{n}.png').resize((360,640)) for n in S]
W=Image.new('RGB',(370*3,640),'#888')
for i,im in enumerate(ims): W.paste(im,(i*370,0))
W.save('stories/prev.png')
