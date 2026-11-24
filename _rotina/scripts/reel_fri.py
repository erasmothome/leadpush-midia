import os, subprocess
from playwright.sync_api import sync_playwright

W, H, FPS, T = 1080, 1920, 30, 15.0
SRC = '/home/claude/ig_week/src/'
FR = '/home/claude/ig_week/frames_fri/'
OUT = '/home/claude/ig_week/Reel_sexta_Black_Friday.mp4'

HTML = '''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Mont;font-weight:600;src:url(file:///root/.fonts/montserrat-latin-600-normal.ttf)}
@font-face{font-family:Mont;font-weight:800;src:url(file:///root/.fonts/montserrat-latin-800-normal.ttf)}
@font-face{font-family:Int;font-weight:500;src:url(file:///root/.fonts/inter-latin-500-normal.ttf)}
@font-face{font-family:Int;font-weight:600;src:url(file:///root/.fonts/inter-latin-600-normal.ttf)}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;background:#0F1D35}
#c{position:relative;width:1080px;height:1920px;overflow:hidden;background:linear-gradient(180deg,#0F1D35 0%,#0A1526 100%)}
.abs{position:absolute}
.gold{background:linear-gradient(135deg,#F3DE96 0%,#DCBB63 52%,#A9863F 100%)}
.h{font-family:Mont;font-weight:800;color:#EDF2FA;letter-spacing:-.015em}
.lab{font-family:Mont;font-weight:600;font-size:30px;letter-spacing:.2em;text-transform:uppercase}
.pan{left:72px;width:936px;height:600px;border-radius:40px;overflow:hidden;border:2px solid rgba(148,166,196,.35);background:#0A1526}
.mb{position:absolute;font-family:Int;font-weight:600;font-size:38px;padding:16px 28px;border-radius:28px;background:#94A6C4;color:#0F1D35;white-space:nowrap;transform-origin:50% 50%}
.cd{position:absolute;width:262px;font-family:Int;font-weight:600;font-size:30px;padding:16px 20px;border-radius:20px;background:#EDF2FA;color:#0F1D35;white-space:nowrap;overflow:hidden}
.col{position:absolute;top:92px;width:278px;height:480px;border-radius:26px;background:#16294B}
.cl{position:absolute;top:104px;width:278px;text-align:center;font-family:Mont;font-weight:700;font-size:24px;letter-spacing:.12em;text-transform:uppercase;color:#DCBB63}
</style></head><body><div id="c">
<div id="hook">
  <div class="abs lab" style="left:90px;top:620px;color:#DCBB63" id="hk0">Black Friday</div>
  <div class="abs h" id="hk1" style="left:90px;top:690px;width:900px;font-size:124px;line-height:1.04">Qual lado é <span style="color:#DCBB63">o seu?</span></div>
</div>
<div id="split" style="opacity:0">
  <div class="abs lab" style="left:90px;top:236px;color:#94A6C4">Sem funil</div>
  <div class="abs pan" id="pt" style="top:290px" ><div id="topin"></div></div>
  <div class="abs lab" style="left:90px;top:900px;color:#DCBB63">Com funil</div>
  <div class="abs pan" id="pb" style="top:954px"><div id="botin"></div></div>
  <div class="abs" style="left:90px;top:1580px;font-family:Int;font-weight:500;font-size:28px;color:#94A6C4">Ilustração do fluxo de atendimento</div>
</div>
<div id="end" style="opacity:0">
  <div class="abs h" style="left:90px;top:520px;width:900px;font-size:108px;line-height:1.05">Cada resposta no <span style="color:#DCBB63">lugar certo.</span></div>
  <div class="abs" style="left:90px;top:900px;width:880px;font-family:Int;font-weight:500;font-size:46px;line-height:1.35;color:#EDF2FA">Fale com um representante da LeadPush.</div>
  <div class="abs gold" id="pill" style="left:90px;top:1080px;padding:40px 76px;border-radius:999px;font-family:Mont;font-weight:800;font-size:56px;color:#0A1526;transform-origin:0 50%">Link na bio</div>
  <img class="abs" src="file://__SRC__comslogan_escuro.png" style="left:90px;top:1340px;width:620px">
</div>
</div>
<script>
const clamp=(x,a,b)=>Math.max(a,Math.min(b,x));
const seg=(t,a,b)=>clamp((t-a)/(b-a),0,1);
const ease=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const eo=x=>1-Math.pow(1-x,3);
const MB=[["Oi",60,70,-4],["Preço?",300,40,3],["Tem?",640,90,-2],["Alô?",170,170,5],["Quanto?",470,200,-5],["Cadê meu pedido?",470,310,3],["Oi?",70,300,-3],["Tem no azul?",260,350,4],["Alô???",660,440,-6],["Qual o prazo?",60,450,2],["Oi, tem?",400,490,-3],["Preço?",330,250,6]];
const CD=[["Oi",0,0],["Preço?",0,1],["Tem?",0,2],["Quanto?",1,0],["Tem no azul?",1,1],["Qual o prazo?",1,2],["Venda fechada",2,0],["Pedido pago",2,1],["Oi, tem?",0,3]];
const LANES=["Chegou","Em conversa","Fechado"];
const topin=document.getElementById('topin'), botin=document.getElementById('botin');
const LX=[24,329,634];
MB.forEach((m,i)=>{const e=document.createElement('div');e.className='mb';e.textContent=m[0];e.style.left=m[1]+'px';e.style.top=m[2]+'px';e.id='mb'+i;e.style.opacity=0;topin.appendChild(e)});
LANES.forEach((n,i)=>{const c=document.createElement('div');c.className='col';c.style.left=LX[i]+'px';botin.appendChild(c);const l=document.createElement('div');l.className='cl';l.style.left=LX[i]+'px';l.textContent=n;botin.appendChild(l)});
CD.forEach((c,i)=>{const e=document.createElement('div');e.className='cd';e.textContent=c[0];e.id='cd'+i;e.style.opacity=0;botin.appendChild(e)});
function setT(t){
  const hk=1-eo(seg(t,1.9,2.5)); const hook=document.getElementById('hook'); hook.style.opacity=hk; hook.style.display=hk<=0?'none':'block';
  const a0=eo(seg(t,0.1,0.6)); document.getElementById('hk0').style.opacity=a0;
  const a1=eo(seg(t,0.3,0.9)); const h1=document.getElementById('hk1'); h1.style.opacity=a1; h1.style.transform='translateY('+(1-a1)*40+'px)';
  const sp=eo(seg(t,2.3,2.9))*(1-eo(seg(t,10.6,11.2)));
  const split=document.getElementById('split'); split.style.opacity=sp;
  MB.forEach((m,i)=>{const t0=3.0+i*0.3; const k=eo(seg(t,t0,t0+0.3)); const e=document.getElementById('mb'+i); e.style.opacity=k; e.style.transform='rotate('+m[3]+'deg) scale('+(0.6+0.4*k)+')'});
  CD.forEach((c,i)=>{const t0=3.3+i*0.38; const k=ease(seg(t,t0,t0+0.6)); const e=document.getElementById('cd'+i);
    const fx=LX[c[1]]+8, fy=148+c[2]*86; const sx=330, sy=-90;
    e.style.left=(sx+(fx-sx)*k)+'px'; e.style.top=(sy+(fy-sy)*k)+'px'; e.style.opacity=clamp(k*3,0,1);});
  // after 7.2: dim top panel
  const dim=eo(seg(t,7.2,7.9)); document.getElementById('pt').style.opacity=1-0.62*dim;
  const ea=eo(seg(t,11.2,11.9)); const en=document.getElementById('end'); en.style.opacity=ea; en.style.transform='translateY('+(1-ea)*30+'px)';
  const pl=document.getElementById('pill'); pl.style.transform='scale('+(1+0.045*Math.sin(Math.max(0,t-12.3)*5.2))+')';
}
</script></body></html>'''.replace('__SRC__', SRC)

os.makedirs(FR, exist_ok=True)
for f in os.listdir(FR):
    os.remove(FR + f)
open('/home/claude/ig_week/reel_fri.html', 'w').write(HTML)
n = int(T * FPS)
with sync_playwright() as p:
    b = p.chromium.launch(args=['--allow-file-access-from-files'])
    pg = b.new_page(viewport={'width': W, 'height': H}, device_scale_factor=1)
    pg.goto('file:///home/claude/ig_week/reel_fri.html')
    pg.wait_for_timeout(800)
    for i in range(n):
        pg.evaluate('setT(%f)' % (i / FPS))
        pg.screenshot(path=FR + 'f%04d.jpg' % i, type='jpeg', quality=95)
    b.close()
cmd = ['ffmpeg', '-y', '-framerate', str(FPS), '-i', FR + 'f%04d.jpg', '-f', 'lavfi', '-t', str(T), '-i', 'anullsrc=r=48000:cl=stereo',
       '-vf', 'format=yuv420p', '-c:v', 'libx264', '-crf', '16', '-preset', 'medium', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
       '-r', str(FPS), '-c:a', 'aac', '-b:a', '128k', '-shortest', '-movflags', '+faststart', OUT]
subprocess.run(cmd, check=True, capture_output=True)
print('done', OUT)
