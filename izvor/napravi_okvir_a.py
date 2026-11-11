"""Generiše sintetički CSS okvir i JavaScript biblioteku za varijantu A.
To nisu stvarne biblioteke: služe da simuliraju tipičan veliki okvir od kojeg
stranica koristi gotovo ništa (oko 140 KB CSS-a i 650 KB JavaScripta, uz
~180 ms sinhronog izvršavanja pri učitavanju). Pokretanje: python napravi_okvir_a.py"""
import random, os
random.seed(3)
os.makedirs("css", exist_ok=True); os.makedirs("js", exist_ok=True)
rules = []
props = ['margin','padding','color','background','border','font-size','line-height','width','height','display','opacity','transform']
for i in range(2600):
    p = random.choice(props)
    rules.append(f".u-{p}-{i}{{{p}:{random.randint(0,99)}px;transition:all .{random.randint(1,9)}s ease}}")
for bp in (576,768,992,1200,1400):
    rules.append(f"@media (min-width:{bp}px){{"+"".join(f".col-{bp}-{k}{{flex:0 0 {k/12*100:.4f}%;max-width:{k/12*100:.4f}%}}" for k in range(1,13))+"}")
open('css/framework.css','w').write("\n".join(rules))
lines = ["(function(){var registry={};"]
for i in range(5200):
    lines.append(f"registry['modul_{i}']=function(a,b){{var x=a*{random.randint(1,999)}+b;for(var k=0;k<{random.randint(2,9)};k++){{x=(x*31+k)%{random.randint(1000,99999)};}}return 'rezultat_'+x+'_{random.random():.8f}';}};")
lines.append("var t=performance.now();var acc=0;while(performance.now()-t<180){acc+=Math.sqrt(Math.random()*1e6);}window.__lib={registry:registry,acc:acc};})();")
open('js/biblioteka.js','w').write("\n".join(lines))
print("css/framework.css i js/biblioteka.js napravljeni")
