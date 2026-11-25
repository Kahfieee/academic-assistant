# Academic Assistant: Universal Research & Scientific Manuscript Framework

[![License: MIT / CC BY-NC 4.0](https://img.shields.io/badge/License-MIT%20%2F%20CC%20BY--NC%204.0-blue.svg)](LICENSE)
[![Methodology: CO--STAR & PRISMA](https://img.shields.io/badge/Workflow-CO--STAR%20%26%20PRISMA-orange.svg)]()

**Academic Assistant** adalah ekosistem kerangka kerja terpadu yang dirancang untuk membantu mahasiswa, peneliti, dan akademisi lintas disiplin ilmu dalam menjalankan keseluruhan siklus riset ilmiah: mulai dari eksplorasi literatur sistematis, perumusan kerangka metodologi, penyusunan naskah tesis/tugas akhir, simulasi *peer review*, pemformatan dokumen formal kampus, hingga adaptasi publikasi konferensi atau jurnal internasional.

Repositori ini bersifat **universal** (tidak terikat pada satu topik penelitian, algoritma tertentu, maupun institusi tertentu) sehingga dapat langsung diadaptasi oleh siapa saja sesuai bidang kajian masing-masing.

---

## 🎯 Kemampuan Utama (*Core Capabilities*)

1. **Eksplorasi Riset & Sintesis Literatur Sistematis**
   - Pemetaan celah penelitian (*research gap*), perumusan pertanyaan riset, serta perancangan metodologi kuantitatif, kualitatif, maupun eksperimental.
   - Penyaringan studi (*title/abstract* dan *full-text screening*) berstandar protokol PRISMA 2020 beserta sintesis bukti ilmiah dan analisis risiko bias.
   - Penegakan integritas sitasi primer bereputasi (anti-halusinasi referensi dan validasi tautan DOI).

2. **Penyusunan Naskah Karya Ilmiah Terstruktur**
   - Panduan penyusunan naskah ilmiah secara koheren berbasis kerangka metodologis CO-STAR—menjamin keselarasan logis antara latar belakang, tinjauan pustaka, rancangan metodologi, analisis hasil evaluasi, hingga simpulan dan arah riset lanjutan.
   - Dukungan berbagai mode penulisan: perancangan *outline*, penyusunan draf penuh, kalibrasi gaya bahasa akademik, penajaman argumen, serta penyusunan abstrak dwibahasa.

3. **Simulasi *Peer Review* & Kontrol Kualitas Naskah**
   - Evaluasi kritis multi-perspektif (kesesuaian jurnal/konferensi, ketajaman metodologi, penelaahan klaim, serta *devil's advocate* untuk mendeteksi kelemahan argumen sebelum sidang atau *submission*).
   - Orkestrasi alur riset ujung-ke-ujung (*research → draft → integrity check → peer review → revision → finalization*).

4. **Pemformatan Dokumen Akademik & Adaptasi Publikasi IEEE**
   - Master template dokumen naskah akhir berstandar akademik universal dalam format **Word (`.docx`)** dan **PDF (`.pdf`)** lengkap dengan margin 4-4-3-3 cm, tipografi Times New Roman, sistem penomoran ganda (Romawi & Arab), serta *placeholder* identitas yang siap pakai.
   - Modul transformasi untuk mengondensasi karya ilmiah panjang menjadi artikel publikasi internasional dua kolom standar IEEE (beserta template LaTeX dan pengelolaan referensi BibTeX).

---

## 🧩 Daftar Skill AI yang Terintegrasi

Seluruh modul skill tersimpan di `.agents/skills/` (serta `.skills/` untuk kompatibilitas lintas *agent*) sehingga otomatis dikenali oleh **Google Antigravity**, **Claude Code**, dan asisten AI berbasis skill lainnya:

| Nama Modul | Fungsi & Kegunaan Utama |
| :--- | :--- |
| **`deep-research`** | Orkestrasi riset mendalam: perumusan pertanyaan ilmiah, penelusuran literatur sistematis, sintesis lintas sumber, tinjauan risiko bias, dan penyusunan laporan akademik. |
| **`sr-screener`** | Penyaringan literatur sistematis berbasis protokol kelayakan (*title/abstract* hingga *full-text screening*), penghitungan alur PRISMA 2020, serta resolusi konflik inklusi. |
| **`academic-paper`** | Asisten penulisan artikel ilmiah multi-agen yang mendukung penyusunan kerangka, penulisan naskah penuh, tinjauan pustaka, audit sitasi, revisi, dan penyusunan *rebuttal*. |
| **`academic-paper-reviewer`** | Panel penelaah sejawat (*peer reviewer*) simulasi dari berbagai sudut pandang untuk mengevaluasi kelayakan metodologi, integritas data, dan kekuatan naskah sebelum dikirim. |
| **`academic-pipeline`** | Orkestrator alur penuh 10 tahap yang menghubungkan riset mendalam, penulisan naskah, pemeriksaan integritas, *peer review* dua tahap, hingga finalisasi manuskrip. |
| **`menulis-skripsi`** | Modul panduan penyusunan tugas akhir dan karya ilmiah mahasiswa berbasis alur metodologis CO-STAR—membantu menjaga konsistensi judul, masalah, metode, hasil, dan kesimpulan. |
| **`skripsi-to-ieee`** | Modul restrukturisasi dan konversi naskah tugas akhir menjadi artikel publikasi ilmiah berstandar dua kolom IEEE (dilengkapi template LaTeX dan pedoman pemformatan). |

---

## 📁 Struktur Direktori

```text
academic-assistant/
├── .agents/
│   ├── rules/
│   │   └── mandatory-academic-standards.md   # Aturan baku otomatis (always-on)
│   └── skills/                               # Modul AI Agent Skills terintegrasi
│       ├── academic-paper/
│       ├── academic-paper-reviewer/
│       ├── academic-pipeline/
│       ├── deep-research/
│       ├── sr-screener/
│       ├── menulis-skripsi/
│       ├── skripsi-to-ieee/
│       └── shared/
├── templates/                                # Master Template Skripsi & Jurnal
│   ├── TEMPLATE_SKRIPSI_DAN_JURNAL.md        # Blueprint ketentuan wajib & kerangka bab
│   ├── formal_thesis_template.docx           # Template Microsoft Word (Margin 4-4-3-3 cm)
│   └── formal_thesis_template.pdf            # Referensi Layout PDF (Penomoran Romawi & Arab)
├── assets/                                   # Placeholder logo institusi untuk sampul
│   └── university_logo_placeholder.png
├── tools/                                    # Skrip generator dokumen otomatis (DOCX & PDF)
│   ├── build_pdf.py
│   ├── generate_docx.js
│   └── package.json
├── AGENTS.md / CLAUDE.md / GEMINI.md         # Instruksi otomatis lintas AI coding agent
├── LICENSE                                   # Informasi Lisensi (MIT & CC BY-NC 4.0)
├── THIRD_PARTY_NOTICES.md                    # Atribusi sumber eksternal
└── README.md
```

---

## 📌 Ketentuan Baku Otomatis (Skripsi & Jurnal)

Setiap kali repositori ini dipasang ke ruang kerja agen AI dan pengguna meminta penyusunan **skripsi, tugas akhir, atau artikel jurnal**, asisten akan secara otomatis menerapkan standar wajib berikut:

1. **Alur Topik & Outline:** Analisis artikel referensi (5 alternatif topik) → pilih **1 topik terbaik** → **justifikasi ≤ 50 kata** & **ringkasan ±250 kata** → **outline sistematis**.
2. **Standar Literatur Scopus Q1/Q2 & Sitasi APA 7:** Pertanyaan pencarian dalam Bahasa Inggris per subbab; minimal **5 referensi** per pertanyaan dari jurnal **Scopus Q1/Q2** berbahasa Inggris, **Open Access & aktif (tidak *discontinued*)**, terbitan **2021–2026**, dengan **≥5 sitasi**; format keluaran berupa 1 paragraf 150 kata berlabel **`Citation:`** diikuti daftar pustaka ber-DOI berlabel **`Bibliography:`** (tanpa memisahkan daftar artikel terpilih).
3. **Target Panjang & Substansi:** **BAB I** (±1.500 kata), **BAB II** (±2.500 kata), **BAB III** (±2.500 kata), **BAB IV** (±2.500 kata), **BAB V** (±750 kata), dan **Abstrak** (±250 kata dalam 1 paragraf + ±5 kata kunci).

---

## 🚀 Cara Penggunaan

1. **Kloning Repositori**
   ```bash
   git clone https://github.com/Kahfieee/academic-assistant.git
   ```
2. **Aktifkan di Workspace Agen AI**  
   Buka folder `academic-assistant` di **Google Antigravity** atau *coding agent* pilihan Anda. Seluruh skill di `.agents/skills/` akan aktif secara otomatis untuk membantu riset di bidang apa pun.
3. **Gunakan Template Dokumen Formal**  
   - Buka `templates/formal_thesis_template.docx` untuk mulai menyusun naskah tugas akhir Anda dengan mengganti seluruh entri bertanda kurung siku `[...]` serta logo pada `assets/university_logo_placeholder.png`.
   - Jika ingin mengustomisasi generator otomatis di `tools/`, pasang dependensi Node.js terlebih dahulu (`cd tools && npm install`), lalu jalankan `node generate_docx.js` atau `python build_pdf.py`.

---

## 📄 Lisensi & Atribusi

* Template dokumen (`templates/`), utilitas generator (`tools/`), serta modul `menulis-skripsi` dan `skripsi-to-ieee` dirilis di bawah lisensi **MIT License**.
* Modul `academic-paper`, `academic-paper-reviewer`, `academic-pipeline`, `deep-research`, `sr-screener`, dan `shared` berasal dari [**Imbad0202/academic-research-skills**](https://github.com/Imbad0202/academic-research-skills) (DOI: [10.5281/zenodo.20696614](https://doi.org/10.5281/zenodo.20696614)) karya Cheng-I Wu di bawah lisensi **CC BY-NC 4.0** (lihat [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)).
