# IOC Checker - AbuseIPDB Lookup Tool

**IOC Checker** adalah proyek sederhana untuk membantu analisis indikator kompromi (IOC), dimulai dari pengecekan alamat IP menggunakan [AbuseIPDB](https://www.abuseipdb.com/). Proyek ini masih dalam tahap awal dan saat ini hanya mendukung input IP secara manual satu per satu melalui command line.

---

## ✨ Fitur Saat Ini

- 🔎 Input manual alamat IP melalui CLI
- ☁️ Query data real-time ke AbuseIPDB API
- 📊 Menampilkan informasi berikut:
  - Skor reputasi (Abuse Confidence Score)
  - Jumlah laporan dan waktu terakhir dilaporkan
  - ISP, domain, dan negara asal IP
  - Detail 5 laporan terbaru dengan kategori dan komentar

---

## 🛠️ Rencana Pengembangan

- [ ] Input list IP dari file (CSV/TXT)
- [ ] Deteksi jenis IOC lain (domain, URL, hash)
- [ ] Integrasi ke layanan intelijen ancaman lain (VirusTotal, OTX, dll)
- [ ] Export hasil ke CSV/JSON
- [ ] CLI mode yang lebih interaktif dan fleksibel

---

## ⚠️ Catatan

- Script membutuhkan koneksi internet aktif
- API Key AbuseIPDB masih disimpan langsung di dalam file dan perlu kamu ubah jika ingin digunakan pribadi

---

## 🤝 Kontribusi

Kontribusi sangat terbuka! Silakan fork, buat perubahan, dan kirim pull request.

---
