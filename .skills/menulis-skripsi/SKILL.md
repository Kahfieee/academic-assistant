---
name: menulis-skripsi
description: Panduan penulisan karya ilmiah, skripsi, dan tugas akhir terstruktur berbasis metodologi CO-STAR. Mengatur 11 tahapan riset dan penulisan (analisis artikel rujukan, penentuan topik, justifikasi kebaruan, outline, pertanyaan literatur, Bab I–V, hingga abstrak) beserta standar ketat pencarian literatur Scopus Q1/Q2 dan format sitasi APA 7.
version: 2.0.0
---

# Academic Thesis & Research Writing Skill

Modul panduan terstruktur untuk menyusun skripsi, tesis, dan karya ilmiah secara sistematis dari tahap penemuan topik hingga abstrak akhir dengan menjaga integritas akademik dan konsistensi antarbagian.

---

## 1. Prinsip Wajib & Aturan Integritas Ilmiah

1. **Anti-Halusinasi & Larangan Fabrikasi:**
   - Dilarang mengarang referensi, DOI, dataset, jumlah sampel, parameter eksperimen, tabel hasil, metrik evaluasi, atau kesimpulan yang tidak didukung data riil.
   - Pada penulisan Bab I, II, III, dan IV, asisten **wajib meminta dan memverifikasi** pernyataan sitasi serta data eksperimen/hasil riil sebelum menyusun narasi.
2. **Kesesuaian Jenjang Akademik (S-1 / D-3 / Sarjana):**
   - *Novelty* (kebaruan) harus realistis dan terukur (misal: komparasi metode, optimasi parameter, integrasi fitur, atau evaluasi pada domain data baru).
3. **Penyelarasan Konsistensi Inti:**
   `Judul → Identifikasi & Rumusan Masalah → Tujuan → Metodologi → Hasil & Pembahasan → Simpulan` wajib selalu sinkron.

---

## 2. Ketentuan Wajib Pencarian Literatur & Format Keluaran (PRIORITAS UTAMA)

Setiap kali melakukan pencarian atau penyusunan literatur untuk mendukung penulisan bab, **seluruh kriteria berikut WAJIB dipenuhi dan diutamakan**:

1. **Jumlah minimal:** Minimal **5 referensi** yang sangat relevan dengan judul penelitian (dalam Bahasa Inggris).
2. **Kualitas & indeksasi:** Jurnal ilmiah internasional terkemuka terindeks **Scopus Q1 atau Scopus Q2**.
3. **Bahasa referensi:** Berbahasa Inggris.
4. **Akses & status jurnal:** Bersifat **Open Access** dan **tidak *discontinued*** (masih aktif terindeks).
5. **Tahun terbit:** Terbit dalam **5 tahun terakhir (2021–2026)**.
6. **Dampak sitasi:** Memiliki jumlah sitasi tinggi, **minimal 5 sitasi** dari jurnal ilmiah yang relevan.
7. **Gaya sitasi:** Format **APA 7**, dengan kutipan dalam teks berbentuk `(Author et al., YEAR)`.
8. **Format keluaran literatur (WAJIB PERSIS):**
   - **Dilarang** menuliskan daftar artikel yang dipilih secara terpisah (*Do not write selected articles*).
   - Gabungkan seluruh pernyataan sitasi dalam **Bahasa Inggris** dari setiap referensi yang ditemukan menjadi **1 paragraf utuh sepanjang 150 kata** dalam format **APA 7**, diawali tepat dengan judul **`Citation:`**.
   - Cantumkan daftar pustaka lengkap beserta **DOI** resmi untuk seluruh referensi tersebut, diawali tepat dengan judul **`Bibliography:`**.

### Template Prompt Pencarian Literatur
Gunakan struktur kueri berikut saat melakukan penelusuran literatur ilmiah:

> `'[Pertanyaan pencarian literatur dalam Bahasa Inggris?]' that is highly relevant to the following research title: '[Judul penelitian dalam Bahasa Inggris]'. Find at least 5 references that meet the following criteria: leading international scientific journals indexed by Scopus Q1 or Scopus Q2, in English, with a high number of citations, open access, journals that are not discontinued, published in the last five years (2021-2026), with at least 5 citations from relevant scientific journals. Do not write selected articles. Write and combine all citations statement in English from each reference found, in a complete paragraph of 150 words in APA 7 format. At the beginning, write the title ("Citation:"). Write a complete list of references with doi. At the beginning, write the title ("Bibliography:").`

---

## 3. Alur Kerja 11 Tahapan Penulisan Karya Ilmiah

| No | Perintah | Masukan (*Input*) | Aturan Keluaran & Target Panjang |
| :-: | :--- | :--- | :--- |
| 1 | `/unggah-artikel` | Artikel ilmiah rujukan utama | Analisis fokus penelitian, masalah, metode, data/objek, temuan, keterbatasan, dan peluang riset lanjutan; rekomendasikan **5 topik** yang relevan dan realistis. |
| 2 | `/tentukan-topik` | Program Studi; Bidang Keahlian/Peminatan | Hasilkan **tepat 1 topik penelitian terbaik** yang relevan, memiliki masalah jelas, realistis, dan layak diteliti. |
| 3 | `/justifikasi-topik` | Judul / Topik penelitian | **Justifikasi topik maksimal 50 kata** dan **ringkasan maksimal ~250 kata** mencakup rumusan masalah, tujuan, manfaat, *novelty*/kebaruan, dan ruang lingkup. |
| 4 | `/tulis-outline` | Program Studi; Bidang Peminatan; Judul/Topik | Susun **outline sistematis Bab I–V** sesuai program studi, bidang peminatan, topik, dan metodologi yang tepat. |
| 5 | `/pertanyaan-literatur` | Outline karya ilmiah | Buat *literature search questions* dalam **Bahasa Inggris** untuk setiap subbab, sub-subbab, dan poin penting dalam outline (siap dipakai dengan ketentuan Bagian 2). |
| 6 | `/tulis-bab-1` | Prodi; Peminatan; Judul; Outline Bab I; Pernyataan sitasi (`Citation:`); Referensi (`Bibliography:`) | Tulis **BAB I Pendahuluan (~1.500 kata)** mengikuti outline, menggunakan referensi yang diberikan, kutipan `(Author et al., YEAR)`, serta menjaga kesinambungan masalah, tujuan, kontribusi, dan ruang lingkup. |
| 7 | `/tulis-bab-2` | Prodi; Peminatan; Judul; Outline Bab II; Pernyataan sitasi (`Citation:`); Referensi (`Bibliography:`) | Tulis **BAB II Tinjauan Pustaka (~2.500 kata)** membahas konsep, teori, perkembangan literatur, penelitian terdahulu, *gap* penelitian, dan hubungan literatur secara sintetis dan akademis. |
| 8 | `/tulis-bab-3` | Prodi; Peminatan; Judul; Outline Bab III; Pernyataan sitasi; Referensi metodologi | Tulis **BAB III Metodologi Penelitian (~2.500 kata)** secara operasional dan sistematis: keterkaitan rumusan masalah, tujuan, data, metode, eksperimen, pengujian, dan evaluasi. |
| 9 | `/tulis-bab-4` | Prodi; Peminatan; Judul; Outline Bab IV; Hasil eksperimen; Data/tabel/grafik; Referensi pembahasan | Tulis **BAB IV Hasil dan Pembahasan (~2.500 kata)** menyajikan hasil secara objektif, menginterpretasikan temuan, menjawab tujuan penelitian, serta membandingkannya dengan studi terdahulu. |
| 10 | `/tulis-bab-5` | Prodi; Peminatan; Judul; Outline Bab V; Rumusan Masalah; Tujuan; Temuan Utama; Interpretasi; Keterbatasan; Kontribusi | Tulis **BAB V Simpulan dan Saran (~750 kata)**. Simpulan menjawab tujuan dan *research question* serta kontribusi temuan; saran diarahkan pada tindak lanjut dan penelitian selanjutnya. |
| 11 | `/tulis-abstrak` | Judul; Latar Belakang; Tujuan; Metode; Hasil & Pembahasan; Simpulan & Saran | Tulis **abstrak ~250 kata dalam satu paragraf** (masalah, tujuan, metode, hasil utama, interpretasi, simpulan, dan implikasi) dilengkapi sekitar **5 kata kunci**. |
