---
name: menulis-skripsi
description: "Standar WAJIB penulisan skripsi, tugas akhir, proposal penelitian, dan artikel jurnal. Aktif otomatis setiap kali pengguna meminta membuat skripsi, menyusun bab, menentukan topik, atau mencari literatur (termasuk permintaan bahasa alami tanpa slash command). Menjamin 5 alternatif topik → 1 topik terbaik → justifikasi ≤50 kata & ringkasan ±250 kata → outline sistematis → literatur Scopus Q1/Q2 (2021–2026, Open Access aktif, ≥5 sitasi, APA 7 + DOI, format Citation: 150 kata + Bibliography:) → target panjang Bab I (±1.500), Bab II (±2.500), Bab III (±2.500), Bab IV (±2.500), Bab V (±750), dan Abstrak (±250 kata + ±5 kata kunci)."
version: 2.1.0
---

# Academic Thesis & Journal Writing Standard (WAJIB)

Setiap kali pengguna meminta penyusunan **skripsi, tugas akhir, atau naskah jurnal** (baik memakai perintah singkat maupun bahasa alami biasa seperti *"buatkan skripsi tentang..."*), asisten **WAJIB** menjalankan seluruh ketentuan di bawah ini secara otomatis sebagai template baku.

---

## 1. Alur Perencanaan & Penetapan Topik (WAJIB)

1. **Eksplorasi Topik (`/unggah-artikel` atau saat menelaah paper rujukan):**
   - Analisis artikel referensi utama dengan memetakan: fokus penelitian, masalah, metode, data/objek, temuan, keterbatasan, serta peluang penelitian lanjutan.
   - Hasilkan **5 alternatif topik** yang relevan dan realistis.
2. **Penetapan Topik (`/tentukan-topik`):**
   - Pilih **tepat 1 topik terbaik** yang selaras dengan Program Studi dan Bidang Keahlian/Peminatan, memiliki masalah penelitian yang jelas, realistis, dan layak dikembangkan.
3. **Justifikasi & Ringkasan Topik (`/justifikasi-topik`):**
   - **Justifikasi topik:** **maksimal 50 kata**.
   - **Ringkasan topik:** **maksimal ±250 kata**, wajib memuat rumusan masalah, tujuan, manfaat, *novelty*/kebaruan, dan ruang lingkup penelitian.
4. **Kerangka (*Outline*, `/tulis-outline`):**
   - Susun secara sistematis sesuai Program Studi, Bidang Peminatan, topik penelitian, dan metodologi yang dipilih.

---

## 2. Ketentuan Literatur, Referensi & Sitasi (WAJIB & DIUTAMAKAN)

Setiap pencarian dan penyusunan literatur untuk mendukung penulisan bab atau jurnal **WAJIB** memenuhi seluruh kriteria berikut:

- **Bahasa Pencarian (`/pertanyaan-literatur`):** Pertanyaan pencarian literatur (*literature search questions*) untuk setiap subbab, sub-subbab, dan poin penting pada outline disusun dalam **Bahasa Inggris**.
- **Jumlah Minimal:** Minimal **5 referensi** yang sangat relevan untuk setiap pertanyaan pencarian literatur.
- **Indeksasi Jurnal:** Jurnal ilmiah internasional terkemuka terindeks **Scopus Q1 atau Scopus Q2**.
- **Bahasa Referensi:** **Berbahasa Inggris**.
- **Akses & Status Jurnal:** Bersifat **Open Access** dan masih aktif (**tidak *discontinued***).
- **Rentang Tahun Terbit:** Maksimal **5 tahun terakhir (2021–2026)**.
- **Jumlah Sitasi:** Memiliki sitasi tinggi, **minimal 5 sitasi** dari jurnal ilmiah yang relevan.
- **Gaya Sitasi & Daftar Pustaka:** Standar **APA 7** dengan kutipan dalam teks `(Author et al., YEAR)` serta daftar pustaka lengkap yang **wajib mencantumkan DOI**.
- **Format Sintesis Sitasi (WAJIB PERSIS):**
  - **Tidak menuliskan daftar artikel yang dipilih secara terpisah** (*Do not write selected articles*).
  - Gabungkan seluruh pernyataan sitasi dalam **Bahasa Inggris** dari referensi yang ditemukan menjadi **1 paragraf utuh sepanjang 150 kata** dalam format **APA 7** berlabel **`Citation:`**.
  - Ikuti langsung dengan daftar pustaka lengkap ber-DOI berlabel **`Bibliography:`**.

### Template Kueri Pencarian Literatur
> `'[Literature search question in English?]' that is highly relevant to the following research title: '[Research title in English]'. Find at least 5 references that meet the following criteria: leading international scientific journals indexed by Scopus Q1 or Scopus Q2, in English, with a high number of citations, open access, journals that are not discontinued, published in the last five years (2021-2026), with at least 5 citations from relevant scientific journals. Do not write selected articles. Write and combine all citations statement in English from each reference found, in a complete paragraph of 150 words in APA 7 format. At the beginning, write the title ("Citation:"). Write a complete list of references with doi. At the beginning, write the title ("Bibliography:").`

---

## 3. Ketentuan Isi & Target Panjang Naskah (WAJIB)

| Bagian | Perintah | Target Panjang | Ketentuan Substansi Wajib |
| :--- | :--- | :--- | :--- |
| **BAB I Pendahuluan** | `/tulis-bab-1` | **±1.500 kata** | Mengikuti struktur outline, menggunakan sitasi `(Author et al., YEAR)`, serta menjaga kesinambungan masalah, tujuan, kontribusi, dan ruang lingkup penelitian. |
| **BAB II Tinjauan Pustaka** | `/tulis-bab-2` | **±2.500 kata** | Membahas konsep, teori, perkembangan literatur, penelitian terdahulu, *gap* penelitian, dan hubungan literatur dengan penelitian secara sintetis dan akademik. |
| **BAB III Metodologi Penelitian** | `/tulis-bab-3` | **±2.500 kata** | Operasional dan sistematis; menjelaskan keterkaitan rumusan masalah, tujuan, data, metode, eksperimen, pengujian, dan evaluasi penelitian. |
| **BAB IV Hasil dan Pembahasan** | `/tulis-bab-4` | **±2.500 kata** | Menyajikan hasil secara objektif (didukung data/tabel/grafik/*confusion matrix*), menginterpretasikan hasil, menjawab tujuan penelitian, dan membandingkan temuan dengan penelitian terdahulu. |
| **BAB V Simpulan dan Saran** | `/tulis-bab-5` | **±750 kata** | Simpulan menjawab tujuan dan *research question* serta menjelaskan makna dan kontribusi temuan; saran diarahkan pada tindak lanjut dan penelitian selanjutnya. |
| **Abstrak & Kata Kunci** | `/tulis-abstrak` | **±250 kata (1 paragraf)** | Mencakup masalah, tujuan, metode, hasil utama, interpretasi, simpulan, dan implikasi; dilengkapi **±5 kata kunci**. |

---

## 4. Prinsip Integritas Akademik (Anti-Fabrikasi)
- Dilarang keras mengarang sitasi, DOI, metrik akurasi, atau data pengujian fiktif.
- Jika pengguna belum menyertakan data eksperimen riil untuk Bab IV atau referensi terverifikasi untuk Bab I–III, susun draf atau tuntun pengguna melampirkan/memverifikasi referensi Scopus Q1/Q2 serta data hasil uji terlebih dahulu sebelum menghasilkan angka final.
