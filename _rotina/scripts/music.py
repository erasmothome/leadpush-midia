# Gera trilhas originais (sem direito autoral). Varie bpm, seed e progressao a cada semana.
import numpy as np, wave
sr = 44100
def _save(name, o):
    o = o / np.max(np.abs(o)) * 0.8
    fade = int(1.0 * sr); o[-fade:] *= np.linspace(1, 0, fade)
    with wave.open(name, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((o * 32767).astype(np.int16).tobytes())
def calm(name, T, bpm=104, seed=1, prog=None):
    rng = np.random.default_rng(seed); n = int(T * sr); out = np.zeros(n); beat = 60 / bpm
    def add(sig, at):
        i = int(at * sr)
        if i >= n: return
        j = min(n, i + len(sig)); out[i:j] += sig[:j - i]
    kt = np.arange(int(.35 * sr)) / sr; kick = np.sin(2*np.pi*(120*np.exp(-kt*18)+45)*kt)*np.exp(-kt*9)
    ht = np.arange(int(.06 * sr)) / sr; hat = np.diff(np.concatenate([[0], rng.standard_normal(len(ht))*np.exp(-ht*70)*0.25]))
    st = np.arange(int(.18 * sr)) / sr; sn = rng.standard_normal(len(st))*np.exp(-st*30)*0.35
    for b in range(int(T / beat) + 1):
        at = b * beat
        if b % 4 in (0, 2): add(kick * 0.9, at)
        if b % 4 in (1, 3): add(sn * 0.5, at)
        add(hat, at + beat / 2)
    prog = prog or [(55.0,[220,261.63,329.63]),(43.65,[174.61,220,261.63]),(65.41,[196,261.63,329.63]),(49.0,[196,246.94,293.66])]
    bar = beat * 4
    for k in range(int(T / bar) + 1):
        f0, ch = prog[k % len(prog)]; s0 = k * bar
        for q in range(8):
            at = s0 + q * beat / 2
            if at >= T: break
            bt = np.arange(int(beat / 2 * sr)) / sr
            add(np.sin(2*np.pi*f0*bt)*np.exp(-bt*6)*0.5*(1 if q % 2 == 0 else 0.55), at)
        pt = np.arange(int(bar * sr)) / sr
        pad = sum(np.sin(2*np.pi*f*pt) + 0.4*np.sin(2*np.pi*f*2*pt) for f in ch) / (len(ch) * 1.4)
        add(pad * np.minimum(pt/0.4, 1) * np.minimum((bar-pt)/0.5, 1) * 0.16, s0)
    _save(name, np.convolve(out, np.ones(3)/3, mode='same'))
def drive(name, T, bpm=124, seed=7, prog=None):
    rng = np.random.default_rng(seed); n = int(T * sr); out = np.zeros(n); beat = 60 / bpm
    def add(sig, at):
        i = int(at * sr)
        if i >= n: return
        j = min(n, i + len(sig)); out[i:j] += sig[:j - i]
    kt = np.arange(int(.3 * sr)) / sr; kick = np.sin(2*np.pi*(140*np.exp(-kt*22)+50)*kt)*np.exp(-kt*10)
    ht = np.arange(int(.05 * sr)) / sr; hat = np.diff(np.concatenate([[0], rng.standard_normal(len(ht))*np.exp(-ht*90)]))*0.3
    ct = np.arange(int(.14 * sr)) / sr; clap = rng.standard_normal(len(ct))*np.exp(-ct*38)*0.4
    for b in range(int(T / beat) + 1):
        at = b * beat; add(kick, at); add(hat, at + beat / 2)
        if b % 2 == 1: add(clap, at)
    prog = prog or [[146.83,174.61,220],[116.54,146.83,174.61],[174.61,220,261.63],[130.81,164.81,196]]
    bar = beat * 4
    for k in range(int(T / bar) + 1):
        ch = prog[k % len(prog)]
        for q in range(16):
            at = k * bar + q * beat / 4
            if at >= T: break
            f = ch[[0, 1, 2, 1][q % 4]] * (2 if q % 8 >= 4 else 1)
            pt = np.arange(int(.22 * sr)) / sr
            add((np.sin(2*np.pi*f*pt)+0.5*np.sin(2*np.pi*f*2*pt)+0.25*np.sin(2*np.pi*f*3*pt))*np.exp(-pt*11)*0.22, at)
        bt = np.arange(int(beat * sr)) / sr
        for q in range(4): add(np.sin(2*np.pi*ch[0]/2*bt)*np.exp(-bt*3.5)*0.5, k*bar + q*beat)
    _save(name, out)
# mux: ffmpeg -i video.mp4 -i trilha.wav -filter_complex "[1:a]volume=0.55,loudnorm=I=-20:TP=-2:LRA=7,aformat=sample_rates=48000:channel_layouts=stereo[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 128k -shortest -movflags +faststart saida.mp4
