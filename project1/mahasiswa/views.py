from django.shortcuts import render, get_object_or_404, redirect
from .forms import MahasiswaForm
from .models import Mahasiswa
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/login/')
def input_mahasiswa(request):
    pesan = ""

    if request.method == 'POST':
        form = MahasiswaForm(request.POST)
        if form.is_valid():
            Mahasiswa.objects.create(
                nama=form.cleaned_data['nama'],
                npm=form.cleaned_data['npm'],
                email=form.cleaned_data['email'],
                nohp=form.cleaned_data['nohp'],
                alamat=form.cleaned_data.get('alamat'),
                jurusan=form.cleaned_data.get('jurusan')
            )
            pesan = "Data berhasil tersimpan"
            form = MahasiswaForm()
    else:
        form = MahasiswaForm()

    semua_mahasiswa = Mahasiswa.objects.all()

    return render(request, 'mahasiswa/input.html', {
        'form': form,
        'pesan': pesan,
        'semua_mahasiswa': semua_mahasiswa
    })

@login_required(login_url='/admin/login/')
def edit_mahasiswa(request, pk):
    mahasiswa = get_object_or_404(Mahasiswa, pk=pk)
    if request.method == 'POST':
        form = MahasiswaForm(request.POST, instance=mahasiswa)
        if form.is_valid():
            form.save()
            return redirect('mahasiswa:input_mahasiswa')
    else:
        form = MahasiswaForm(instance=mahasiswa)
    return render(request, 'mahasiswa/edit.html', {'form': form})

@login_required(login_url='/admin/login/')
def delete_mahasiswa(request, pk):
    mahasiswa = get_object_or_404(Mahasiswa, pk=pk)
    mahasiswa.delete()
    return redirect('mahasiswa:input_mahasiswa')
