const fs = require('fs');
const path = require('path');

let docxPkg;
try {
  docxPkg = require('docx');
} catch {
  docxPkg = require(path.join(__dirname, '..', '..', 'docx_builder', 'node_modules', 'docx'));
}

const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, BorderStyle, Header, Footer,
  PageNumber, NumberFormat, PageBreak, ShadingType, ImageRun
} = docxPkg;

const ROOT_DIR = path.resolve(__dirname, '..');
const DOCX_PATH = path.join(ROOT_DIR, 'templates', 'formal_thesis_template.docx');
const LOGO_PATH = path.join(ROOT_DIR, 'assets', 'university_logo_placeholder.png');

const MARGINS = {
  top: 2268,    // 4 cm
  left: 2268,   // 4 cm
  bottom: 1701, // 3 cm
  right: 1701   // 3 cm
};

function titlePara(text, size = 28, bold = true, spacingAfter = 200, alignment = AlignmentType.CENTER) {
  return new Paragraph({
    alignment,
    spacing: { after: spacingAfter, before: 100, line: 280 },
    children: [new TextRun({ text, bold, size, font: "Times New Roman" })]
  });
}

function chapTitle(chapNum, chapName) {
  return [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 240, after: 80, line: 280 },
      heading: HeadingLevel.HEADING_1,
      children: [new TextRun({ text: chapNum, bold: true, size: 28, font: "Times New Roman" })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 80, after: 320, line: 280 },
      heading: HeadingLevel.HEADING_1,
      children: [new TextRun({ text: chapName, bold: true, size: 28, font: "Times New Roman" })]
    })
  ];
}

function subHeading(text) {
  return new Paragraph({
    alignment: AlignmentType.LEFT,
    spacing: { before: 240, after: 120, line: 360 },
    heading: HeadingLevel.HEADING_2,
    children: [new TextRun({ text, bold: true, size: 24, font: "Times New Roman" })]
  });
}

function bodyPara(text, indent = true) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    indent: indent ? { firstLine: 567 } : undefined,
    spacing: { before: 60, after: 120, line: 360 },
    children: [new TextRun({ text, size: 24, font: "Times New Roman" })]
  });
}

function bodyParaWithBold(boldPrefix, text, indent = true) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    indent: indent ? { firstLine: 567 } : undefined,
    spacing: { before: 60, after: 120, line: 360 },
    children: [
      new TextRun({ text: boldPrefix, bold: true, size: 24, font: "Times New Roman" }),
      new TextRun({ text, size: 24, font: "Times New Roman" })
    ]
  });
}

function listItem(prefix, boldLabel, text) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    indent: { left: 567, hanging: 360 },
    spacing: { before: 40, after: 80, line: 360 },
    children: [
      new TextRun({ text: prefix + " ", bold: true, size: 24, font: "Times New Roman" }),
      ...(boldLabel ? [new TextRun({ text: boldLabel + " ", bold: true, size: 24, font: "Times New Roman" })] : []),
      new TextRun({ text, size: 24, font: "Times New Roman" })
    ]
  });
}

function captionPara(text) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 160, after: 100, line: 240 },
    children: [new TextRun({ text, bold: true, size: 22, font: "Times New Roman" })]
  });
}

function createStyledTable(headers, rows, colWidths) {
  const tableRows = [
    new TableRow({
      tableHeader: true,
      children: headers.map((h, i) => new TableCell({
        width: colWidths ? { size: colWidths[i], type: WidthType.DXA } : undefined,
        shading: { type: ShadingType.CLEAR, fill: "F1F5F9" },
        margins: { top: 100, bottom: 100, left: 140, right: 140 },
        children: [
          new Paragraph({
            alignment: AlignmentType.CENTER,
            spacing: { line: 240 },
            children: [new TextRun({ text: h, bold: true, size: 20, font: "Times New Roman" })]
          })
        ]
      }))
    }),
    ...rows.map((row) => new TableRow({
      children: row.map((cellText, i) => new TableCell({
        width: colWidths ? { size: colWidths[i], type: WidthType.DXA } : undefined,
        margins: { top: 90, bottom: 90, left: 140, right: 140 },
        children: [
          new Paragraph({
            alignment: AlignmentType.LEFT,
            spacing: { line: 240 },
            children: [new TextRun({ text: cellText, size: 20, font: "Times New Roman" })]
          })
        ]
      }))
    }))
  ];

  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 8, color: "000000" },
      bottom: { style: BorderStyle.SINGLE, size: 8, color: "000000" },
      left: { style: BorderStyle.NONE },
      right: { style: BorderStyle.NONE },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC" },
      insideVertical: { style: BorderStyle.NONE }
    },
    rows: tableRows
  });
}

const frontChildren = [
  // HALAMAN SAMPUL
  titlePara("[JUDUL PENELITIAN / KARYA ILMIAH DISINI]", 28, true, 240),
  titlePara("SKRIPSI / TUGAS AKHIR", 26, true, 300),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 120, after: 240, line: 320 },
    children: [new TextRun({ text: "Diajukan untuk Memenuhi Sebagian Persyaratan Akademik\nMeraih Gelar [Nama Gelar Akademik Disini] pada Program Studi [Nama Program Studi Disini]", size: 22, font: "Times New Roman" })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 240, after: 240 },
    children: [
      new ImageRun({
        data: fs.readFileSync(LOGO_PATH),
        transformation: { width: 140, height: 140 }
      })
    ]
  }),
  titlePara("Disusun Oleh:", 24, false, 80),
  titlePara("[Nama Penulis Disini]", 24, true, 60),
  titlePara("NIM / ID: [Nomor Induk Disini]", 24, true, 500),
  titlePara("PROGRAM STUDI [NAMA PROGRAM STUDI DISINI]", 24, true, 60),
  titlePara("FAKULTAS [NAMA FAKULTAS DISINI]", 24, true, 60),
  titlePara("[NAMA UNIVERSITAS / INSTITUSI DISINI]", 24, true, 60),
  titlePara("[Tahun Disini]", 24, true, 120),

  // LEMBAR PENGESAHAN
  new Paragraph({ children: [new PageBreak()] }),
  titlePara("LEMBAR PENGESAHAN", 26, true, 180),
  bodyPara("Judul Karya Ilmiah : [JUDUL PENELITIAN / KARYA ILMIAH DISINI]", false),
  bodyPara("Nama Mahasiswa : [Nama Penulis Disini]", false),
  bodyPara("Nomor Induk (NIM) : [Nomor Induk Disini]", false),
  bodyPara("Program Studi : [Nama Program Studi Disini]", false),
  bodyPara("Bidang Konsentrasi : [Bidang Kajian / Peminatan Disini]", false),
  bodyPara("Karya ilmiah ini telah disetujui, dipertahankan di hadapan Dewan Penguji pada Program Studi [Nama Program Studi Disini], [Nama Universitas / Institusi Disini] pada tanggal [Tanggal Sidang Disini], dan dinyatakan LULUS.", false),
  captionPara("Komisi Pembimbing:"),
  createStyledTable(
    ["Pembimbing Utama", "Pembimbing Pendamping"],
    [["\n\n\n[Nama Pembimbing Utama Disini]\nNIDN / NIP: [Nomor Identitas Disini]", "\n\n\n[Nama Pembimbing Pendamping Disini]\nNIDN / NIP: [Nomor Identitas Disini]"]],
    [5000, 5000]
  ),
  captionPara("Dewan Penguji:"),
  createStyledTable(
    ["Ketua Penguji", "Anggota Penguji"],
    [["\n\n\n[Nama Ketua Penguji Disini]\nNIDN / NIP: [Nomor Identitas Disini]", "\n\n\n[Nama Anggota Penguji Disini]\nNIDN / NIP: [Nomor Identitas Disini]"]],
    [5000, 5000]
  ),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 160, after: 40 },
    children: [new TextRun({ text: "Mengetahui,\nKetua Program Studi [Nama Program Studi Disini]\n\n\n\n[Nama Ketua Program Studi Disini]\nNIDN / NIP: [Nomor Identitas Disini]", bold: true, size: 20, font: "Times New Roman" })]
  }),

  // PERNYATAAN KEASLIAN
  new Paragraph({ children: [new PageBreak()] }),
  titlePara("PERNYATAAN KEASLIAN KARYA ILMIAH", 28, true, 240),
  bodyPara("Saya yang bertanda tangan di bawah ini:", false),
  bodyPara("Nama : [Nama Penulis Disini]", false),
  bodyPara("Nomor Induk (NIM) : [Nomor Induk Disini]", false),
  bodyPara("Program Studi : [Nama Program Studi Disini]", false),
  bodyPara("Perguruan Tinggi : [Nama Universitas / Institusi Disini]", false),
  bodyPara("Menyatakan dengan sesungguhnya bahwa karya ilmiah yang berjudul \"[JUDUL PENELITIAN / KARYA ILMIAH DISINI]\" adalah benar-benar merupakan karya ilmiah asli saya sendiri di bawah arahan komisi pembimbing, bukan hasil jiplakan, saduran, atau fabrikasi data dari karya orang lain, baik sebagian maupun seluruhnya. Seluruh rujukan, kepustakaan, dan kutipan telah dicantumkan secara sah sesuai kaidah integritas akademik dan etika sitasi ilmiah yang berlaku."),
  bodyPara("Apabila di kemudian hari terbukti bahwa karya ilmiah ini mengandung unsur plagiarisme, manipulasi data, atau pelanggaran etika akademik lainnya, saya bersedia menerima sanksi akademik sesuai peraturan perundang-undangan yang berlaku, termasuk pembatalan kelulusan dan pencabutan gelar akademik yang diperoleh."),
  new Paragraph({
    alignment: AlignmentType.RIGHT,
    spacing: { before: 200, after: 100 },
    children: [new TextRun({ text: "[Kota Disini], [Tanggal Disini]\nYang menyatakan,\n\n[ Materai Resmi ]\n\n\n[Nama Penulis Disini]\nNIM / ID: [Nomor Induk Disini]", bold: true, size: 22, font: "Times New Roman" })]
  }),

  // KATA PENGANTAR
  new Paragraph({ children: [new PageBreak()] }),
  titlePara("KATA PENGANTAR", 28, true, 240),
  bodyPara("Puji syukur kehadirat Tuhan Yang Maha Esa atas segala rahmat dan karunia-Nya sehingga penulis dapat menyelesaikan naskah karya ilmiah yang berjudul \"[Judul Penelitian / Karya Ilmiah Disini]\" dengan baik. Naskah ini disusun sebagai salah satu syarat akademik untuk memperoleh gelar [Nama Gelar Akademik Disini] pada Program Studi [Nama Program Studi Disini], [Nama Universitas / Institusi Disini]."),
  bodyPara("Dalam proses penelitian hingga penyelesaian naskah ini, penulis menyampaikan terima kasih dan penghargaan yang sebesar-besarnya kepada:"),
  listItem("1.", "[Nama Rektor / Ketua Institusi Disini],", "selaku Pimpinan [Nama Universitas / Institusi Disini]."),
  listItem("2.", "[Nama Dekan / Ketua Program Studi Disini],", "selaku Ketua Program Studi [Nama Program Studi Disini]."),
  listItem("3.", "[Nama Pembimbing Utama Disini],", "selaku Dosen Pembimbing Utama atas arahan metodologis dan ketelitian bimbingan."),
  listItem("4.", "[Nama Pembimbing Pendamping Disini],", "selaku Dosen Pembimbing Pendamping atas bimbingan teknis dan penyempurnaan penulisan."),
  listItem("5.", "Seluruh Dosen dan Staf Akademik [Nama Universitas / Institusi Disini],", "atas ilmu pengetahuan selama masa studi."),
  listItem("6.", "Orang Tua, Keluarga, dan Rekan Seperjuangan,", "atas doa, dukungan moral, dan diskusi konstruktif."),
  bodyPara("Penulis menyadari bahwa karya ilmiah ini masih terbuka terhadap saran konstruktif demi penyempurnaan di masa mendatang. Semoga hasil penelitian ini bermanfaat bagi perkembangan ilmu pengetahuan."),
  new Paragraph({
    alignment: AlignmentType.RIGHT,
    spacing: { before: 160, after: 80 },
    children: [new TextRun({ text: "[Kota Disini], [Tanggal Disini]\nPenulis,\n\n\n[Nama Penulis Disini]\nNIM / ID: [Nomor Induk Disini]", bold: true, size: 22, font: "Times New Roman" })]
  }),

  // ABSTRAK ID & EN
  new Paragraph({ children: [new PageBreak()] }),
  titlePara("ABSTRAK", 28, true, 200),
  titlePara("[NAMA PENULIS DISINI]. [Nomor Induk Disini]. [Judul Penelitian / Karya Ilmiah Disini].", 22, true, 200),
  bodyParaWithBold("[Latar Belakang & Masalah (~15–20%):] ", "Jelaskan konteks permasalahan nyata, kesenjangan penelitian terdahulu (research gap), dan urgensi solusi yang diusulkan."),
  bodyParaWithBold("[Metodologi & Desain Eksperimen (~20–30%):] ", "Uraikan karakteristik dataset atau objek penelitian, tahapan pra-pemrosesan/perancangan sistem, metode utama, dan skema evaluasi terukur."),
  bodyParaWithBold("[Hasil Kuantitatif & Simpulan (~50%):] ", "Sajikan metrik kinerja utama, hasil uji signifikansi statistik, perbandingan terhadap metode pembanding, serta simpulan ringkas kontribusi ilmiah."),
  bodyParaWithBold("Kata Kunci: ", "[Kata Kunci 1], [Kata Kunci 2], [Kata Kunci 3], [Kata Kunci 4], [Kata Kunci 5].", false),

  new Paragraph({ children: [new PageBreak()] }),
  titlePara("ABSTRACT", 28, true, 200),
  titlePara("[AUTHOR NAME]. [Student ID]. [English Title of Research / Thesis].", 22, true, 200),
  bodyParaWithBold("[Background & Problem Statement (~15–20%):] ", "Describe the research context, literature limitations, and primary objective of the proposed work."),
  bodyParaWithBold("[Methodology & Experimental Protocol (~20–30%):] ", "Detail the dataset or system design, preprocessing steps, proposed methodology, and validation protocol."),
  bodyParaWithBold("[Key Findings & Conclusion (~50%):] ", "Report quantitative metrics, baseline comparisons, statistical significance verification, and core contributions."),
  bodyParaWithBold("Keywords: ", "[Keyword 1], [Keyword 2], [Keyword 3], [Keyword 4], [Keyword 5].", false),

  // DAFTAR ISI / TABEL / GAMBAR (Placeholder Word TOC)
  new Paragraph({ children: [new PageBreak()] }),
  titlePara("DAFTAR ISI", 28, true, 240),
  bodyPara("[Gunakan fitur Automatic Table of Contents di Microsoft Word (References → Table of Contents) agar nomor halaman terbarui otomatis mengikuti Heading 1 dan Heading 2 pada dokumen ini.]", false),

  new Paragraph({ children: [new PageBreak()] }),
  titlePara("DAFTAR TABEL", 28, true, 240),
  bodyPara("Tabel 2.1 Matriks Perbandingan Penelitian Terdahulu ...................................................... [hal]", false),
  bodyPara("Tabel 3.1 Operasionalisasi Variabel / Parameter Penelitian ......................................... [hal]", false),
  bodyPara("Tabel 4.1 Rekapitulasi Perbandingan Kinerja Antar Skenario Uji ................................. [hal]", false),

  new Paragraph({ children: [new PageBreak()] }),
  titlePara("DAFTAR GAMBAR", 28, true, 240),
  bodyPara("Gambar 3.1 Diagram Alir Tahapan Metodologi Penelitian ........................................... [hal]", false),
  bodyPara("Gambar 4.1 Visualisasi Grafik Hasil Evaluasi Penelitian ............................................. [hal]", false)
];

const mainChildren = [
  ...chapTitle("BAB I", "PENDAHULUAN"),
  subHeading("1.1 Latar Belakang Masalah"),
  bodyPara("Latar belakang disusun secara deduktif (alur piramida terbalik) yang mengantarkan pembaca dari konteks makro menuju permasalahan spesifik yang diteliti. Setiap klaim empiris wajib didukung referensi primer bereputasi."),
  subHeading("1.2 Identifikasi Masalah"),
  listItem("1.", "", "[Identifikasi kendala atau kesenjangan empiris pertama pada objek penelitian.]"),
  listItem("2.", "", "[Identifikasi keterbatasan metodologis pada studi terdahulu.]"),
  subHeading("1.3 Batasan Masalah"),
  listItem("1.", "", "[Batasan cakupan data, sampel, parameter metode, dan metrik evaluasi yang ditetapkan.]"),
  subHeading("1.4 Rumusan Masalah"),
  listItem("1.", "", "Bagaimana merancang dan mengimplementasikan [metode/sistem usulan] untuk menyelesaikan [permasalahan inti]?"),
  listItem("2.", "", "Bagaimana kinerja dan signifikansi peningkatan [metode/sistem usulan] dibandingkan pendekatan pembanding?"),
  subHeading("1.5 Tujuan Penelitian"),
  listItem("1.", "", "Merancang, mengimplementasikan, dan menguji [metode/sistem usulan] pada domain studi."),
  listItem("2.", "", "Mengukur secara kuantitatif kinerja serta validitas ilmiah hasil penelitian."),
  subHeading("1.6 Manfaat Penelitian"),
  listItem("1.", "Manfaat Teoritis:", "Memberikan kontribusi empiris bagi pengembangan literatur di bidang terkait."),
  listItem("2.", "Manfaat Praktis:", "Menghasilkan solusi teruji yang dapat diaplikasikan secara efektif."),

  new Paragraph({ children: [new PageBreak()] }),
  ...chapTitle("BAB II", "TINJAUAN PUSTAKA DAN LANDASAN TEORI"),
  subHeading("2.1 Tinjauan Pustaka (Penelitian Terdahulu)"),
  bodyPara("Bagian ini mensintesis secara kritis penelitian terdahulu yang relevan untuk memetakan celah penelitian (research gap) yang menjadi dasar kebaruan studi."),
  captionPara("Tabel 2.1 Matriks Perbandingan Penelitian Terdahulu"),
  createStyledTable(
    ["Peneliti (Tahun)", "Metode / Pendekatan", "Objek / Dataset", "Temuan & Celah Penelitian"],
    [
      ["[Penulis A (Tahun)]", "[Metode Studi 1]", "[Karakteristik Data]", "[Hasil dan keterbatasan]"],
      ["[Penulis B (Tahun)]", "[Metode Studi 2]", "[Karakteristik Data]", "[Hasil dan keterbatasan]"],
      ["Penelitian Ini", "[Pendekatan Usulan]", "[Ruang Lingkup Studi]", "[Kebaruan terukur yang ditawarkan]"]
    ],
    [1800, 2400, 2400, 3400]
  ),
  subHeading("2.2 Landasan Teori"),
  bodyPara("Uraikan teori formal, formulasi matematis, arsitektur konseptual, algoritma/metode inti, serta definisi metrik evaluasi yang menjadi pijakan ilmiah."),
  subHeading("2.3 Kerangka Pemikiran dan Hipotesis"),
  bodyPara("Gambarkan keterkaitan antara permasalahan, teori, metode usulan, dan hipotesis penelitian (H0 dan H1 bila bersifat eksperimental komparatif)."),

  new Paragraph({ children: [new PageBreak()] }),
  ...chapTitle("BAB III", "METODOLOGI PENELITIAN"),
  subHeading("3.1 Kerangka Kerja Penelitian"),
  bodyPara("Jelaskan tahapan sistematis pelaksanaan penelitian mulai dari pengumpulan data hingga evaluasi akhir."),
  subHeading("3.2 Pengumpulan dan Karakteristik Data"),
  bodyPara("Paparkan sumber data/objek, periode pengambilan, jumlah sampel, distribusi kategori, serta prosedur verifikasi kualitas data."),
  subHeading("3.3 Tahapan Pra-pemrosesan dan Perancangan"),
  bodyPara("Jabarkan prosedur pembersihan data, normalisasi, dan rancangan arsitektur sistem agar eksperimen dapat direplikasi sepenuhnya."),
  captionPara("Tabel 3.1 Operasionalisasi Variabel / Parameter Penelitian"),
  createStyledTable(
    ["Kode / Variabel", "Definisi Operasional", "Tipe / Skala", "Keterangan"],
    [
      ["[Variabel / Fitur 1]", "[Penjelasan rumus/pengukuran]", "[Tipe]", "[Peran dalam model]"],
      ["[Variabel / Fitur 2]", "[Penjelasan rumus/pengukuran]", "[Tipe]", "[Peran dalam model]"]
    ],
    [2200, 3800, 2000, 2000]
  ),
  subHeading("3.4 Arsitektur dan Konfigurasi Pengujian"),
  bodyPara("Jelaskan protokol pembagian data yang bebas kebocoran informasi (data leakage), penyetelan parameter, serta skenario pembanding (baseline)."),
  subHeading("3.5 Metrik Evaluasi dan Uji Signifikansi"),
  bodyPara("Tetapkan metrik kuantitatif serta uji signifikansi statistik untuk memvalidasi perbedaan performa antar skenario."),

  new Paragraph({ children: [new PageBreak()] }),
  ...chapTitle("BAB IV", "HASIL DAN PEMBAHASAN"),
  subHeading("4.1 Gambaran Umum Hasil Implementasi"),
  bodyPara("Sajikan statistik deskriptif data serta spesifikasi lingkungan perangkat keras/lunak pengujian."),
  subHeading("4.2 Hasil Evaluasi Kinerja dan Perbandingan"),
  bodyPara("Tampilkan hasil kuantitatif pendekatan yang diusulkan dan bandingkan secara langsung terhadap skenario pembanding pada data uji yang identik."),
  captionPara("Tabel 4.1 Rekapitulasi Perbandingan Kinerja Antar Skenario Uji"),
  createStyledTable(
    ["Skenario / Pendekatan", "Metrik 1", "Metrik 2", "Metrik 3", "Efisiensi Waktu"],
    [
      ["[Skenario Pembanding 1]", "[Nilai]", "[Nilai]", "[Nilai]", "[Durasi]"],
      ["[Skenario Pembanding 2]", "[Nilai]", "[Nilai]", "[Nilai]", "[Durasi]"],
      ["[Pendekatan Usulan]", "[Nilai]", "[Nilai]", "[Nilai]", "[Durasi]"]
    ],
    [3400, 1600, 1600, 1600, 1800]
  ),
  subHeading("4.3 Validasi Statistik dan Analisis Mendalam"),
  bodyPara("Laporkan hasil uji hipotesis statistik (nilai uji beserta p-value) dan interpretasi kontribusi komponen utama."),
  subHeading("4.4 Pembahasan dan Analisis Kesalahan"),
  bodyPara("Kaitkan temuan dengan literatur pada Bab II serta bahas keterbatasan kasus dan analisis kesalahan secara objektif."),

  new Paragraph({ children: [new PageBreak()] }),
  ...chapTitle("BAB V", "KESIMPULAN DAN SARAN"),
  subHeading("5.1 Kesimpulan"),
  bodyPara("Kesimpulan menjawab seluruh butir rumusan masalah pada Bab I secara langsung, padat, dan berbasis bukti kuantitatif dari Bab IV."),
  listItem("1.", "", "[Simpulan 1 menjawab rumusan masalah pertama.]"),
  listItem("2.", "", "[Simpulan 2 menjawab rumusan masalah kedua disertai angka capaian terukur.]"),
  subHeading("5.2 Saran"),
  listItem("1.", "", "[Saran pengembangan metodologis atau perluasan cakupan data/domain pada penelitian berikutnya.]"),
  listItem("2.", "", "[Saran optimalisasi efisiensi komputasi atau implementasi sistem lanjutan.]"),

  new Paragraph({ children: [new PageBreak()] }),
  ...chapTitle("DAFTAR PUSTAKA", ""),
  bodyPara("[Gunakan format APA Edisi ke-7 atau IEEE secara konsisten. Setiap entri wajib disitasi dalam naskah dan mencantumkan DOI resmi bila tersedia.]", false),
  bodyPara("Penulis, A. A., & Penulis, B. B. (Tahun). Judul artikel penelitian ilmiah. Nama Jurnal Ilmiah Bereputasi, Volume(Nomor), Halaman awal–akhir. https://doi.org/10.xxxx/xxxxx", false),

  new Paragraph({ children: [new PageBreak()] }),
  ...chapTitle("LAMPIRAN A", "KODE SUMBER / INSTRUMEN PENELITIAN"),
  bodyPara("Sertakan kode sumber inti terverifikasi, instrumen penelitian, atau log pengujian eksperimen di sini.", false),

  new Paragraph({ children: [new PageBreak()] }),
  ...chapTitle("LAMPIRAN B", "BIODATA PENULIS"),
  createStyledTable(
    ["Data Pribadi", "Keterangan"],
    [
      ["Nama Lengkap", "[Nama Penulis Disini]"],
      ["Nomor Induk Mahasiswa", "[Nomor Induk Disini]"],
      ["Tempat, Tanggal Lahir", "[Tempat, Tanggal Lahir Disini]"],
      ["Program Studi", "[Nama Program Studi Disini]"],
      ["Institusi / Perguruan Tinggi", "[Nama Universitas / Institusi Disini]"],
      ["Alamat Surel (Email)", "[Email Penulis Disini]"]
    ],
    [4000, 6000]
  )
];

const doc = new Document({
  sections: [
    {
      properties: {
        titlePage: true,
        page: { margin: MARGINS, pageNumbers: { start: 1, formatType: NumberFormat.LOWER_ROMAN } }
      },
      footers: {
        first: new Footer({ children: [] }),
        default: new Footer({
          children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], size: 20, font: "Times New Roman" })] })]
        })
      },
      children: frontChildren
    },
    {
      properties: {
        page: { margin: MARGINS, pageNumbers: { start: 1, formatType: NumberFormat.DECIMAL } }
      },
      headers: {
        default: new Header({
          children: [new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { after: 120 }, children: [new TextRun({ children: [PageNumber.CURRENT], size: 20, font: "Times New Roman" })] })]
        })
      },
      children: mainChildren
    }
  ]
});

Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync(DOCX_PATH, buffer);
  console.log("Generated universal DOCX template:", DOCX_PATH, buffer.length, "bytes");
}).catch((err) => {
  console.error(err);
  process.exit(1);
});
