"""Phone-photo style JPG twins of the warranty PDFs (page 1 of each; every one is a single page).
   python make-photo-twins.py      -> warranties-from-receipts-photo/ and warranties-photo/ (same file names, .jpg)
Deterministic: the look of each photo is seeded from its file name, so re-running gives the same images."""
import glob, os, random, zlib
import pypdfium2 as pdfium
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw

HERE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
JOBS = [('warranties-from-receipts', 'warranties-from-receipts-photo'), ('warranties', 'warranties-photo')]

def photo(page_img, rnd):
    w, h = page_img.size
    pad = int(w * 0.07)
    desk = tuple(rnd.randint(60, 110) for _ in range(3))
    canvas = Image.new('RGB', (w + 2 * pad, h + 2 * pad), desk)
    shadow = Image.new('RGB', page_img.size, (20, 20, 20)).filter(ImageFilter.GaussianBlur(14))
    canvas.paste(shadow, (pad + 8, pad + 10))
    canvas.paste(page_img, (pad, pad))
    # light falling across the paper: a soft gradient, brighter one side
    grad = Image.linear_gradient('L').resize(canvas.size).rotate(rnd.choice([0, 90, 180, 270]) + rnd.randint(-25, 25), fillcolor=128).filter(ImageFilter.GaussianBlur(60))
    shade = Image.new('RGB', canvas.size, (0, 0, 0))
    canvas = Image.composite(canvas, Image.blend(canvas, shade, 0.30), grad.point(lambda v: 150 + v // 3))
    canvas = canvas.rotate(rnd.uniform(-3.2, 3.2), resample=Image.BICUBIC, expand=True, fillcolor=desk)
    # a small perspective lean, as if held a little off-square
    cw, ch = canvas.size
    k = rnd.uniform(-0.035, 0.035)
    canvas = canvas.transform(canvas.size, Image.PERSPECTIVE, (1, k, 0, 0, 1, 0, 0, 0.00002 * rnd.choice([-1, 1]) * rnd.random()), Image.BICUBIC, fillcolor=desk)
    canvas = canvas.filter(ImageFilter.GaussianBlur(rnd.uniform(0.5, 1.1)))
    canvas = ImageEnhance.Contrast(canvas).enhance(rnd.uniform(0.9, 1.05))
    canvas = ImageEnhance.Brightness(canvas).enhance(rnd.uniform(0.92, 1.04))
    longest = 2000
    s = longest / max(canvas.size)
    return canvas.resize((round(canvas.width * s), round(canvas.height * s)), Image.LANCZOS)

made = 0
for src, dst in JOBS:
    os.makedirs(os.path.join(HERE, dst), exist_ok=True)
    for f in sorted(glob.glob(os.path.join(HERE, src, '*.pdf'))):
        name = os.path.basename(f)
        pdf = pdfium.PdfDocument(f)
        img = pdf[0].render(scale=2.2).to_pil().convert('RGB')
        out = photo(img, random.Random(zlib.crc32(name.encode())))
        out.save(os.path.join(HERE, dst, name[:-4] + '.jpg'), 'JPEG', quality=82)
        made += 1
print('made', made)
