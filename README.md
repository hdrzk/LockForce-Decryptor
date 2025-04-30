# 🐍💻 LockForce & Decryptor — Python Ransomware Simulation

![Python](https://img.shields.io/badge/Made%20With-Python-306998?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/For-Education%20Only-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Simulasi-Virus%20%26%20Antivirus-blue?style=for-the-badge)

> Simulasi sederhana pembuatan ransomware dan antivirus menggunakan Python, dibuat untuk keperluan pembelajaran keamanan komputer.

---

## 📌 Deskripsi Proyek

- **LockForce** adalah virus simulasi yang mengenkripsi file dengan ekstensi tertentu di folder `Documents`, serta membuat file ransom note di Desktop.
- **LockForce Decryptor** adalah antivirus yang digunakan untuk mendekripsi file yang telah dikunci oleh virus LockForce, menggunakan kunci simetris (`key.key`).

---

## 🚨 PERINGATAN

> 🛑 **Script ini hanya untuk pembelajaran!**  
> Jalankan hanya di lingkungan **Virtual Machine (VM)** dan **jangan digunakan untuk tujuan merusak**.  
> Penulis tidak bertanggung jawab atas penyalahgunaan.

---

## 🧩 Fitur

### 🔒 LockForce (virus simulasi)
- Mengenkripsi file `.txt`, `.jpg`, `.docx`, `.pdf` di folder `Documents`.
- Membuat ransom note (`README_LOCKED.txt`) di Desktop.
- Popup peringatan setelah infeksi.

### 🔓 LockForce Decryptor
- Mendekripsi file yang telah dikunci.
- Menghapus ransom note.
- Menggunakan file `key.key` sebagai kunci dekripsi.

---

## 🧪 Teknologi Digunakan

- **Python 3**
- Library: `cryptography`, `tkinter`, `os`
- **Virtual Machine**: Windows 10 (untuk pengujian aman)
- **PyInstaller** (untuk konversi `.py` → `.exe`)

---

## ⚙️ Cara Menggunakan

### ▶️ Menjalankan Virus
1. Jalankan `lockforce.py` atau file `.exe` hasil compile.
2. File di `Documents` akan terkunci, dan ransom note dibuat di Desktop.

### 🛠 Menjalankan Antivirus
1. Pastikan file `key.key` berada di folder yang sama dengan `unlockforce.py`.
2. Jalankan script untuk mengembalikan semua file yang terenkripsi.

---

## 👨‍💻 Kontributor

- Nama: Haidir Zacky
- Tujuan: Edukasi dan simulasi mekanisme virus & antivirus

---

## 📜 Lisensi

Project ini dibuat untuk **tujuan edukasi** dan **tidak boleh digunakan secara ilegal**.
