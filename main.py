from layanan.sistem_inti import SistemInti
from layanan.mahasiswa_service import LayananMahasiswa
from layanan.peralatan_service import LayananPeralatan
from layanan.transaksi_service import LayananTransaksi
from layanan.laporan_service import LayananLaporan
from layanan.menu_service import LayananMenu


class SistemLaboratorium(
    SistemInti,
    LayananMahasiswa,
    LayananPeralatan,
    LayananTransaksi,
    LayananLaporan,
    LayananMenu,
):
    pass


def main():
    sistem = SistemLaboratorium()
    sistem.data_awal()
    sistem.jalankan()


if __name__ == "__main__":
    main()
