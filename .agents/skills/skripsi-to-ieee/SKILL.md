---
name: skripsi-to-ieee
description: Use this skill when the user asks to "convert skripsi to IEEE", "buat jurnal IEEE dari skripsi", "format paper IEEE", "tulis artikel ilmiah IEEE", "ubah skripsi atau tesis jadi paper conference/journal IEEE", "write an IEEE paper", "IEEEtran LaTeX template", or needs guidance on condensing an academic thesis into a high-impact, two-column IEEE standard paper.
version: 1.0.0
---

# Skripsi to IEEE Journal & Conference Paper Skill

Panduan komprehensif untuk mengonversi dokumen Skripsi/Tesis/Disertasi (80–150+ halaman) menjadi artikel ilmiah standar **IEEE Conference (4–6 halaman)** atau **IEEE Transactions / Journal (6–10 halaman)** dengan format dua kolom, gaya penulisan akademis berbobot, dan struktur *state-of-the-art*.

---

## 1. Prinsip Utama: Kondensasi vs Copy-Paste

Mengubah skripsi menjadi paper IEEE **bukan sekadar merangkum**, melainkan **merestrukturisasi narasi**:
- **Skripsi** bertujuan membuktikan bahwa mahasiswa telah belajar, memahami teori dasar, dan menjalankan metodologi secara lengkap (banyak penjelasan tutorial, diagram alir dasar, dan tinjauan pustaka umum).
- **Paper IEEE** bertujuan menyampaikan **kontribusi ilmiah orisinal (novelty)** kepada komunitas peneliti internasional. Pembaca dianggap sudah menguasai konsep dasar.

### Aturan Eliminasi (Apa yang WAJIB Dibuang dari Skripsi):
1. **Penjelasan teori dasar buku teks**: Jangan jelaskan apa itu "PHP", "MySQL", "Kamera", "Arduino", atau definisi umum "Machine Learning". Langsung fokus pada arsitektur/model spesifik yang dipakai.
2. **Diagram umum/sistem sepele**: Hapus Use Case Diagram, Activity Diagram konvensional, struktur tabel basis data lengkap, dan antarmuka login/CRUD standar.
3. **Penyajian data mentah berulang**: Ganti tabel berlembar-lembar dengan grafik ringkas (line plot, bar chart, boxplot) atau tabel metrik kinerja teragregasi (Accuracy, Precision, Recall, F1-Score, Execution Time, PSNR/SSIM, dll).
4. **Kalimat pengantar bertele-tele**: Hapus kalimat seperti *"Berdasarkan latar belakang di atas maka peneliti bermaksud..."*. Ganti dengan *problem statement* dan *proposed contribution* yang lugas.

---

## 2. Pemetaan Bab Skripsi ke Format IEEE

Gunakan pemetaan sistematis berikut untuk mengekstrak inti penelitian:

| Bab Skripsi (Induk) | Bagian Paper IEEE | Fokus & Target Bobot Halaman |
| :--- | :--- | :--- |
| **Judul Skripsi** | **Paper Title** | Lebih padat, spesifik, hindari frasa *"Rancang Bangun"* / *"Implementasi Sistem"*. Fokus pada metode & hasil. |
| **Abstrak (Skripsi)** | **Abstract & Index Terms** | 150–250 kata: Konteks (1-2 kal.), Masalah (1 kal.), Solusi/Metode (1-2 kal.), Hasil Utama kuantitatif (1-2 kal.), Kesimpulan (1 kal.). 4–6 IEEE Keywords. |
| **Bab 1: Pendahuluan** | **I. INTRODUCTION** | ~15–20% panjang paper. Latar belakang masalah riil, gap penelitian, keterbatasan studi terdahulu, dan 3–4 poin kontribusi utama (*"The main contributions of this study are..."*). |
| **Bab 2: Tinjauan Pustaka** | **II. RELATED WORK** | Evaluasi kritis 5–15 paper mutakhir (3–5 tahun terakhir). Jangan hanya deskripsi, tapi bandingkan kelebihan & kekurangannya terhadap metode yang diusulkan. |
| **Bab 3: Metodologi** | **III. PROPOSED METHODOLOGY / SYSTEM ARCHITECTURE** | ~25–30% panjang paper. Formulasi matematis, blok diagram sistem, algoritma (pseudocode), tahapan *preprocessing*, model arsitektur, dan justifikasi parameter. |
| **Bab 4: Hasil & Pembahasan** | **IV. EXPERIMENTAL SETUP & RESULTS** (atau **IV. RESULTS AND DISCUSSION**) | ~35–40% panjang paper. Spesifikasi dataset/lingkungan uji, metrik evaluasi, komparasi dengan baseline/studi lain (*benchmarking*), visualisasi hasil, dan analisis *trade-off*. |
| **Bab 5: Kesimpulan & Saran** | **V. CONCLUSION** | 1–2 paragraf. Rangkuman capaian inti, validasi hipotesis, keterbatasan studi, dan arah penelitian lanjutan (*future work*). Hapus saran administratif non-teknis. |
| **Daftar Pustaka** | **REFERENCES** | 15–30 referensi primer (80% jurnal/konferensi bereputasi 5 tahun terakhir, format sitasi numerik IEEE `[1]`). |

---

## 3. Struktur Standar Dokumen IEEE

### 3.1 Judul (Title)
- Huruf kapital awal kata (*Title Case*), hindari akronim yang tidak umum.
- **Hindari**: *"Rancang Bangun Aplikasi Deteksi Penyakit Daun Padi Menggunakan Metode Convolutional Neural Network Berbasis Android"*
- **Rekomendasi IEEE**: *"Optimized Convolutional Neural Network for Real-Time Rice Leaf Disease Classification on Mobile Devices"*

### 3.2 Penulis & Afiliasi (Author Block)
Format IEEE Conference biasanya menggunakan multi-kolom horizontal untuk afiliasi:
```text
First A. Author*, Second B. Author†, and Third C. Supervisor*
*Department of Electrical Engineering and Information Technology, Universitas Gadjah Mada, Yogyakarta, Indonesia
†Department of Computer Science, Institut Teknologi Bandung, Bandung, Indonesia
Email: author1@mail.ugm.ac.id, author2@itb.ac.id, supervisor@ugm.ac.id
```

### 3.3 Abstract & Keywords
- Abstrak tidak boleh mengandung sitasi (`[1]`), akronim tanpa kepanjangan, atau persamaan matematis bernomor.
- *Index Terms / Keywords*: Urutkan secara alfabetis, pisahkan dengan koma. Pilih kata kunci dari taksonomi IEEE (misal: *Deep learning, Image classification, Precision agriculture, Mobile applications*).

### 3.4 Section Headings (Gaya Huruf Romawi)
- **Primary Headings**: Huruf Romawi kapital, tengah, *Small Caps* (misal: `I. INTRODUCTION`, `II. RELATED WORK`).
- **Secondary Headings**: Huruf kapital alfabet, miring, rata kiri (misal: `A. Data Preprocessing`, `B. Model Architecture`).
- **Tertiary Headings**: Angka arab, miring, indentasi, diikuti tanda titik dua (misal: `1) Hyperparameter Tuning:`).

---

## 4. Panduan Bahasa & Academic Tone

IEEE Paper umumnya disyaratkan dalam bahasa Inggris akademis formal (*formal scholarly English*).

### Kaidah Tenses:
1. **Present Tense**: Digunakan untuk fakta umum, kebenaran ilmiah yang mapan, dan pembahasan figur/tabel di naskah (*"Fig. 2 shows that...", "The algorithm converges when..."*).
2. **Past Tense**: Digunakan saat menjelaskan prosedur eksperimen yang telah dilakukan dan hasil spesifik yang diperoleh (*"We trained the network for 100 epochs", "The model achieved an accuracy of 96.4%"*).
3. **Present Perfect Tense**: Digunakan saat membahas literatur terdahulu yang relevan hingga saat ini (*"Recent studies have demonstrated...", "Several authors have proposed..."*).

### Transformasi Kosakata (Indonesian Skripsi $\rightarrow$ Academic English):
- *"Penulis membuat aplikasi ini untuk mempermudah..."* $\rightarrow$ *"This work proposes a framework to enhance..."*
- *"Dapat dilihat pada tabel di bawah..."* $\rightarrow$ *"As presented in Table I, ..."*
- *"Hasilnya sangat bagus sekali..."* $\rightarrow$ *"The experimental results demonstrate a substantial improvement (14.2% margin)..."*
- *"Penelitian ini belum sempurna dan masih banyak kekurangan..."* $\rightarrow$ *"While the proposed method achieves competitive accuracy, its inference latency poses constraints on ultra-low-power edge nodes."*

---

## 5. Standar Format Elemen Teknis (Persamaan, Gambar, Tabel)

### 5.1 Persamaan Matematika (Equations)
- Beri nomor urut persamaan di sisi kanan kolom dengan tanda kurung: `(1)`.
- Semua variabel harus didefinisikan tepat setelah persamaan muncul.
- Persamaan adalah bagian dari kalimat; gunakan koma atau titik di akhir persamaan jika diperlukan.
- Dalam teks, rujuk dengan `"Eq. (1)"` di awal kalimat atau `"(1)"` di tengah kalimat.

Contoh LaTeX:
```latex
The objective loss function is defined as:
\begin{equation}
\mathcal{L}(\theta) = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right] + \lambda \|\theta\|_2^2,
\label{eq:loss}
\end{equation}
where $N$ denotes the batch size, $\hat{y}_i$ is the predicted probability, and $\lambda$ represents the regularization coefficient.
```

### 5.2 Gambar (Figures)
- Gambar wajib tajam (resolusi minimal 300 DPI, format vektor EPS/PDF diutamakan, atau PNG beresolusi tinggi).
- **Caption Gambar**: Diletakkan **di bawah gambar**, berformat `"Fig. 1. Description of the system architecture."` (Perhatikan: `"Fig. 1."` disingkat, bukan `"Figure 1"`).
- Lebar gambar disesuaikan:
  - 1 kolom: $\approx 3.5$ inci ($8.8$ cm). Gunakan `\begin{figure}` di LaTeX.
  - 2 kolom (span kedua kolom): $\approx 7.0$ inci ($18.1$ cm). Gunakan `\begin{figure*}` di LaTeX.
- Pastikan semua label, sumbu ($x$-axis, $y$-axis), dan *legend* terbaca dengan ukuran font sebanding teks naskah (~8pt).

### 5.3 Tabel (Tables)
- **Caption Tabel**: Diletakkan **di atas tabel**, berpusat, dengan nomor romawi kapital: `"TABLE I"`, baris berikutnya berisi judul tabel dalam *Small Caps* atau Huruf Kapital: `"PERFORMANCE COMPARISON OF DIFFERENT MODELS"`.
- Desain minimalis: Gunakan garis horizontal tebal di atas & bawah (`\toprule`, `\bottomrule`), garis tipis pemisah header (`\midrule`), dan **hindari garis vertikal**.

---

## 6. Referensi & Sitasi (Gaya IEEE)

- Sitasi di dalam teks menggunakan nomor kurung siku di dalam baris teks, misalnya: `"...as demonstrated by Zhang et al. [3]"` atau `"...in previous works [1], [4]--[6]."`.
- Jangan menuliskan *"in reference [5]"*, cukup tuliskan *"in [5]"*.
- Di akhir naskah, urutkan referensi sesuai urutan kemunculan sitasi pertama kali (bukan menurut abjad).

Format Standar BibTeX:
```bibtex
@article{vaswani2017attention,
  author    = {A. Vaswani and N. Shazeer and N. Parmar and J. Uszkoreit and L. Jones and A. N. Gomez and L. Kaiser and I. Polosukhin},
  title     = {Attention is All You Need},
  journal   = {Advances in Neural Information Processing Systems},
  volume    = {30},
  pages     = {5998--6008},
  year      = {2017}
}

@inproceedings{he2016deep,
  author    = {K. He and X. Zhang and S. Ren and J. Sun},
  title     = {Deep Residual Learning for Image Recognition},
  booktitle = {Proc. IEEE Conf. Computer Vision and Pattern Recognition (CVPR)},
  pages     = {770--778},
  year      = {2016}
}
```

---

## 7. Checklist Verifikasi Sebelum Submit (Anti-Desk Rejection)

Sebelum mengunggah manuskrip ke portal konferensi/jurnal (EDAS, IEEE Author Portal, EasyChair, dll.):
- [ ] **Batas Halaman**: Sudah sesuai toleransi (misal: tepat 6 halaman, atau tidak melebihi halaman maksimal tanpa *overlength page charges*).
- [ ] **Tidak Ada Halaman Menggantung**: Halaman terakhir harus seimbang kedua kolomnya (`\balance` atau `\IEEEtriggeratref`). Jangan tinggalkan hanya 2-3 baris di halaman baru.
- [ ] **Metadata Penulis Lengkap**: Nama, afiliasi resmi institusi, kota, negara, dan email aktif.
- [ ] **Novelty & Contribution Jelas**: Minimal terdapat 3 kontribusi eksplisit di paragraf terakhir *Introduction*.
- [ ] **Visual Clarity**: Semua teks dalam grafik/diagram dapat dibaca tanpa harus zoom > 150%.
- [ ] **Kualitas Referensi**: Minimal 70% referensi berasal dari jurnal bereputasi atau prosiding konferensi internasional 5 tahun terakhir dengan DOI lengkap.
- [ ] **Kepatuhan Template**: Menggunakan template resmi `IEEEtran.cls` (LaTeX) atau template `.docx` IEEE resmi versi terbaru.

---

## 8. Template & Resource Tambahan

Skill ini menyediakan berkas siap pakai:
- [IEEE LaTeX Template (resources/ieee_template.tex)](./resources/ieee_template.tex)
- [Contoh Berkas BibTeX (resources/references.bib)](./resources/references.bib)
- [Panduan Detail Format & Troubleshooting (references/ieee-formatting-rules.md)](./references/ieee-formatting-rules.md)
