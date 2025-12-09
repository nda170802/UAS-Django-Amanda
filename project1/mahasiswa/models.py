from django.db import models
class Mahasiswa(models.Model):
    nama = models.CharField(max_length=200)
    npm = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    nohp = models.CharField(max_length=20)
    jurusan = models.CharField(max_length=100)
    alamat = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Mahasiswa"
        verbose_name_plural = "Mahasiswas"   # atau "Mahasiswa" sesuai preferensi

    def _str_(self):
        return f"{self.nama} ({self.npm})"
