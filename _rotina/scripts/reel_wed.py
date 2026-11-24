import os, subprocess, shutil
from playwright.sync_api import sync_playwright

W, H, FPS, T = 1080, 1920, 30, 25.0
SRC = '/home/claude/ig_week/src/'
SHOT = '/home/claude/lp/site/assets/shot-fluxos.webp'
FR = '/home/claude/ig_week/frames_wed/'
OUT = '/home/claude/ig_week/Reel_quarta_Funil_da_Semana_1.mp4'

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
.lab{font-family:Mont;font-weight:600;font-size:30px;letter-spacing:.2em;text-transform:uppercase;color:#DCBB63}
.bub{font-family:Int;font-weight:500;font-size:44px;line-height:1.3;padding:30px 42px;border-radius:38px;background:#EDF2FA;color:#0F1D35;border-bottom-left-radius:10px}
.dot{display:inline-block;width:20px;height:20px;border-radius:50%;background:#94A6C4;margin:0 6px}
#panel{left:72px;top:600px;width:936px;height:760px;border-radius:40px;overflow:hidden;border:2px solid rgba(148,166,196,.35);background:#0A1526}
#img{position:absolute;left:0;top:0;transform-origin:0 0;filter:brightness(1.3) contrast(1.08)}
#cap{left:90px;top:1410px;width:900px;font-family:Int;font-weight:500;font-size:44px;line-height:1.32;color:#EDF2FA}
.ring{position:absolute;border:5px solid #DCBB63;border-radius:18px;box-shadow:0 0 0 0 rgba(220,187,99,0)}
</style></head><body><div id="c">
<div id="hook">
  <div class="abs h" id="h1" style="left:90px;top:540px;width:900px;font-size:104px;line-height:1.05">O cliente respondeu.</div>
  <div class="abs h" id="h2" style="left:90px;top:770px;width:900px;font-size:150px;line-height:1.0;color:#DCBB63">E agora?</div>
  <div class="abs bub" id="b1" style="left:90px;top:1090px;transform-origin:0 100%">Quero saber mais!</div>
  <div class="abs bub" id="b2" style="left:90px;top:1250px;padding:26px 36px;transform-origin:0 100%"><span class="dot" id="d1"></span><span class="dot" id="d2"></span><span class="dot" id="d3"></span></div>
</div>
<div id="step" style="opacity:0">
  <div class="abs lab" id="stlab" style="left:90px;top:300px"></div>
  <div class="abs h" id="sttit" style="left:90px;top:360px;width:900px;font-size:76px;line-height:1.04"></div>
</div>
<div class="abs" id="cap" style="opacity:0"></div>
<div class="abs" id="panel" style="opacity:0"><img id="img" src="file://__SHOT__"><img id="img2" src="file:///home/claude/ig_week/kanban_anon.png" style="position:absolute;left:0;top:0;transform-origin:0 0;opacity:0"><div class="ring" id="ring" style="opacity:0"></div></div>
<div id="end" style="opacity:0">
  <div class="abs lab" style="left:90px;top:520px">Funil da Semana #1</div>
  <div class="abs h" style="left:90px;top:590px;width:900px;font-size:112px;line-height:1.04">Toda semana, um <span style="color:#DCBB63">funil novo.</span></div>
  <div class="abs gold" id="pill" style="left:90px;top:1040px;padding:40px 76px;border-radius:999px;font-family:Mont;font-weight:800;font-size:56px;color:#0A1526;transform-origin:0 50%">Siga a LeadPush</div>
  <img class="abs" src="file://__SRC__comslogan_escuro.png" style="left:90px;top:1330px;width:620px">
</div>
</div>
<script>
const IW=1280, IH=608, PW=936, PH=760;
const clamp=(x,a,b)=>Math.max(a,Math.min(b,x));
const seg=(t,a,b)=>clamp((t-a)/(b-a),0,1);
const ease=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const eo=x=>1-Math.pow(1-x,3);
// scenes: region x0,y0,width
const R1={x:330,y:100,w:500}, R2={x:500,y:226,w:470}, R3={x:0,y:60,w:425};
function lerp(a,b,k){return a+(b-a)*k}
function region(t){
  if(t<9) return R1;
  if(t<9.8){const k=ease(seg(t,9,9.8));return {x:lerp(R1.x,R2.x,k),y:lerp(R1.y,R2.y,k),w:lerp(R1.w,R2.w,k)}}
  if(t<15) return R2;
  return R2;
}
function setText(id,s){const e=document.getElementById(id); if(e.dataset.s!==s){e.textContent=s;e.dataset.s=s}}
function setT(t){
  // hook
  const hk=1-eo(seg(t,2.9,3.4));
  const hook=document.getElementById('hook'); hook.style.opacity=hk; hook.style.display=hk<=0?'none':'block';
  const a1=eo(seg(t,0.15,0.7)); const h1=document.getElementById('h1'); h1.style.opacity=a1; h1.style.transform='translateY('+(1-a1)*40+'px)';
  const a2=eo(seg(t,1.2,1.75)); const h2=document.getElementById('h2'); h2.style.opacity=a2; h2.style.transform='translateY('+(1-a2)*40+'px)';
  const pb=eo(seg(t,0.5,0.95)); const b1=document.getElementById('b1'); b1.style.opacity=pb; b1.style.transform='scale('+(0.7+0.3*pb)+')';
  const pc=eo(seg(t,1.5,1.9)); const b2=document.getElementById('b2'); b2.style.opacity=pc; b2.style.transform='scale('+(0.7+0.3*pc)+')';
  for(let i=1;i<=3;i++){const d=document.getElementById('d'+i); const ph=((t*2.2)-(i*0.25))%1; d.style.opacity=0.35+0.65*Math.abs(Math.sin(Math.PI*ph))}
  // panel
  const pa=eo(seg(t,3.0,3.7))*(1-eo(seg(t,19.6,20.2)));
  const panel=document.getElementById('panel'); panel.style.opacity=pa; panel.style.transform='translateY('+(1-eo(seg(t,3.0,3.7)))*80+'px)';
  const r=region(t), s=PW/r.w;
  const f2=eo(seg(t,15.0,15.6));
  const i2=document.getElementById('img2'); i2.style.opacity=f2; const s2=PW/560, px=lerp(104,880,ease(seg(t,16.0,19.4)));
  i2.style.transform='translate('+(-px*s2)+'px,'+(-140*s2)+'px) scale('+s2+')';
  document.getElementById('img').style.opacity=1-f2;
  const img=document.getElementById('img'); img.style.transform='translate('+(-r.x*s)+'px,'+(-r.y*s)+'px) scale('+s+')';
  // step titles
  let lab='',tit='';
  if(t>=3.3&&t<9){lab='Passo 1';tit='A resposta chega'}
  else if(t>=9.2&&t<15){lab='Passo 2';tit='O funil conduz a conversa'}
  else if(t>=15.2&&t<19.8){lab='Passo 3';tit='O contato entra no Kanban'}
  setText('stlab',lab); setText('sttit',tit);
  let cp=''; if(lab==='Passo 1')cp='Quando o cliente responde, o fluxo começa sozinho.'; else if(lab==='Passo 2')cp='O funil envia a mensagem certa para cada contato.'; else if(lab==='Passo 3')cp='Cada contato vira um card e avança de etapa em etapa.'; setText('cap',cp);
  const starts=[3.3,9.2,15.2], ends=[9,15,19.8];
  let so=0;
  for(let i=0;i<3;i++){ if(t>=starts[i]&&t<ends[i]){ so=eo(seg(t,starts[i],starts[i]+0.5))*(1-eo(seg(t,ends[i]-0.4,ends[i]))); } }
  const st=document.getElementById('step'); st.style.opacity=so; document.getElementById('cap').style.opacity=so;
  // ring (in image coords per scene)
  let box=null;
  if(t>=4.2&&t<9) box={x:508,y:150,w:182,h:50};            // Inicio / mensagem recebida
  else if(t>=10.2&&t<15) box={x:602,y:440,w:160,h:140};    // Funil node
  
  const ring=document.getElementById('ring');
  if(box){const pad=10; ring.style.left=((box.x-r.x)*s-pad)+'px'; ring.style.top=((box.y-r.y)*s-pad)+'px'; ring.style.width=(box.w*s+2*pad)+'px'; ring.style.height=(box.h*s+2*pad)+'px';
    const k0=(t<9?4.2:10.2); ring.style.opacity=eo(seg(t,k0,k0+0.4))*(0.65+0.35*Math.abs(Math.sin(t*4)));}
  else ring.style.opacity=0;
  // end
  const ea=eo(seg(t,20.2,20.9)); const en=document.getElementById('end'); en.style.opacity=ea; en.style.transform='translateY('+(1-ea)*30+'px)';
  const pl=document.getElementById('pill'); const pul=1+0.045*Math.sin(Math.max(0,t-21.4)*5.2); pl.style.transform='scale('+pul+')';
}
</script></body></html>'''.replace('__SHOT__', SHOT).replace('__SRC__', SRC)

os.makedirs(FR, exist_ok=True)
for f in os.listdir(FR):
    os.remove(FR + f)
open('/home/claude/ig_week/reel_wed.html', 'w').write(HTML)

n = int(T * FPS)
with sync_playwright() as p:
    b = p.chromium.launch(args=['--allow-file-access-from-files'])
    pg = b.new_page(viewport={'width': W, 'height': H}, device_scale_factor=1)
    pg.goto('file:///home/claude/ig_week/reel_wed.html')
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
