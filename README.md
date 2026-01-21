# 🎓 Sistem Manajemen Akademik - Django

## 🎉 UPDATE TERBARU (21 Jan 2026)

Sistem akademik Anda telah diupdate dengan **3 fitur baru** yang powerful!

### ✨ Fitur Baru:
1. ✅ **Popup Profil Mahasiswa** - Klik nama untuk lihat detail
2. ✅ **Popup Profil Dosen** - Klik nama untuk lihat detail  
3. ✅ **Dynamic Search Dropdown** - Cari mahasiswa dengan mudah
4. 🎁 **Bonus:** Modal Delete yang tidak berkedip (smooth UI)

---

## 🚀 Quick Start

### 1. Jalankan Server
```bash
cd project1
python manage.py runserver
```

### 2. Akses Aplikasi
```
URL: http://127.0.0.1:8000/
Login: Gunakan admin account
```

### 3. Coba Fitur Baru
- **Profil Mahasiswa:** Buka `/mahasiswa/input/` → Klik nama mahasiswa
- **Profil Dosen:** Buka `/mahasiswa/input-dosen/` → Klik nama dosen
- **Search Mahasiswa:** Buka `/mahasiswa/input-matakuliah/` → Cari di bagian Mahasiswa

---

## 📚 Dokumentasi

| File | Untuk | Waktu |
|------|-------|-------|
| **QUICK_START.md** | User baru, ingin coba langsung | 5-10 min |
| **FITUR_BARU.md** | Developer, detail teknis | 15-20 min |
| **PERBAIKAN_SUMMARY.txt** | Manager, ringkasan | 10 min |
| **VISUAL_GUIDE.txt** | Dev advanced, architecture | 20-30 min |
| **INDEX.md** | Navigasi dokumentasi | 3-5 min |

**Rekomendasi:** Mulai dari `QUICK_START.md` 👈

---

## 📁 Struktur Project

```
framworkdjanggo/
├── env/                              # Virtual environment
├── project1/                         # Django project
│   ├── manage.py
│   ├── db.sqlite3
│   ├── project1/                     # Settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── AppMahasiswa/                # App utama
│   └── mahasiswa/                   # App data akademik
│       ├── models.py               # Database models
│       ├── views.py                # View logic + API
│       ├── urls.py                 # URL routing
│       ├── forms.py                # Form definitions
│       └── templates/
│           └── mahasiswa/
│               ├── input.html      # Input mahasiswa
│               ├── input_dosen.html # Input dosen
│               └── input_matakuliah.html # Input matakuliah
├── QUICK_START.md                   # 👈 Start here!
├── FITUR_BARU.md
├── PERBAIKAN_SUMMARY.txt
├── VISUAL_GUIDE.txt
└── INDEX.md
```

---

## 🔧 Tech Stack

- **Backend:** Django 6.0
- **Frontend:** Bootstrap 5.3.3, Font Awesome 6.4.0
- **Database:** SQLite
- **Python:** 3.13.7
- **API:** RESTful (JSON responses)

---

## 📊 Fitur yang Ditambahkan

### 1. Popup Profil Mahasiswa
```
Lokasi  : Halaman Input Mahasiswa
Trigger : Klik nama di tabel
Tampilan: Modal dengan profil lengkap
```

### 2. Popup Profil Dosen
```
Lokasi  : Halaman Input Dosen
Trigger : Klik nama di tabel
Tampilan: Modal dengan profil lengkap
```

### 3. Dynamic Search Dropdown
```
Lokasi  : Halaman Input Mata Kuliah
Fitur   : Search box + filter real-time
Select  : Checkbox multiple mahasiswa
```

### 4. Fix Modal Delete
```
Improvement : Tidak berkedip lagi
Lokasi      : Semua halaman
UX          : Lebih smooth & professional
```

---

## 🔗 API Endpoints

### Profile Mahasiswa
```
GET /mahasiswa/api/mahasiswa/<id>/profile/

Response:
{
  "id": 1,
  "nama": "Ahmad Rizki",
  "npm": "21T001",
  "email": "ahmad@univ.ac.id",
  "nohp": "08123456789",
  "alamat": "Jl. Merdeka No. 123",
  "jurusan": "Teknik Informatika"
}
```

### Profile Dosen
```
GET /mahasiswa/api/dosen/<id>/profile/

Response:
{
  "id": 1,
  "nama": "Dr. Budi Santoso",
  "nidn": "0112345",
  "email": "budi@univ.ac.id",
  "no_hp": "08123456789",
  "alamat": "Jl. Campus No. 50",
  "homebase": "Teknik Informatika"
}
```

### All Mahasiswa
```
GET /mahasiswa/api/mahasiswa/all/

Response:
[
  {"id": 1, "nama": "Ahmad Rizki", "npm": "21T001"},
  {"id": 2, "nama": "Siti Nurhaliza", "npm": "21T002"},
  ...
]
```

---

## 🧪 Testing

### Run Django Checks
```bash
python manage.py check
```

### Run Tests
```bash
python manage.py test
```

### Access Admin
```
URL: http://127.0.0.1:8000/admin/
```

---

## 📋 Changelog

### Version 1.0 (21 Jan 2026)
- ✅ Tambah popup profil mahasiswa
- ✅ Tambah popup profil dosen
- ✅ Tambah dynamic search dropdown mahasiswa
- ✅ Fix modal delete blinking
- ✅ Add API endpoints untuk profil
- ✅ Comprehensive documentation

---

## ⚙️ Setup Instructions

### 1. Activate Virtual Environment
```bash
# Windows
env\Scripts\activate

# macOS/Linux
source env/bin/activate
```

### 2. Install Dependencies (if needed)
```bash
pip install -r requirements.txt
```

### 3. Run Migrations (if needed)
```bash
python manage.py migrate
```

### 4. Create Superuser (if needed)
```bash
python manage.py createsuperuser
```

### 5. Run Server
```bash
python manage.py runserver
```

---

## 🎯 Halaman Utama

1. **Dashboard:** `/mahasiswa/`
   - Overview sistem
   - Statistik
   - Data terbaru

2. **Input Mahasiswa:** `/mahasiswa/input/`
   - Form input
   - Daftar mahasiswa
   - Edit/Hapus

3. **Input Dosen:** `/mahasiswa/input-dosen/`
   - Form input
   - Daftar dosen
   - Edit/Hapus

4. **Input Mata Kuliah:** `/mahasiswa/input-matakuliah/`
   - Form input
   - Daftar mata kuliah
   - Assign mahasiswa

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'django'"
```bash
# Solution: Activate venv dan install
source env/bin/activate
pip install django==6.0
```

### Issue: "Port 8000 already in use"
```bash
# Solution: Use different port
python manage.py runserver 8001
```

### Issue: "Database locked"
```bash
# Solution: Remove lock file
rm project1/db.sqlite3-journal
```

### Issue: "Module 'mahasiswa' has no attribute 'get_mahasiswa_profile'"
```bash
# Solution: Restart server (Ctrl+C, then run again)
python manage.py runserver
```

---

## 📞 Support

Untuk bantuan lebih lanjut:
1. Baca dokumentasi di folder root
2. Check console (F12) untuk error
3. Contact development team

---

## ✅ Checklist Before Production

- [ ] All features tested
- [ ] No console errors
- [ ] No server errors
- [ ] Data validated
- [ ] Performance checked
- [ ] Security reviewed
- [ ] Documentation complete
- [ ] Backup created
- [ ] Deployment plan ready

---

## 🎓 Learning Resources

- Django Official: https://docs.djangoproject.com/
- Bootstrap Docs: https://getbootstrap.com/docs/
- JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript/

---

## 📄 License

Copyright © 2026 Sistem Akademik. All rights reserved.

---

## 👥 Contributors

- Development Team
- QA Team
- Documentation Team

---

## 🚀 Next Steps

1. ✅ Read `QUICK_START.md`
2. ✅ Try all features
3. ✅ Test in production
4. ✅ Provide feedback
5. ✅ Deploy!

---

**Happy Coding! 🎉**

**Last Updated:** 21 Jan 2026
**Version:** 1.0.0
**Status:** Production Ready ✅

---

For questions or issues, please refer to the documentation files in this directory.
# UAS-Django-Amanda
