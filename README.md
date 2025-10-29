# Penerapan IndoBERT-LSTM untuk Klasifikasi Berita Hoax Berbahasa Indonesia

## Abstrak

Skripsi ini membahas implementasi model IndoBERT-LSTM untuk klasifikasi berita hoax berbahasa Indonesia. Dengan meningkatnya jumlah pengguna internet di Indonesia dan rendahnya tingkat literasi digital, penyebaran berita hoax menjadi masalah serius. Penelitian ini bertujuan untuk mengimplementasikan dan mengevaluasi performa model IndoBERT-LSTM dalam membedakan berita hoax dan non-hoax, khususnya pada topik Politik & Pemerintahan serta Kesehatan. Dataset berita hoax bersumber dari MAFINDO dan berita non-hoax dari Detik.com. Hasil penelitian menunjukkan bahwa model IndoBERT-LSTM mampu mengklasifikasikan berita hoax dengan performa yang baik.

## Fitur Utama

*   **Klasifikasi Berita Hoax:** Menggunakan model IndoBERT-LSTM untuk mengidentifikasi berita hoax berbahasa Indonesia.
*   **Preprocessing Data:** Tahapan pembersihan data meliputi penghilangan noise, *case folding*, penghapusan tanda baca, penghilangan *stopword* dan angka, serta *WordPiece Tokenizing*.
*   **IndoBERT-LSTM:** Kombinasi model pre-trained IndoBERT untuk pemahaman konteks bahasa Indonesia yang lebih baik dengan LSTM untuk menangani dependensi sekuensial dalam teks.
*   **Evaluasi Model:** Mengukur performa model menggunakan metrik seperti Akurasi, Presisi, Recall, dan F1-Score.

## Tools dan Libraries yang Digunakan

+------------------------+
| HuggingFace Transformers |
+------------------------+
| PyTorch                |
+------------------------+
| Regex                  |
+------------------------+
| BeautifulSoup          |
+------------------------+
| Requests Library       |
+------------------------+
| Pandas                 |
+------------------------+
| Scikit-learn           |
+------------------------+
