import streamlit as st
import time
from datetime import datetime

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="Selamat Tahun Baru 2025", layout="centered")

# Judul dan deskripsi
st.title("🎉 Selamat Tahun Baru 2025! 🎉")
st.markdown(
    """Selamat datang di Aplikasi Perayaan Tahun Baru! 
    Mari kita rayakan kedatangan tahun 2025 bersama dengan hitungan mundur, resolusi, dan pesan motivasi."""
)

# Hitungan Mundur
st.header("⏳ Hitungan Mundur ke 2025")
waktu_sekarang = datetime.now()
waktu_tujuan = datetime(2025, 1, 1, 0, 0, 0)
sisa_waktu = waktu_tujuan - waktu_sekarang

def format_waktu_delta(td):
    hari, detik = td.days, td.seconds
    jam = detik // 3600
    menit = (detik % 3600) // 60
    detik = detik % 60
    return f"{hari} hari, {jam:02} jam, {menit:02} menit, {detik:02} detik"

if sisa_waktu.total_seconds() > 0:
    st.info(f"Waktu tersisa hingga 2025: {format_waktu_delta(sisa_waktu)}")
else:
    st.success("🎆 Selamat Tahun Baru 2025! 🎆")

# Bagian Resolusi
st.header("📜 Resolusi Tahun Baru")
daftar_resolusi = []
resolusi = st.text_input("Tulis Resolusi Tahun Baru Anda di sini:")
if st.button("Tambah Resolusi"):
    if resolusi:
        daftar_resolusi.append(resolusi)
        st.success(f"Berhasil ditambahkan: {resolusi}")
    else:
        st.warning("Harap tuliskan sesuatu sebelum menambahkan!")

if daftar_resolusi:
    st.write("### Resolusi Anda:")
    for i, res in enumerate(daftar_resolusi, 1):
        st.write(f"{i}. {res}")

# Pesan Motivasi
st.header("🌟 Pesan Motivasi untuk 2025")
kutipan_motivasi = [
    "Cara terbaik untuk memprediksi masa depan adalah dengan menciptakannya.",
    "Setiap awal baru datang dari akhir sebuah awal lainnya.",
    "Bermimpi besar, bekerja keras, dan wujudkan!",
    "2025 adalah tahunmu untuk bersinar!",
    "Percayalah pada diri sendiri dan semua yang kamu miliki.",
    "Tahun Baru, Tujuan Baru, Dirimu yang Baru!"
]
if st.button("Dapatkan Pesan Motivasi"):
    kutipan = kutipan_motivasi[int(time.time()) % len(kutipan_motivasi)]
    st.success(kutipan)

# Bagian Motivasi Diri
st.header("💡 Motivasi Diri")
motivasi_diri = """
## Motivasi Diri

Motivasi adalah kekuatan yang mendorong seseorang untuk bertindak, mencapai tujuan, dan menghadapi tantangan. Dalam kehidupan, motivasi berperan sebagai bahan bakar yang membantu kita tetap fokus dan bersemangat dalam mencapai apa yang kita inginkan.

### Jenis-jenis Motivasi
1. **Motivasi Intrinsik**
   - Berasal dari dalam diri sendiri, seperti keinginan untuk berkembang, rasa ingin tahu, atau kepuasan pribadi.

2. **Motivasi Ekstrinsik**
   - Dipengaruhi oleh faktor eksternal, seperti penghargaan, pengakuan, atau tekanan dari lingkungan.

### Cara Meningkatkan Motivasi
1. **Menetapkan Tujuan yang Jelas**
   - Tentukan apa yang ingin dicapai dengan spesifik dan realistis.

2. **Membagi Tujuan Besar Menjadi Langkah-langkah Kecil**
   - Langkah kecil membuat tujuan terasa lebih mudah dicapai dan memberi rasa pencapaian setiap kali langkah tersebut diselesaikan.

3. **Menciptakan Lingkungan yang Mendukung**
   - Kelilingi diri dengan orang-orang yang positif dan mendukung, serta ciptakan ruang kerja yang nyaman.

4. **Menghargai Diri Sendiri**
   - Rayakan pencapaian kecil sebagai bentuk penghargaan atas usaha yang telah dilakukan.

5. **Mengatasi Rasa Malas**
   - Mulailah dengan langkah kecil, fokus pada manfaat jangka panjang, dan hindari gangguan yang tidak perlu.

6. **Mendapatkan Inspirasi dari Orang Lain**
   - Bacalah buku motivasi, tonton video inspiratif, atau dengarkan kisah sukses untuk menyegarkan semangat.

### Pentingnya Motivasi
Motivasi membantu kita:
- Menjaga fokus pada tujuan.
- Mengatasi hambatan dan tantangan.
- Meningkatkan produktivitas dan efisiensi.
- Mencapai kepuasan pribadi dan profesional.

### Kesimpulan
Motivasi adalah elemen penting dalam perjalanan hidup. Dengan memahami jenis motivasi dan cara meningkatkannya, kita dapat menghadapi tantangan hidup dengan lebih percaya diri dan semangat. Ingatlah bahwa motivasi bukan hanya tentang memulai, tetapi juga tentang menjaga momentum hingga tujuan tercapai.
"""
st.markdown(motivasi_diri)

# Footer
st.markdown("""---\nDikembangkan dengan ❤️ untuk membuat Tahun Baru Anda istimewa!""")
