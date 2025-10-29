# Penerapan IndoBERT-LSTM untuk Klasifikasi Berita Hoax Berbahasa Indonesia

## Abstrak

Skripsi ini membahas implementasi model IndoBERT-LSTM untuk klasifikasi berita hoax berbahasa Indonesia. Dengan meningkatnya jumlah pengguna internet di Indonesia dan rendahnya tingkat literasi digital, penyebaran berita hoax menjadi masalah serius. Penelitian ini bertujuan untuk mengimplementasikan dan mengevaluasi performa model IndoBERT-LSTM dalam membedakan berita hoax dan non-hoax, khususnya pada topik Politik & Pemerintahan serta Kesehatan. Dataset berita hoax bersumber dari MAFINDO dan berita non-hoax dari Detik.com. Hasil penelitian menunjukkan bahwa model IndoBERT-LSTM mampu mengklasifikasikan berita hoax dengan performa yang baik.

## Fitur Utama

*   **Klasifikasi Berita Hoax:** Menggunakan model IndoBERT-LSTM untuk mengidentifikasi berita hoax berbahasa Indonesia.
*   **Preprocessing Data:** Tahapan pembersihan data meliputi penghilangan noise, *case folding*, penghapusan tanda baca, penghilangan *stopword* dan angka, serta *WordPiece Tokenizing*.
*   **IndoBERT-LSTM:** Kombinasi model pre-trained IndoBERT untuk pemahaman konteks bahasa Indonesia yang lebih baik dengan LSTM untuk menangani dependensi sekuensial dalam teks.
*   **Evaluasi Model:** Mengukur performa model menggunakan metrik seperti Akurasi, Presisi, Recall, dan F1-Score.

## Tools dan Libraries yang Digunakan

[![HuggingFace Transformers](https://img.shields.io/badge/HuggingFace_Transformers-PyTorch-orange?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/docs/transformers/index)
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep_Learning-red?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Regex](https://img.shields.io/badge/Regex-Pattern_Matching-green?style=for-the-badge&logo=regex&logoColor=white)](https://docs.python.org/3/library/re.html)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web_Scraping-blue?style=for-the-badge&logo=beautifulsoup&logoColor=white)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
[![Requests Library](https://img.shields.io/badge/Requests_Library-HTTP-purple?style=for-the-badge&logo=requests&logoColor=white)](https://docs.python-requests.org/en/latest/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-yellow?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine_Learning-brightgreen?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/stable/)
