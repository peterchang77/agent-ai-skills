# /// script
# requires-python = ">=3.10"
# dependencies = ["pydicom==2.4.4", "pylibjpeg==2.0.1", "pylibjpeg-libjpeg==2.3.0", "numpy", "pillow==10.4.0"]
# ///
"""Reference viewer tool: a self-contained HTML contact sheet for DICOM review.

    uv run make_viewer.py IMAGES_DIR OUT.html [--flags flags.csv]

flags.csv (optional) has columns: file,flag   (several rows per file allowed). The page has a filter by flag, a larger view on click,
a header panel, and confirm / reject / unsure buttons. Decisions are kept in the browser and exported with a button as review.csv
(file,decision,flags). Static and offline: no network, no external scripts. Labels and model scores are never embedded.
"""
import argparse, base64, csv, io, json, warnings
from collections import defaultdict
from pathlib import Path
import numpy as np, pydicom
from PIL import Image
warnings.filterwarnings("ignore")

ap = argparse.ArgumentParser(); ap.add_argument("images"); ap.add_argument("out"); ap.add_argument("--flags"); ap.add_argument("--size", type=int, default=512)
a = ap.parse_args()
flags = defaultdict(list)
if a.flags:
    for r in csv.DictReader(open(a.flags)): flags[r["file"]].append(r["flag"])
SHOW = ["PatientID", "PatientSex", "PatientAge", "Modality", "ViewPosition", "PhotometricInterpretation", "Rows", "Columns", "PixelSpacing", "StudyDate", "SOPInstanceUID"]
items = []
for p in sorted(Path(a.images).glob("*.dcm")):
    rec = dict(file=p.name, flags=flags.get(p.name, []), hdr={}, img=None)
    try:
        ds = pydicom.dcmread(p); arr = ds.pixel_array.astype(np.uint8)
        rec["hdr"] = {k: str(ds.get(k, "(missing)")) for k in SHOW}
        if ds.PhotometricInterpretation == "MONOCHROME1": arr = 255 - arr    # show MONOCHROME1 the way a viewer would
        im = Image.fromarray(arr).convert("L"); im.thumbnail((a.size, a.size))
        buf = io.BytesIO(); im.save(buf, "JPEG", quality=70)
        rec["img"] = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    except Exception as e:
        rec["hdr"] = {"error": f"{type(e).__name__}: {e}"[:200]}
    items.append(rec)
allflags = sorted({f for r in items for f in r["flags"]})
page = """<!doctype html><meta charset=utf-8><title>DICOM review sheet</title>
<style>body{font:14px system-ui;margin:12px;background:#111;color:#eee}.g{display:grid;grid-template-columns:repeat(auto-fill,150px);gap:8px}
.c{background:#222;padding:4px;border:3px solid #222;cursor:pointer}.c img{width:100%;display:block}.c small{display:block;word-break:break-all}
.confirm{border-color:#d33}.reject{border-color:#3a3}.unsure{border-color:#da3}.f{color:#fc6}#m{position:fixed;inset:0;background:#000d;display:none;padding:16px;overflow:auto}
#m img{max-height:80vh}button{margin:2px;padding:6px 10px}pre{font-size:12px}</style>
<h3>DICOM review sheet <small id=n></small></h3>
<label>Filter: <select id=flt><option value="">all</option></select></label>
<button onclick=exp()>Export review.csv</button> <small>Red = confirmed problem, green = rejected (looks fine), amber = unsure. Decisions stay in this browser until exported.</small>
<div class=g id=g></div><div id=m onclick="if(event.target===this)this.style.display='none'"></div>
<script>
const D=__DATA__, FL=__FLAGS__; const dec=JSON.parse(localStorage.getItem('dec:'+location.pathname)||'{}');
const flt=document.getElementById('flt'); FL.forEach(f=>{const o=document.createElement('option');o.value=o.text=f;flt.add(o)});
function save(){localStorage.setItem('dec:'+location.pathname,JSON.stringify(dec))}
function draw(){const g=document.getElementById('g');g.innerHTML='';let k=0;D.forEach((r,i)=>{if(flt.value&&!r.flags.includes(flt.value))return;k++;
 const c=document.createElement('div');c.className='c '+(dec[r.file]||'');c.onclick=()=>show(i);
 c.innerHTML=(r.img?'<img src="'+r.img+'">':'<div style="height:150px">unreadable</div>')+'<small>'+r.file+'</small><small class=f>'+r.flags.join(', ')+'</small>';g.appendChild(c)});
 document.getElementById('n').textContent='('+k+' shown of '+D.length+')'}
function show(i){const r=D[i],m=document.getElementById('m');m.style.display='block';
 m.innerHTML='<div>'+(r.img?'<img src="'+r.img+'">':'')+'</div><h4>'+r.file+'</h4><pre>'+JSON.stringify(r.hdr,null,1)+'</pre><p class=f>'+r.flags.join(', ')+'</p>'+
 ['confirm','reject','unsure'].map(d=>'<button onclick="dec[\\''+r.file+'\\']=\\''+d+'\\';save();draw();show('+i+')">'+d+'</button>').join('')+
 '<button onclick="document.getElementById(\\'m\\').style.display=\\'none\\'">close</button>'}
function exp(){const t='file,decision,flags\\n'+Object.entries(dec).map(e=>e[0]+','+e[1]+',"'+(D.find(r=>r.file===e[0]).flags.join(';'))+'"').join('\\n')+'\\n';const a=document.createElement('a');
 a.href=URL.createObjectURL(new Blob([t],{type:'text/csv'}));a.download='review.csv';a.click()}
flt.onchange=draw;draw();
</script>"""
Path(a.out).write_text(page.replace("__DATA__", json.dumps(items).replace("</", "<\\/")).replace("__FLAGS__", json.dumps(allflags)))
print(f"wrote {a.out}: {len(items)} images, {Path(a.out).stat().st_size/1e6:.1f} MB")
