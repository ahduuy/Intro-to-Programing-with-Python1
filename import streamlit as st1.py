import streamlit as st

st.title('Intro to Programing with Python')
st.write('"Simple is better than complex"')



st.image('https://i.imgur.com/ndMW2L1.png', caption="it's easy to learn, flexible, and easy to read")

st.image('https://i.imgur.com/lTQOdb1.png')

# Mengatur tampilan dengan markdown untuk pemformatan
st.markdown(
    """
    <style>
        .centered {
            text-align: center;
            margin-top: 100px; /* Memberikan jarak dari atas */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Menampilkan judul dan kalimat penjelas di tengah layar
st.markdown('<div class="centered"><h2>Sintaks yang sederhana  dan mudah dipelajari</h2></div>', unsafe_allow_html=True)
st.markdown('<div class="centered"><p>"Python dirancang dengan sintaks yang bersih dan mirip bahasa manusia"</p></div>', unsafe_allow_html=True)

st.image('https://i.imgur.com/PSmUcOv.png')

categories = {
    "Pengembangan Web": "Contoh: Django, Flask",
    "Data Science dan Analisis Data": "Contoh: Pandas, NumPy",
    "Kecerdasan Buatan dan Machine Learning": "Contoh: TensorFlow, PyTorch",
    "Otomatisasi Tugas": "Contoh: Selenium untuk web scraping"
}

# Menampilkan kategori dalam bentuk kartu
tabs = st.tabs(list(categories.keys()))
for tab, (category, example) in zip(tabs, categories.items()):
    with tab:
        st.subheader(category)
        st.write(example)

st.image('https://i.imgur.com/y4ZfSqs.png')

# Daftar library dengan deskripsi
libraries = {
    "Matplotlib dan Seaborn": "Untuk visualisasi data yang menarik dan informatif.",
    "OpenCV": "Untuk computer vision dan pemrosesan gambar.",
    "Scikit-learn": "Untuk machine learning dan analisis data."
}

# Menampilkan daftar library dalam format horizontal
tabs = st.tabs(list(libraries.keys()))
for tab, (lib, desc) in zip(tabs, libraries.items()):
    with tab:
        st.write(f"**{lib}** - {desc}")

st.image('https://i.imgur.com/9bAnIbW.png')

st.image('https://i.imgur.com/r0Ani3M.png', caption="click the button for the detail information !")

# Daftar tools dengan deskripsi
tools = {
    "PyCharm": "IDE untuk pengembangan Python dengan fitur canggih.",
    "Visual Studio Code": "Editor kode ringan dengan banyak ekstensi.",
    "Sublime Text": "Editor teks yang cepat dan ringan.",
    "Vim": "Editor teks berbasis terminal yang kuat.",
    "GNU Emacs": "Editor teks yang sangat dapat dikustomisasi.",
    "Spyder": "IDE untuk data science dan analisis Python.",
    "Atom": "Editor kode open-source dengan UI modern.",
    "Jupyter": "Notebook interaktif untuk analisis data dan machine learning.",
    "Eclipse": "IDE populer untuk Java dan bahasa lainnya.",
    "Notepad++": "Editor teks sederhana dengan fitur tambahan."
}

# Menampilkan daftar tools dalam format grid
cols = st.columns(2)
for index, (tool, desc) in enumerate(tools.items()):
    with cols[index % 2]:
        if st.button(tool):
            st.success(f"**{tool}** - {desc}")

st.markdown('<div class="centered"><h2>Start It With </h2></div>', unsafe_allow_html=True)
st.image('https://i.imgur.com/cUAkSnQ.png', caption="little step can make a big impact")

st.markdown('<div class="centered"><h2>How to make It?</h2></div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    on1 = st.checkbox('prompt')
    if on1:
        st.image('https://i.imgur.com/TP46GMz.png')
with col2:
    on2 = st.checkbox('output')
    if on2:
        st.image('https://i.imgur.com/d34QEGE.png')
st.markdown('<div class="centered"><p>Click the toggle button!</p></div>', unsafe_allow_html=True)

st.image('https://i.imgur.com/nGqUHHq.png', caption="Don't stop, keep moving !")

st.markdown('<div class="centered"><h2>Relaxing your mind by listen to your favorite music !</h2></div>', unsafe_allow_html=True)

# Input untuk mendapatkan link Spotify
spotify_link = st.text_input("Masukkan URL Spotify (Playlist/Album/Track):", "https://open.spotify.com/playlist/2sZYutAwhMODqCaS0mYj4Z?si=5877ed7371534edc")

# Embed Spotify Player
if spotify_link:
    # Menyematkan iframe Spotify
    st.markdown(
        f'<iframe src="https://open.spotify.com/embed?uri={spotify_link}" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>',
        unsafe_allow_html=True,
    )

st.image('https://i.imgur.com/XibDx2u.png')

# Pilihan materi pelajaran
materi = st.selectbox('Pilih Tipe Data-I:', 
                      ['String', 'Float', 'Interger', 'Boolean'])

# Fungsi untuk menjelaskan materi
def penjelasan_materi(materi):
    if materi == 'String':
        return 'string adalah tipe data yang digunakan untuk merepresentasikan teks. String terdiri dari urutan karakter, yang bisa mencakup huruf, angka, simbol, dan spasi. Di banyak bahasa pemrograman, string biasanya dikelilingi oleh tanda kutip (baik itu tanda kutip tunggal atau tanda kutip ganda).'
    elif materi == 'Float':
        return 'Float adalah tipe data yang digunakan dalam pemrograman untuk merepresentasikan angka pecahan (desimal) atau bilangan riil. Berbeda dengan tipe data integer yang hanya dapat menyimpan angka bulat, float memungkinkan penggunaan angka dengan bagian desimal. '
    elif materi == 'Interger':
        return 'Integer adalah tipe data yang digunakan dalam pemrograman untuk merepresentasikan angka bulat, baik positif, negatif, maupun nol. Integer tidak memiliki bagian desimal, sehingga hanya dapat menyimpan nilai utuh tanpa fraksi. '
    elif materi == 'Boolean':
        return 'Boolean adalah tipe data yang memiliki dua nilai, yaitu True (benar) dan False (salah). Tipe data ini digunakan dalam logika dan pemrograman untuk melakukan operasi seperti AND (keduanya True), OR (salah satu atau keduanya True), dan NOT (kebalikan nilai). Boolean sangat berguna dalam pengambilan keputusan dalam kode program.'
    else:
        return 'Materi tidak ditemukan.'

# Menampilkan penjelasan
if st.button('Tampilkan Penjelasan'):
    st.write(penjelasan_materi(materi))

st.image('https://i.imgur.com/Mkmzmzu.png')

# Judul aplikasi
st.title("Tipe Data-II")

# Daftar konten dengan gambar
konten = {
    "MUTABLE": "https://i.imgur.com/ojsaDjS.png",  # Ganti dengan URL gambar yang sesuai
    "ORDERED": "https://i.imgur.com/FB1Zqao.png",  # Ganti dengan URL gambar yang sesuai
    "INDEXING/SLICING": "https://i.imgur.com/dSWOwHm.png",  # Ganti dengan URL gambar yang sesuai
    "DUPLICATE": "https://i.imgur.com/Ec8Bntf.png",  # Ganti dengan URL gambar yang sesuai
    "LIST": "https://i.imgur.com/IasqMBN.png",  # Ganti dengan URL gambar yang sesuai
    "TUPLE": "https://i.imgur.com/ixlvYti.png",  # Ganti dengan URL gambar yang sesuai
    "SET": "https://i.imgur.com/wcq4sPB.png",  # Ganti dengan URL gambar yang sesuai
    "DICTIONARY": "https://i.imgur.com/lewLbmu.png",  # Ganti dengan URL gambar yang sesuai
}

# Menampilkan daftar konten dengan interaksi
for judul, url_gambar in konten.items():
    if st.button(judul):
        st.image(url_gambar, caption=judul, use_column_width=True)  # Menampilkan gambar

# Judul aplikasi
st.title("OPERATOR")
st.image('https://i.imgur.com/ID14ALK.png')

# Daftar teks
daftar_teks = [
    "addition merujuk pada proses penjumlahan atau penggabungan dua atau lebih objek atau nilai. Proses ini dapat dilakukan menggunakan operator (+). Tergantung pada tipe data yang digunakan, addition bisa memiliki makna yang berbeda.",
    "substraction (atau pengurangan) merujuk pada proses mengurangi satu nilai dari nilai lainnya. Ini dilakukan menggunakan operator (-). Seperti halnya dengan addition, substraction memiliki makna yang berbeda tergantung pada tipe data yang digunakan.",
    "Multiplication (perkalian) adalah operasi matematika dasar yang menghitung hasil dari menambahkan suatu angka ke dirinya sendiri sebanyak jumlah tertentu.",
    "Division (pembagian) adalah operasi matematika yang membagi suatu angka (dividend) dengan angka lainnya (divisor) untuk mendapatkan hasil (quotient)",
    "Modulus (sering disebut mod atau sisa pembagian) adalah operasi matematika yang memberikan sisa dari pembagian dua angka.",
    "Exponentiation (eksponensiasi) adalah operasi matematika di mana sebuah bilangan (basis) dikalikan dengan dirinya sendiri sebanyak jumlah yang ditentukan oleh eksponen.",
    "Floor division adalah operasi pembagian yang membulatkan hasilnya ke bawah (ke bilangan bulat terdekat).",
]

# Slider untuk memilih teks
index = st.slider("Pilih Penjelasan Arithmatic :", 0, len(daftar_teks) - 1)

# Menampilkan teks berdasarkan index slider
st.text(daftar_teks[index])

daftar_teks = [
    "Equal berarti sama dengan, biasanya digunakan dalam matematika dan pemrograman untuk membandingkan dua nilai.",
    "Not Equal berarti tidak sama dengan, digunakan untuk membandingkan dua nilai dan menentukan apakah mereka berbeda.",
    "Greater than berarti lebih besar dari suatu nilai lain.",
    "Less than berarti lebih kecil dari suatu nilai lain.",
    "Greater than or equal to berarti lebih besar dari atau sama dengan suatu nilai lain.",
    "Less than or equal to berarti lebih kecil dari atau sama dengan suatu nilai lain."
]

# Slider untuk memilih teks
index = st.slider("Pilih Penjelasan Comparasion :", 0, len(daftar_teks) - 1)

# Menampilkan teks berdasarkan index slider
st.text(daftar_teks[index])

# Judul aplikasi
st.title("Referensi video untuk pembelajaran yang lebih mendalam")

# Daftar video dengan URL, judul, dan deskripsi
videos = [
    {
        "url": "https://youtu.be/_uQrJ0TkZlc?si=PAzY3G3taAy9KF5Q",
        "title": "Python Full Course for Beginners",
        "description": "Video penjelasan super lengkap terkait python untuk pemula"
    },
    {
        "url": "https://youtu.be/St48epdRDZw?si=zDsAMoxvVRlO-9Gd",
        "title": "How I Would Learn Python FAST (if I could start over)",
        "description": "menjelaskan strategi dan metode yang efektif untuk belajar Python dengan cepat"
    },
    {
        "url": "https://youtu.be/CHstO3etOBc?si=SS7MUkmLGXe7Q5rg",
        "title": "kenapa python...",
        "description": "membahas berbagai alasan mengapa Python dianggap sebagai bahasa pemrograman yang ideal untuk pemula"
    },
]

# Membagi kolom untuk menampilkan video secara horizontal
cols = st.columns(len(videos))

# Menampilkan setiap video dalam kolom dengan informasi
for i, video in enumerate(videos):
    with cols[i]:
        st.video(video["url"])
        st.subheader(video["title"])  # Menampilkan judul
        st.write(video["description"])  # Menampilkan deskripsi
