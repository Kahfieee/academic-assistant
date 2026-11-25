import os
import re
import io
import base64
import subprocess
import pypdf
from reportlab.pdfgen import canvas

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(TOOLS_DIR)
TEMPLATES_DIR = os.path.join(ROOT_DIR, 'templates')
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets')

EDGE_PATH = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
OUTPUT_PDF = os.path.join(TEMPLATES_DIR, 'formal_thesis_template.pdf')
LOGO_PATH = os.path.join(ASSETS_DIR, 'university_logo_placeholder.png')

os.makedirs(TEMPLATES_DIR, exist_ok=True)

with open(LOGO_PATH, 'rb') as f:
    logo_b64 = base64.b64encode(f.read()).decode('utf-8')
logo_uri = f'data:image/png;base64,{logo_b64}'

HTML_HEAD = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Template Naskah Karya Ilmiah / Skripsi</title>
<style>
  @page {
    size: A4;
    margin: 4cm 3cm 3cm 4cm;
  }
  body {
    font-family: "Times New Roman", Times, serif;
    font-size: 12pt;
    line-height: 1.5;
    color: #000;
    margin: 0;
    padding: 0;
  }
  .page-break {
    page-break-before: always;
  }
  h1.chapter {
    font-size: 14pt;
    font-weight: bold;
    text-align: center;
    text-transform: uppercase;
    margin: 0 0 1.2rem 0;
    line-height: 1.4;
  }
  h2 {
    font-size: 12pt;
    font-weight: bold;
    margin: 1.1rem 0 0.4rem 0;
  }
  h3 {
    font-size: 12pt;
    font-weight: bold;
    margin: 0.9rem 0 0.3rem 0;
  }
  p {
    text-align: justify;
    text-indent: 1cm;
    margin: 0 0 0.6rem 0;
  }
  p.no-indent {
    text-indent: 0;
  }
  p.caption {
    text-indent: 0;
    text-align: center;
    font-size: 10.5pt;
    font-weight: bold;
    margin: 0.8rem 0 0.4rem 0;
  }
  .center {
    text-align: center;
  }
  ul, ol {
    margin: 0.3rem 0 0.8rem 1.2cm;
    padding-left: 0.5cm;
  }
  li {
    text-align: justify;
    margin-bottom: 0.25rem;
  }
  table.academic {
    width: 100%;
    border-collapse: collapse;
    font-size: 10.5pt;
    line-height: 1.35;
    margin: 0.4rem 0 1rem 0;
  }
  table.academic th, table.academic td {
    border-top: 1px solid #000;
    border-bottom: 1px solid #000;
    padding: 6px 8px;
    text-align: left;
    vertical-align: top;
  }
  table.academic thead th {
    background-color: #f1f5f9;
    font-weight: bold;
    text-align: center;
    border-top: 1.5px solid #000;
    border-bottom: 1.5px solid #000;
  }
  .toc-item {
    display: flex;
    align-items: baseline;
    margin-bottom: 0.25rem;
  }
  .toc-dots {
    flex: 1;
    border-bottom: 1px dotted #444;
    margin: 0 6px;
  }
  .guide-box {
    background-color: #f8fafc;
    border-left: 3px solid #475569;
    padding: 0.5rem 0.8rem;
    margin: 0.4rem 0 0.8rem 0;
    font-size: 11pt;
    text-align: justify;
  }
  pre.code-block {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    padding: 0.7rem;
    font-family: Consolas, monospace;
    font-size: 9pt;
    line-height: 1.35;
    white-space: pre-wrap;
    text-indent: 0;
  }
</style>
</head>
<body>
"""

FRONT_BEFORE_TOC = f"""<!-- COVER -->
<div class="center" style="min-height: 21.5cm; display: flex; flex-direction: column; justify-content: space-between;">
  <div>
    <p class="no-indent center" style="font-size: 14pt; font-weight: bold; text-transform: uppercase; margin-bottom: 1.2rem;">
      [JUDUL PENELITIAN / KARYA ILMIAH DISINI]
    </p>
    <p class="no-indent center" style="font-size: 13pt; font-weight: bold; margin-bottom: 0.6rem;">
      SKRIPSI / TUGAS AKHIR
    </p>
    <p class="no-indent center" style="font-size: 11pt;">
      Diajukan untuk Memenuhi Sebagian Persyaratan Akademik<br>
      Meraih Gelar [Nama Gelar Akademik Disini] pada Program Studi [Nama Program Studi Disini]
    </p>
  </div>

  <div style="margin: 1cm auto; text-align: center;">
    <img src="{logo_uri}" alt="Logo Institusi" style="width: 140px; height: auto; display: block; margin: 0 auto;">
  </div>

  <div>
    <p class="no-indent center" style="font-size: 12pt; margin-bottom: 0.4rem;">Disusun Oleh:</p>
    <p class="no-indent center" style="font-size: 12pt; font-weight: bold; margin-bottom: 0.2rem;">[Nama Penulis Disini]</p>
    <p class="no-indent center" style="font-size: 12pt; font-weight: bold; margin-bottom: 2.2rem;">NIM / ID: [Nomor Induk Disini]</p>

    <p class="no-indent center" style="font-size: 12pt; font-weight: bold; text-transform: uppercase; margin-bottom: 0.15rem;">PROGRAM STUDI [NAMA PROGRAM STUDI DISINI]</p>
    <p class="no-indent center" style="font-size: 12pt; font-weight: bold; text-transform: uppercase; margin-bottom: 0.15rem;">FAKULTAS [NAMA FAKULTAS DISINI]</p>
    <p class="no-indent center" style="font-size: 12pt; font-weight: bold; text-transform: uppercase; margin-bottom: 0.15rem;">[NAMA UNIVERSITAS / INSTITUSI DISINI]</p>
    <p class="no-indent center" style="font-size: 12pt; font-weight: bold;">[Tahun Disini]</p>
  </div>
</div>

<!-- LEMBAR PENGESAHAN -->
<div class="page-break">
  <h1 class="chapter" style="font-size: 13pt; margin-bottom: 0.8rem;">LEMBAR PENGESAHAN</h1>
  <table style="width: 100%; font-size: 10.5pt; line-height: 1.4; margin-bottom: 0.8rem; border-collapse: collapse;">
    <tr><td style="width: 28%; font-weight: bold; vertical-align: top; padding: 3px 0;">Judul Karya Ilmiah</td><td style="width: 3%; vertical-align: top;">:</td><td style="font-weight: bold; text-align: justify;">[JUDUL PENELITIAN / KARYA ILMIAH DISINI]</td></tr>
    <tr><td style="font-weight: bold; padding: 3px 0;">Nama Mahasiswa</td><td>:</td><td>[Nama Penulis Disini]</td></tr>
    <tr><td style="font-weight: bold; padding: 3px 0;">Nomor Induk (NIM)</td><td>:</td><td>[Nomor Induk Disini]</td></tr>
    <tr><td style="font-weight: bold; padding: 3px 0;">Program Studi</td><td>:</td><td>[Nama Program Studi Disini]</td></tr>
    <tr><td style="font-weight: bold; padding: 3px 0;">Bidang Konsentrasi</td><td>:</td><td>[Bidang Kajian / Peminatan Disini]</td></tr>
  </table>

  <p class="no-indent" style="font-size: 10pt; text-align: justify; margin-bottom: 0.8rem;">
    Karya ilmiah ini telah disetujui, dipertahankan di hadapan Dewan Penguji pada Program Studi [Nama Program Studi Disini], [Nama Universitas / Institusi Disini] pada tanggal [Tanggal Sidang Disini], dan dinyatakan <strong>LULUS</strong>.
  </p>

  <p class="no-indent" style="font-size: 10pt; font-weight: bold; margin-bottom: 0.3rem;">Komisi Pembimbing:</p>
  <table style="width: 100%; font-size: 9.5pt; text-align: center; margin-bottom: 0.8rem; border-collapse: collapse;">
    <tr>
      <td style="width: 50%; vertical-align: top;">Pembimbing Utama,<br><br><br><br><u><strong>[Nama Pembimbing Utama Disini]</strong></u><br>NIDN / NIP: [Nomor Identitas Disini]</td>
      <td style="width: 50%; vertical-align: top;">Pembimbing Pendamping,<br><br><br><br><u><strong>[Nama Pembimbing Pendamping Disini]</strong></u><br>NIDN / NIP: [Nomor Identitas Disini]</td>
    </tr>
  </table>

  <p class="no-indent" style="font-size: 10pt; font-weight: bold; margin-bottom: 0.3rem;">Dewan Penguji:</p>
  <table style="width: 100%; font-size: 9.5pt; text-align: center; margin-bottom: 0.8rem; border-collapse: collapse;">
    <tr>
      <td style="width: 50%; vertical-align: top;">Ketua Penguji,<br><br><br><br><u><strong>[Nama Ketua Penguji Disini]</strong></u><br>NIDN / NIP: [Nomor Identitas Disini]</td>
      <td style="width: 50%; vertical-align: top;">Anggota Penguji,<br><br><br><br><u><strong>[Nama Anggota Penguji Disini]</strong></u><br>NIDN / NIP: [Nomor Identitas Disini]</td>
    </tr>
  </table>

  <div style="text-align: center; margin-top: 0.6rem; font-size: 9.5pt;">
    <p class="no-indent center" style="margin: 0;">Mengetahui,</p>
    <p class="no-indent center" style="margin: 0; font-weight: bold;">Ketua Program Studi [Nama Program Studi Disini]</p>
    <br><br><br>
    <p class="no-indent center" style="margin: 0;"><u><strong>[Nama Ketua Program Studi Disini]</strong></u></p>
    <p class="no-indent center" style="margin: 0;">NIDN / NIP: [Nomor Identitas Disini]</p>
  </div>
</div>

<!-- PERNYATAAN KEASLIAN -->
<div class="page-break">
  <h1 class="chapter">PERNYATAAN KEASLIAN KARYA ILMIAH</h1>
  <p class="no-indent">Saya yang bertanda tangan di bawah ini:</p>
  <table style="width: 100%; font-size: 11.5pt; margin-bottom: 1rem; border-collapse: collapse;">
    <tr><td style="width: 28%; padding: 3px 0;">Nama</td><td style="width: 3%;">:</td><td>[Nama Penulis Disini]</td></tr>
    <tr><td style="padding: 3px 0;">Nomor Induk (NIM)</td><td>:</td><td>[Nomor Induk Disini]</td></tr>
    <tr><td style="padding: 3px 0;">Program Studi</td><td>:</td><td>[Nama Program Studi Disini]</td></tr>
    <tr><td style="padding: 3px 0;">Perguruan Tinggi</td><td>:</td><td>[Nama Universitas / Institusi Disini]</td></tr>
  </table>
  <p>
    Menyatakan dengan sesungguhnya bahwa karya ilmiah yang berjudul <strong>"[JUDUL PENELITIAN / KARYA ILMIAH DISINI]"</strong> adalah benar-benar merupakan karya ilmiah asli saya sendiri di bawah arahan komisi pembimbing, bukan hasil jiplakan, saduran, atau fabrikasi data dari karya orang lain, baik sebagian maupun seluruhnya. Seluruh rujukan, kepustakaan, dan kutipan telah dicantumkan secara sah sesuai kaidah integritas akademik dan etika sitasi ilmiah yang berlaku.
  </p>
  <p>
    Apabila di kemudian hari terbukti bahwa karya ilmiah ini mengandung unsur plagiarisme, manipulasi data, atau pelanggaran etika akademik lainnya, saya bersedia menerima sanksi akademik sesuai peraturan perundang-undangan yang berlaku, termasuk pembatalan kelulusan dan pencabutan gelar akademik yang diperoleh.
  </p>
  <div style="margin-top: 1.5cm; float: right; text-align: center; width: 230px;">
    [Kota Disini], [Tanggal Disini]<br>
    Yang menyatakan,<br><br>
    <div style="border: 1px dashed #888; padding: 10px; font-size: 9pt; color: #555; margin: 8px auto; width: 130px;">
      Materai Resmi
    </div>
    <br>
    <u><strong>[Nama Penulis Disini]</strong></u><br>
    NIM / ID: [Nomor Induk Disini]
  </div>
  <div style="clear: both;"></div>
</div>

<!-- KATA PENGANTAR -->
<div class="page-break" style="font-size: 11pt; line-height: 1.45;">
  <h1 class="chapter" style="margin-bottom: 0.9rem;">KATA PENGANTAR</h1>
  <p>
    Puji syukur kehadirat Tuhan Yang Maha Esa atas segala rahmat dan karunia-Nya sehingga penulis dapat menyelesaikan naskah karya ilmiah yang berjudul <strong>"[Judul Penelitian / Karya Ilmiah Disini]"</strong> dengan baik. Naskah ini disusun sebagai salah satu syarat akademik untuk memperoleh gelar [Nama Gelar Akademik Disini] pada Program Studi [Nama Program Studi Disini], [Nama Universitas / Institusi Disini].
  </p>
  <p>
    Dalam proses penelitian hingga penyelesaian naskah ini, penulis telah memperoleh bimbingan, masukan ilmiah, serta dukungan dari berbagai pihak. Penulis menyampaikan terima kasih dan penghargaan yang sebesar-besarnya kepada:
  </p>
  <ol style="margin-left: 0.8cm; font-size: 10.5pt; line-height: 1.4;">
    <li><strong>[Nama Rektor / Ketua Institusi Disini]</strong>, selaku Pimpinan [Nama Universitas / Institusi Disini].</li>
    <li><strong>[Nama Dekan / Ketua Program Studi Disini]</strong>, selaku Ketua Program Studi [Nama Program Studi Disini].</li>
    <li><strong>[Nama Pembimbing Utama Disini]</strong>, selaku Dosen Pembimbing Utama atas arahan metodologis, pendampingan analitis, dan ketelitian dalam membimbing riset ini.</li>
    <li><strong>[Nama Pembimbing Pendamping Disini]</strong>, selaku Dosen Pembimbing Pendamping atas bimbingan teknis, evaluasi rancangan, dan penyempurnaan penulisan.</li>
    <li>Seluruh Dosen dan Staf Akademik pada [Nama Universitas / Institusi Disini] atas ilmu pengetahuan yang diberikan selama masa studi.</li>
    <li>Orang tua, keluarga, dan rekan-rekan seperjuangan atas dukungan moral, doa, serta diskusi konstruktif selama proses penelitian.</li>
  </ol>
  <p>
    Penulis menyadari bahwa karya ilmiah ini masih terbuka terhadap saran dan kritik konstruktif demi penyempurnaan di masa mendatang. Semoga hasil penelitian ini memberikan kontribusi bermanfaat bagi perkembangan keilmuan dan praktik industri.
  </p>
  <div style="margin-top: 0.6rem; float: right; text-align: center; width: 230px;">
    [Kota Disini], [Tanggal Disini]<br><br><br>
    <u><strong>[Nama Penulis Disini]</strong></u><br>
    NIM / ID: [Nomor Induk Disini]
  </div>
  <div style="clear: both;"></div>
</div>

<!-- ABSTRAK INDONESIA -->
<div class="page-break">
  <h1 class="chapter">ABSTRAK</h1>
  <p class="no-indent center" style="font-weight: bold; margin-bottom: 1rem;">
    [NAMA PENULIS DISINI]. [Nomor Induk Disini]. [Judul Penelitian / Karya Ilmiah Disini].
  </p>
  <p>
    <strong>[Paragraf 1 - Latar Belakang &amp; Masalah (~15–20%):]</strong> Jelaskan konteks permasalahan nyata yang mendasari penelitian, keterbatasan solusi atau studi sebelumnya (<em>research gap</em>), serta urgensi pendekatan yang diusulkan.
  </p>
  <p>
    <strong>[Paragraf 2 - Metodologi &amp; Desain Eksperimen (~20–30%):]</strong> Uraikan karakteristik dataset atau objek penelitian, tahapan pra-pemrosesan/rekayasa sistem, metode utama yang dirancang, serta skema validasi atau protokol pengujian yang digunakan secara terukur.
  </p>
  <p>
    <strong>[Paragraf 3 - Hasil Kuantitatif &amp; Simpulan (~50%):]</strong> Sajikan temuan kuantitatif utama (misalnya metrik kinerja, efisiensi, hasil uji hipotesis/statistik, perbandingan terhadap metode pembanding), makna dari temuan tersebut, serta simpulan ringkas kontribusi penelitian.
  </p>
  <p class="no-indent" style="margin-top: 1rem;">
    <strong>Kata Kunci:</strong> [Kata Kunci 1], [Kata Kunci 2], [Kata Kunci 3], [Kata Kunci 4], [Kata Kunci 5].
  </p>
</div>

<!-- ABSTRACT ENGLISH -->
<div class="page-break">
  <h1 class="chapter">ABSTRACT</h1>
  <p class="no-indent center" style="font-weight: bold; font-style: italic; margin-bottom: 1rem;">
    [AUTHOR NAME]. [Student ID]. [English Title of Research / Thesis].
  </p>
  <p>
    <strong>[Background &amp; Problem Statement (~15–20%):]</strong> Describe the real-world research context, existing methodological limitations or literature gaps, and the primary objective of the proposed approach.
  </p>
  <p>
    <strong>[Methodology &amp; Experimental Protocol (~20–30%):]</strong> Detail the dataset or system specifications, preprocessing and engineering workflow, proposed architecture or method, and validation design applied in the study.
  </p>
  <p>
    <strong>[Key Findings &amp; Conclusion (~50%):]</strong> Report concrete quantitative evaluation metrics, baseline comparisons, statistical significance verification, and the main conclusion highlighting the scientific contribution.
  </p>
  <p class="no-indent" style="margin-top: 1rem;">
    <strong>Keywords:</strong> [Keyword 1], [Keyword 2], [Keyword 3], [Keyword 4], [Keyword 5].
  </p>
</div>
"""

BODY_HTML = """<!-- BAB I PENDAHULUAN -->
<div class="page-break">
  <h1 class="chapter">BAB I<br>PENDAHULUAN</h1>
  <h2>1.1 Latar Belakang Masalah</h2>
  <p>
    Latar belakang disusun secara deduktif (alur piramida terbalik) yang mengantarkan pembaca dari konteks makro menuju permasalahan spesifik yang diteliti. Setiap klaim empiris dan angka statistik wajib didukung referensi primer bereputasi.
  </p>
  <div class="guide-box">
    <strong>Panduan Substansi:</strong> (1) Konteks bidang &amp; urgensi masalah, (2) Kondisi ideal vs kesenjangan fakta di lapangan, (3) Kajian studi terdahulu &amp; keterbatasan metode yang ada (<em>research gap</em>), (4) Rasionalitas pemilihan pendekatan/metode usulan, (5) Nilai kebaruan (<em>novelty</em>) dan kontribusi terukur, serta (6) Penegasan fokus judul penelitian.
  </div>

  <h2>1.2 Identifikasi Masalah</h2>
  <p>Berdasarkan uraian latar belakang di atas, permasalahan pokok yang teridentifikasi meliputi:</p>
  <ol>
    <li>[Identifikasi kendala atau kesenjangan empiris pertama yang terjadi pada objek penelitian.]</li>
    <li>[Identifikasi keterbatasan teknis/metodologis pada penelitian atau sistem yang telah ada sebelumnya.]</li>
    <li>[Identifikasi kebutuhan pengukuran validitas atau efisiensi terhadap pendekatan solusi yang ditawarkan.]</li>
  </ol>

  <h2>1.3 Batasan Masalah</h2>
  <p>Agar pembahasan terarah dan mendalam, penelitian ini dibatasi pada ruang lingkup berikut:</p>
  <ol>
    <li>[Batasan cakupan data, populasi, sampel, atau domain objek studi yang dianalisis.]</li>
    <li>[Batasan parameter metode, arsitektur, alat bantu, atau lingkungan pengujian yang digunakan.]</li>
    <li>[Batasan metrik evaluasi yang menjadi tolok ukur keberhasilan penelitian.]</li>
  </ol>

  <h2>1.4 Rumusan Masalah</h2>
  <p>Rumusan masalah yang hendak dijawab dalam penelitian ini adalah:</p>
  <ol>
    <li>Bagaimana merancang dan mengimplementasikan [metode/sistem usulan] untuk menyelesaikan [permasalahan inti]?</li>
    <li>Bagaimana kinerja dan signifikansi peningkatan [metode/sistem usulan] dibandingkan dengan pendekatan pembanding berdasarkan metrik evaluasi yang ditetapkan?</li>
  </ol>

  <h2>1.5 Tujuan Penelitian</h2>
  <ol>
    <li>Merancang, mengimplementasikan, dan menguji [metode/sistem usulan] pada domain permasalahan yang diteliti.</li>
    <li>Mengukur secara kuantitatif dan menganalisis validitas kinerja pendekatan yang diusulkan terhadap metode pembanding.</li>
  </ol>

  <h2>1.6 Manfaat Penelitian</h2>
  <ol>
    <li><strong>Manfaat Teoritis / Akademis:</strong> Memberikan kontribusi konseptual dan bukti empiris pada kajian [bidang keilmuan penelitian].</li>
    <li><strong>Manfaat Praktis:</strong> Menghasilkan rancangan sistem atau model teruji yang dapat diaplikasikan secara efektif oleh pemangku kepentingan terkait.</li>
  </ol>
</div>

<!-- BAB II TINJAUAN PUSTAKA -->
<div class="page-break">
  <h1 class="chapter">BAB II<br>TINJAUAN PUSTAKA DAN LANDASAN TEORI</h1>
  <h2>2.1 Tinjauan Pustaka (Penelitian Terdahulu)</h2>
  <p>
    Bagian ini mensintesis secara kritis penelitian terdahulu yang relevan (disarankan minimal 10–15 artikel jurnal bereputasi 5 tahun terakhir), membandingkan metode, dataset, temuan, serta celah penelitian yang menjadi dasar kebaruan studi ini.
  </p>
  <p class="caption">Tabel 2.1 Matriks Perbandingan Penelitian Terdahulu</p>
  <table class="academic">
    <thead>
      <tr>
        <th style="width: 18%;">Peneliti (Tahun)</th>
        <th style="width: 24%;">Metode / Pendekatan</th>
        <th style="width: 24%;">Objek / Dataset</th>
        <th style="width: 34%;">Temuan &amp; Celah Penelitian</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>[Penulis A (Tahun)]</td>
        <td>[Metode Studi 1]</td>
        <td>[Karakteristik Data/Objek]</td>
        <td>[Hasil kunci dan keterbatasan yang diperbaiki]</td>
      </tr>
      <tr>
        <td>[Penulis B (Tahun)]</td>
        <td>[Metode Studi 2]</td>
        <td>[Karakteristik Data/Objek]</td>
        <td>[Hasil kunci dan keterbatasan yang diperbaiki]</td>
      </tr>
      <tr>
        <td><strong>Penelitian Ini</strong></td>
        <td><strong>[Pendekatan Usulan]</strong></td>
        <td><strong>[Dataset / Ruang Lingkup]</strong></td>
        <td><strong>[Integrasi solusi &amp; kebaruan terukur]</strong></td>
      </tr>
    </tbody>
  </table>

  <h2>2.2 Landasan Teori</h2>
  <p>
    Uraikan teori formal, definisi matematis, arsitektur konseptual, algoritma/metode inti, protokol pengujian, serta metrik evaluasi yang digunakan sebagai pijakan ilmiah dalam Bab III dan Bab IV.
  </p>

  <h2>2.3 Kerangka Pemikiran dan Hipotesis</h2>
  <p>
    Gambarkan alur logis keterkaitan antara permasalahan, landasan teori, metode yang diusulkan, dan keluaran yang diharapkan. Jika penelitian bersifat eksperimental komparatif, nyatakan hipotesis nol (H<sub>0</sub>) dan hipotesis alternatif (H<sub>1</sub>) secara tegas.
  </p>
</div>

<!-- BAB III METODOLOGI PENELITIAN -->
<div class="page-break">
  <h1 class="chapter">BAB III<br>METODOLOGI PENELITIAN</h1>
  <h2>3.1 Kerangka Kerja Penelitian</h2>
  <p>
    Jelaskan tahapan sistematis pelaksanaan penelitian (misalnya adaptasi kerangka kerja eksperimental, siklus rekayasa perangkat lunak, atau tahapan analisis kuantitatif) mulai dari perumusan masalah hingga evaluasi akhir.
  </p>

  <h2>3.2 Pengumpulan dan Karakteristik Data</h2>
  <p>
    Paparkan sumber perolehan data atau objek penelitian, periode pengambilan, jumlah sampel, distribusi kelas/kategori, kriteria inklusi/eksklusi, serta prosedur anotasi atau verifikasi kualitas data.
  </p>

  <h2>3.3 Tahapan Pra-pemrosesan dan Perancangan</h2>
  <p>
    Jabarkan proses pembersihan data, normalisasi, transformasi fitur, atau rancangan arsitektur sistem secara operasional agar eksperimen dapat direplikasi sepenuhnya oleh peneliti lain.
  </p>
  <p class="caption">Tabel 3.1 Operasionalisasi Variabel / Parameter Penelitian</p>
  <table class="academic">
    <thead>
      <tr>
        <th style="width: 22%;">Kode / Variabel</th>
        <th style="width: 38%;">Definisi Operasional</th>
        <th style="width: 20%;">Tipe / Skala</th>
        <th style="width: 20%;">Keterangan</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>[Variabel / Fitur 1]</td>
        <td>[Penjelasan rumus atau mekanisme pengukuran]</td>
        <td>[Numerik / Kategorikal]</td>
        <td>[Peran dalam model]</td>
      </tr>
      <tr>
        <td>[Variabel / Fitur 2]</td>
        <td>[Penjelasan rumus atau mekanisme pengukuran]</td>
        <td>[Numerik / Kategorikal]</td>
        <td>[Peran dalam model]</td>
      </tr>
    </tbody>
  </table>

  <h2>3.4 Arsitektur dan Konfigurasi Pengujian</h2>
  <p>
    Jelaskan skema pembagian data (<em>splitting protocol</em>) yang bebas kebocoran informasi (<em>data leakage</em>), ruang pencarian parameter (<em>hyperparameter tuning</em>), serta skenario model atau sistem pembanding (<em>baseline</em>).
  </p>

  <h2>3.5 Metrik Evaluasi dan Uji Signifikansi</h2>
  <p>
    Tetapkan metrik kuantitatif (misalnya akurasi, presisi, sensitivitas, waktu eksekusi, atau skala kepuasan pengguna) serta uji statistik yang dipakai untuk memverifikasi keabsahan perbedaan hasil antar skenario.
  </p>
</div>

<!-- BAB IV HASIL DAN PEMBAHASAN -->
<div class="page-break">
  <h1 class="chapter">BAB IV<br>HASIL DAN PEMBAHASAN</h1>
  <h2>4.1 Gambaran Umum Hasil Implementasi</h2>
  <p>
    Sajikan ringkasan statistik deskriptif data atau hasil implementasi sistem pada lingkungan uji yang telah didefinisikan pada Bab III. Sertakan spesifikasi perangkat keras dan perangkat lunak yang digunakan selama eksperimen.
  </p>

  <h2>4.2 Hasil Evaluasi Kinerja dan Perbandingan</h2>
  <p>
    Tampilkan hasil kuantitatif model atau sistem usulan secara objektif dan bandingkan secara langsung terhadap seluruh skenario pembanding (<em>baseline</em>) pada partisi evaluasi yang identik.
  </p>
  <p class="caption">Tabel 4.1 Rekapitulasi Perbandingan Kinerja Antar Skenario Uji</p>
  <table class="academic">
    <thead>
      <tr>
        <th style="width: 34%;">Skenario / Pendekatan</th>
        <th style="width: 16%;">Metrik 1</th>
        <th style="width: 16%;">Metrik 2</th>
        <th style="width: 16%;">Metrik 3</th>
        <th style="width: 18%;">Efisiensi Waktu</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>[Skenario Pembanding 1]</td>
        <td style="text-align: center;">[Nilai]</td>
        <td style="text-align: center;">[Nilai]</td>
        <td style="text-align: center;">[Nilai]</td>
        <td style="text-align: center;">[Durasi]</td>
      </tr>
      <tr>
        <td>[Skenario Pembanding 2]</td>
        <td style="text-align: center;">[Nilai]</td>
        <td style="text-align: center;">[Nilai]</td>
        <td style="text-align: center;">[Nilai]</td>
        <td style="text-align: center;">[Durasi]</td>
      </tr>
      <tr>
        <td><strong>[Pendekatan Usulan]</strong></td>
        <td style="text-align: center;"><strong>[Nilai]</strong></td>
        <td style="text-align: center;"><strong>[Nilai]</strong></td>
        <td style="text-align: center;"><strong>[Nilai]</strong></td>
        <td style="text-align: center;"><strong>[Durasi]</strong></td>
      </tr>
    </tbody>
  </table>

  <h2>4.3 Validasi Statistik dan Analisis Mendalam</h2>
  <p>
    Laporkan hasil uji signifikansi statistik (nilai statistik uji beserta nilai <em>p-value</em>), interpretasi kontribusi komponen/fitur penting, serta visualisasi kurva atau grafik pendukung dengan resolusi tinggi.
  </p>

  <h2>4.4 Pembahasan dan Analisis Kesalahan (<em>Error Analysis</em>)</h2>
  <p>
    Bahas mengapa pendekatan yang diusulkan bekerja lebih efektif, kaitkan temuan dengan literatur pada Bab II, dan bedah kasus-kasus kesalahan atau keterbatasan aktual secara jujur dan ilmiah.
  </p>
</div>

<!-- BAB V KESIMPULAN DAN SARAN -->
<div class="page-break">
  <h1 class="chapter">BAB V<br>KESIMPULAN DAN SARAN</h1>
  <h2>5.1 Kesimpulan</h2>
  <p>
    Kesimpulan menjawab seluruh butir rumusan masalah pada Bab I secara langsung, padat, dan berbasis bukti kuantitatif dari Bab IV (proporsi 60–70% dari Bab V). Hindari pengulangan teori umum atau klaim di luar data pengujian.
  </p>
  <ol>
    <li>[Simpulan 1: Menjawab rumusan masalah pertama terkait implementasi dan arsitektur yang berhasil dibangun.]</li>
    <li>[Simpulan 2: Menjawab rumusan masalah kedua disertai angka capaian kinerja dan validitas statistiknya.]</li>
  </ol>

  <h2>5.2 Saran</h2>
  <p>
    Saran merumuskan rekomendasi teknis lanjutan berdasarkan keterbatasan yang teridentifikasi selama penelitian (proporsi 30–40% dari Bab V):
  </p>
  <ol>
    <li>[Saran pengembangan metodologis atau perluasan cakupan data/domain pada penelitian berikutnya.]</li>
    <li>[Saran optimalisasi efisiensi komputasi atau integrasi implementasi pada skala produksi.]</li>
  </ol>
</div>

<!-- DAFTAR PUSTAKA -->
<div class="page-break">
  <h1 class="chapter">DAFTAR PUSTAKA</h1>
  <p class="no-indent" style="font-size: 11pt; margin-bottom: 0.8rem;">
    Susun daftar pustaka secara alfabetis menggunakan format standar internasional (APA Edisi ke-7 atau IEEE), pastikan setiap entri disitasi dalam naskah dan dilengkapi tautan DOI resmi bila tersedia.
  </p>
  <p class="no-indent" style="padding-left: 1cm; text-indent: -1cm;">
    Penulis, A. A., &amp; Penulis, B. B. (Tahun). Judul artikel penelitian ilmiah. <em>Nama Jurnal Ilmiah Bereputasi</em>, Volume(Nomor), Halaman awal–akhir. https://doi.org/10.xxxx/xxxxx
  </p>
  <p class="no-indent" style="padding-left: 1cm; text-indent: -1cm;">
    Penulis, C. C. (Tahun). <em>Judul buku atau prosiding konferensi ilmiah internasional</em> (Edisi ke-x). Nama Penerbit Akademik. https://doi.org/10.xxxx/xxxxx
  </p>
</div>

<!-- LAMPIRAN A -->
<div class="page-break">
  <h1 class="chapter">LAMPIRAN A<br>KODE SUMBER / INSTRUMEN PENELITIAN</h1>
  <p class="no-indent">
    Sertakan cuplikan kode inti yang terverifikasi bebas kesalahan sintaksis, instrumen kuesioner, atau lembar log pengujian eksperimen pada bagian ini.
  </p>
  <pre class="code-block"># Contoh blok dokumentasi kode / skrip eksperimen yang telah diverifikasi
def run_experiment_pipeline(dataset, config):
    # Kerangka fungsi eksperimen modular dan bebas kebocoran data
    pass</pre>
</div>

<!-- LAMPIRAN B -->
<div class="page-break">
  <h1 class="chapter">LAMPIRAN B<br>BIODATA PENULIS</h1>
  <table style="width: 100%; border-collapse: collapse; font-size: 11pt; line-height: 1.6; margin-bottom: 1.2rem;">
    <tr><td style="width: 34%; font-weight: bold; padding: 3px 0;">Nama Lengkap</td><td style="width: 3%;">:</td><td>[Nama Penulis Disini]</td></tr>
    <tr><td style="font-weight: bold; padding: 3px 0;">Nomor Induk Mahasiswa</td><td>:</td><td>[Nomor Induk Disini]</td></tr>
    <tr><td style="font-weight: bold; padding: 3px 0;">Tempat, Tanggal Lahir</td><td>:</td><td>[Tempat, Tanggal Lahir Disini]</td></tr>
    <tr><td style="font-weight: bold; padding: 3px 0;">Program Studi</td><td>:</td><td>[Nama Program Studi Disini]</td></tr>
    <tr><td style="font-weight: bold; padding: 3px 0;">Institusi / Perguruan Tinggi</td><td>:</td><td>[Nama Universitas / Institusi Disini]</td></tr>
    <tr><td style="font-weight: bold; padding: 3px 0;">Alamat Surel (Email)</td><td>:</td><td>[Email Penulis Disini]</td></tr>
  </table>
  <p class="no-indent" style="font-weight: bold; margin-bottom: 0.3rem;">Riwayat Pendidikan Formal:</p>
  <ol style="margin-left: 1cm;">
    <li>[Nama Sekolah Dasar Disini] (Lulus Tahun [Tahun])</li>
    <li>[Nama Sekolah Menengah Pertama Disini] (Lulus Tahun [Tahun])</li>
    <li>[Nama Sekolah Menengah Atas / Kejuruan Disini] (Lulus Tahun [Tahun])</li>
    <li>[Nama Universitas / Institusi Disini] ([Tahun Masuk] – [Tahun Lulus])</li>
  </ol>
</div>
"""


def build_toc(page_map):
    def gp(k, default=1):
        return page_map.get(k, default)

    b1, s14 = gp("BAB_I", 1), gp("S1_4", gp("BAB_I", 1))
    b2 = gp("BAB_II", 3)
    b3 = gp("BAB_III", 4)
    b4 = gp("BAB_IV", 5)
    b5 = gp("BAB_V", 6)
    dp = gp("DAFTAR_PUSTAKA", 7)
    la = gp("LAMPIRAN_A", 8)
    lb = gp("LAMPIRAN_B", 9)

    return f"""<!-- DAFTAR ISI -->
<div class="page-break">
  <h1 class="chapter" style="margin-bottom: 0.6rem;">DAFTAR ISI</h1>
  <div style="font-size: 10pt; line-height: 1.24;">
    <div class="toc-item"><span><strong>HALAMAN JUDUL</strong></span><span class="toc-dots"></span><span>i</span></div>
    <div class="toc-item"><span><strong>LEMBAR PENGESAHAN</strong></span><span class="toc-dots"></span><span>ii</span></div>
    <div class="toc-item"><span><strong>PERNYATAAN KEASLIAN KARYA ILMIAH</strong></span><span class="toc-dots"></span><span>iii</span></div>
    <div class="toc-item"><span><strong>KATA PENGANTAR</strong></span><span class="toc-dots"></span><span>iv</span></div>
    <div class="toc-item"><span><strong>ABSTRAK</strong></span><span class="toc-dots"></span><span>v</span></div>
    <div class="toc-item"><span><strong>ABSTRACT</strong></span><span class="toc-dots"></span><span>vi</span></div>
    <div class="toc-item"><span><strong>DAFTAR ISI</strong></span><span class="toc-dots"></span><span>vii</span></div>
    <div class="toc-item"><span><strong>DAFTAR TABEL</strong></span><span class="toc-dots"></span><span>viii</span></div>
    <div class="toc-item"><span><strong>DAFTAR GAMBAR</strong></span><span class="toc-dots"></span><span>ix</span></div>

    <div class="toc-item" style="margin-top: 0.25rem;"><span><strong>BAB I PENDAHULUAN</strong></span><span class="toc-dots"></span><span>{b1}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>1.1 Latar Belakang Masalah</span><span class="toc-dots"></span><span>{gp("S1_1", b1)}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>1.2 Identifikasi Masalah</span><span class="toc-dots"></span><span>{gp("S1_2", b1)}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>1.3 Batasan Masalah</span><span class="toc-dots"></span><span>{gp("S1_3", b1)}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>1.4 Rumusan Masalah</span><span class="toc-dots"></span><span>{s14}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>1.5 Tujuan Penelitian</span><span class="toc-dots"></span><span>{gp("S1_5", s14)}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>1.6 Manfaat Penelitian</span><span class="toc-dots"></span><span>{gp("S1_6", s14)}</span></div>

    <div class="toc-item" style="margin-top: 0.25rem;"><span><strong>BAB II TINJAUAN PUSTAKA DAN LANDASAN TEORI</strong></span><span class="toc-dots"></span><span>{b2}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>2.1 Tinjauan Pustaka (Penelitian Terdahulu)</span><span class="toc-dots"></span><span>{gp("S2_1", b2)}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>2.2 Landasan Teori</span><span class="toc-dots"></span><span>{gp("S2_2", b2)}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>2.3 Kerangka Pemikiran dan Hipotesis</span><span class="toc-dots"></span><span>{gp("S2_3", b2)}</span></div>

    <div class="toc-item" style="margin-top: 0.25rem;"><span><strong>BAB III METODOLOGI PENELITIAN</strong></span><span class="toc-dots"></span><span>{b3}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>3.1 Kerangka Kerja Penelitian</span><span class="toc-dots"></span><span>{gp("S3_1", b3)}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>3.2 Pengumpulan dan Karakteristik Data</span><span class="toc-dots"></span><span>{gp("S3_2", b3)}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>3.3 Tahapan Pra-pemrosesan dan Perancangan</span><span class="toc-dots"></span><span>{gp("S3_3", b3)}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>3.4 Arsitektur dan Konfigurasi Pengujian</span><span class="toc-dots"></span><span>{gp("S3_4", b3)}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>3.5 Metrik Evaluasi dan Uji Signifikansi</span><span class="toc-dots"></span><span>{gp("S3_5", b3)}</span></div>

    <div class="toc-item" style="margin-top: 0.25rem;"><span><strong>BAB IV HASIL DAN PEMBAHASAN</strong></span><span class="toc-dots"></span><span>{b4}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>4.1 Gambaran Umum Hasil Implementasi</span><span class="toc-dots"></span><span>{gp("S4_1", b4)}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>4.2 Hasil Evaluasi Kinerja dan Perbandingan</span><span class="toc-dots"></span><span>{gp("S4_2", b4)}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>4.3 Validasi Statistik dan Analisis Mendalam</span><span class="toc-dots"></span><span>{gp("S4_3", b4)}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>4.4 Pembahasan dan Analisis Kesalahan</span><span class="toc-dots"></span><span>{gp("S4_4", b4)}</span></div>

    <div class="toc-item" style="margin-top: 0.25rem;"><span><strong>BAB V KESIMPULAN DAN SARAN</strong></span><span class="toc-dots"></span><span>{b5}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>5.1 Kesimpulan</span><span class="toc-dots"></span><span>{gp("S5_1", b5)}</span></div>
    <div class="toc-item" style="padding-left: 1.4rem;"><span>5.2 Saran</span><span class="toc-dots"></span><span>{gp("S5_2", b5)}</span></div>

    <div class="toc-item" style="margin-top: 0.25rem;"><span><strong>DAFTAR PUSTAKA</strong></span><span class="toc-dots"></span><span>{dp}</span></div>
    <div class="toc-item" style="margin-top: 0.2rem;"><span><strong>LAMPIRAN A KODE SUMBER / INSTRUMEN PENELITIAN</strong></span><span class="toc-dots"></span><span>{la}</span></div>
    <div class="toc-item" style="margin-top: 0.2rem;"><span><strong>LAMPIRAN B BIODATA PENULIS</strong></span><span class="toc-dots"></span><span>{lb}</span></div>
  </div>
</div>

<!-- DAFTAR TABEL -->
<div class="page-break">
  <h1 class="chapter">DAFTAR TABEL</h1>
  <div style="font-size: 11pt; line-height: 1.6;">
    <div class="toc-item"><span>Tabel 2.1 Matriks Perbandingan Penelitian Terdahulu</span><span class="toc-dots"></span><span>{gp("T2_1", b2)}</span></div>
    <div class="toc-item"><span>Tabel 3.1 Operasionalisasi Variabel / Parameter Penelitian</span><span class="toc-dots"></span><span>{gp("T3_1", b3)}</span></div>
    <div class="toc-item"><span>Tabel 4.1 Rekapitulasi Perbandingan Kinerja Antar Skenario Uji</span><span class="toc-dots"></span><span>{gp("T4_1", b4)}</span></div>
  </div>
</div>

<!-- DAFTAR GAMBAR -->
<div class="page-break">
  <h1 class="chapter">DAFTAR GAMBAR</h1>
  <div style="font-size: 11pt; line-height: 1.6;">
    <div class="toc-item"><span>Gambar 3.1 Diagram Alir Tahapan Metodologi Penelitian</span><span class="toc-dots"></span><span>{b3}</span></div>
    <div class="toc-item"><span>Gambar 4.1 Visualisasi Grafik Hasil Evaluasi Penelitian</span><span class="toc-dots"></span><span>{b4}</span></div>
  </div>
</div>
"""


def make_page_overlay(page_w, page_h, text, position="bottom-center"):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(page_w, page_h))
    can.setFont("Times-Roman", 11)
    if position == "bottom-center":
        can.drawCentredString(page_w / 2.0, 56.7, text)
    elif position == "top-right":
        can.drawRightString(page_w - 70.87, page_h - 56.7, text)
    can.save()
    packet.seek(0)
    return pypdf.PdfReader(packet).pages[0]


def render_html_to_pdf(html_path, pdf_path):
    subprocess.run([
        EDGE_PATH, '--headless', '--disable-gpu', '--no-pdf-header-footer',
        '--run-all-compositor-stages-before-draw', f'--print-to-pdf={pdf_path}', html_path
    ], check=True)


def main():
    temp_body_html = os.path.join(TOOLS_DIR, 'temp_body.html')
    temp_body_pdf = os.path.join(TOOLS_DIR, 'temp_body_raw.pdf')
    temp_front_html = os.path.join(TOOLS_DIR, 'temp_front.html')
    temp_front_pdf = os.path.join(TOOLS_DIR, 'temp_front_raw.pdf')

    with open(temp_body_html, 'w', encoding='utf-8') as f:
        f.write(HTML_HEAD + BODY_HTML + '</body></html>')
    render_html_to_pdf(temp_body_html, temp_body_pdf)

    reader_body = pypdf.PdfReader(temp_body_pdf)
    page_map = {}
    chapter_openers = set()
    chapter_markers = [
        ("BAB_I", "BAB I"), ("BAB_II", "BAB II"), ("BAB_III", "BAB III"),
        ("BAB_IV", "BAB IV"), ("BAB_V", "BAB V"),
        ("DAFTAR_PUSTAKA", "DAFTAR PUSTAKA"),
        ("LAMPIRAN_A", "LAMPIRAN A"), ("LAMPIRAN_B", "LAMPIRAN B")
    ]
    sub_markers = [
        ("S1_1", "1.1 Latar Belakang"), ("S1_2", "1.2 Identifikasi"), ("S1_3", "1.3 Batasan"),
        ("S1_4", "1.4 Rumusan"), ("S1_5", "1.5 Tujuan"), ("S1_6", "1.6 Manfaat"),
        ("S2_1", "2.1 Tinjauan"), ("S2_2", "2.2 Landasan"), ("S2_3", "2.3 Kerangka"),
        ("S3_1", "3.1 Kerangka"), ("S3_2", "3.2 Pengumpulan"), ("S3_3", "3.3 Tahapan"),
        ("S3_4", "3.4 Arsitektur"), ("S3_5", "3.5 Metrik"),
        ("S4_1", "4.1 Gambaran"), ("S4_2", "4.2 Hasil"), ("S4_3", "4.3 Validasi"), ("S4_4", "4.4 Pembahasan"),
        ("S5_1", "5.1 Kesimpulan"), ("S5_2", "5.2 Saran"),
        ("T2_1", "Tabel 2.1"), ("T3_1", "Tabel 3.1"), ("T4_1", "Tabel 4.1")
    ]
    for i, page in enumerate(reader_body.pages):
        txt = page.extract_text() or ""
        pnum = i + 1
        for key, marker in chapter_markers:
            if marker in txt and key not in page_map:
                page_map[key] = pnum
                chapter_openers.add(pnum)
        for key, marker in sub_markers:
            if marker in txt and key not in page_map:
                page_map[key] = pnum

    toc_html = build_toc(page_map)
    with open(temp_front_html, 'w', encoding='utf-8') as f:
        f.write(HTML_HEAD + FRONT_BEFORE_TOC + toc_html + '</body></html>')
    render_html_to_pdf(temp_front_html, temp_front_pdf)

    reader_front = pypdf.PdfReader(temp_front_pdf)
    writer = pypdf.PdfWriter()

    romans = ["", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii"]
    for idx, page in enumerate(reader_front.pages):
        added = writer.add_page(page)
        if idx > 0:
            num_str = romans[idx] if idx < len(romans) else str(idx + 1)
            added.merge_page(make_page_overlay(float(page.mediabox.width), float(page.mediabox.height), num_str, "bottom-center"))

    for idx, page in enumerate(reader_body.pages):
        pnum = idx + 1
        added = writer.add_page(page)
        pos = "bottom-center" if pnum in chapter_openers else "top-right"
        added.merge_page(make_page_overlay(float(page.mediabox.width), float(page.mediabox.height), str(pnum), pos))

    with open(OUTPUT_PDF, 'wb') as f:
        writer.write(f)

    for tmp in [temp_body_html, temp_body_pdf, temp_front_html, temp_front_pdf]:
        if os.path.exists(tmp):
            os.remove(tmp)

    print(f"Generated universal PDF template: {OUTPUT_PDF} ({len(reader_front.pages)} front + {len(reader_body.pages)} body = {len(writer.pages)} pages)")


if __name__ == '__main__':
    main()
