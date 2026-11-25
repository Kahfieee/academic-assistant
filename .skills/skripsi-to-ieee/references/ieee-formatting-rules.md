# IEEE Formatting Rules & Thesis Conversion Guidelines

Dokumen rujukan teknis mendalam untuk standardisasi format IEEE dan konversi naskah skripsi/tesis.

---

## 1. Spesifikasi Tipografi & Layout IEEE (Two-Column)

Standar IEEE (A4 / US Letter):
- **Kertas**: A4 (210 mm x 297 mm) atau US Letter (8.5 in x 11 in). Di Indonesia dan Asia/Eropa, gunakan format A4 kecuali jika CFP (Call for Papers) mensyaratkan Letter.
- **Margin A4**:
  - Top: 19 mm (0.75 in)
  - Bottom: 43 mm (1.69 in) / 25 mm pada naskah draft
  - Left / Inside: 13 mm (0.51 in)
  - Right / Outside: 13 mm (0.51 in)
- **Kolom**:
  - Jumlah: 2 kolom (kecuali Judul, Pengarang, dan Abstrak yang membentang 1 kolom lebar).
  - Lebar Kolom: 88 mm (3.46 in).
  - Spasi Antar Kolom (*Column Gutter*): 4.6 mm (0.18 in).
- **Hirarki Ukuran Font (Times New Roman / Nimbus Roman)**:
  - Title: 24 pt, Regular, Centered.
  - Author Names: 10 pt, Regular, Centered.
  - Author Affiliations: 9 pt, Italic, Centered.
  - Section Headings: 10 pt, Small Caps, Centered (Numerasi Romawi: I, II, III).
  - Subsection Headings: 10 pt, Italic, Left-aligned (Numerasi Alfabet: A, B, C).
  - Sub-subsection Headings: 10 pt, Italic, Indented (Numerasi Arab: 1), 2)).
  - Body Text: 10 pt, Justified, Single-spaced, Indentasi paragraf awal 3.5 mm (0.14 in).
  - Table Caption & Content: 8 pt.
  - Figure Caption: 8 pt.
  - References: 8 pt, Justified.

---

## 2. Kesalahan Terjemahan Umum (Indonesian Thesis $\rightarrow$ Academic English)

Ketika menerjemahkan draft skripsi ke bahasa Inggris untuk IEEE:

| Frasa Skripsi / Terjemahan Mentah | Masalah | Rekomendasi Standar IEEE |
| :--- | :--- | :--- |
| *"In this paper, we will discuss about..."* | Gramatikal & informal (*discuss* tidak butuh *about*). | *"This paper presents..."* atau *"This study investigates..."* |
| *"As we know, IoT is very popular nowadays."* | Klise, tidak ilmiah, subjektif. | *"Internet of Things (IoT) systems have seen widespread deployment in recent years [1]."* |
| *"Peneliti melakukan pengujian sebanyak 10 kali..."* $\rightarrow$ *"Researcher conducted tests 10 times..."* | Menggunakan kata ganti orang ketiga janggal. | *"The experiment was repeated across 10 independent trials..."* |
| *"The accuracy is very good and satisfying."* | Emosional / non-kuantitatif. | *"The proposed model attained a 94.8% classification accuracy, surpassing baseline CNNs by 4.2%."* |
| *"Based on Table 4, it shows that..."* | *Dangling modifier* / redundan. | *"As presented in Table IV, ..."* atau *"Table IV outlines..."* |
| *"In order to..."* (di setiap kalimat) | *Wordy* / pemborosan kata. | Cukup gunakan *"To..."*. |

---

## 3. Penanganan Gambar & Grafik

### Aturan Resolusi & Format:
1. **Diagram Alir / Skema Arsitektur**:
   - Jangan gunakan screenshot antarmuka atau screenshot drawing tool berkualitas rendah.
   - Ekspor dalam format vektor: **PDF**, **EPS**, atau **SVG** (lalu convert ke PDF).
   - Di LaTeX gunakan `\includegraphics[width=\linewidth]{filename.pdf}`.
2. **Grafik Metrik Kinerja (Loss curve, Accuracy, Confusion Matrix)**:
   - Buat menggunakan Python (Matplotlib / Seaborn) dengan DPI minimal 300:
     ```python
     import matplotlib.pyplot as plt
     plt.rcParams.update({'font.size': 8, 'font.family': 'serif'})
     fig, ax = plt.subplots(figsize=(3.5, 2.5)) # Ukuran pas 1 kolom IEEE
     # plot data...
     plt.tight_layout()
     plt.savefig('result.pdf', dpi=300, bbox_inches='tight')
     ```
3. **Ukuran Huruf dalam Gambar**:
   - Teks di dalam gambar (sumbu X, Y, angka legenda) harus sebanding ukurannya dengan body text (sekitar 7–8 pt) saat gambar dicetak/diskalakan ke lebar kolom.

---

## 4. Persyaratan IEEE PDF eXpress

Sebagian besar konferensi IEEE mewajibkan naskah divalidasi melalui sistem **IEEE PDF eXpress**:
- **Font Embedding**: Semua font (termasuk font standar seperti Times New Roman, Helvetica, Symbol) **WAJIB di-embed** 100%. Tidak boleh ada *Type 3 fonts*.
  - Di LaTeX: `pdflatex` modern secara default meng-embed font Type 1.
  - Di MS Word: Pilih *Options $\rightarrow$ Save $\rightarrow$ Embed fonts in the file*.
- **Bookmark & Links**: Jangan menyertakan formulir interaktif atau JavaScript di dalam PDF.
- **Ukuran File**: Biasanya dibatasi maksimal 10 MB - 20 MB.
