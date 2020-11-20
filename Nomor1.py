satuan = ['', 'satu', 'dua', 'tiga', 'empat','lima', 'enam', 'tujuh', 'delapan', 'sembilan']


def terbilang(n):
    if n % 1 > 0 :
        carititik = str(n).find(".")
        setelahtitik = str(n)[carititik+1:]
        sebelumtitik = str(n)[0:carititik]
        hasil1 = int(sebelumtitik)
        hasil2 = int(setelahtitik)

        return terbilang(hasil1)+" koma "+terbilang(hasil2)

    elif n < 10:
        # satuan
        return satuan[n]
    elif n >= 1_000_000_000:
        # milyar
        return terbilang(n // 1_000_000_000) + ' milyar ' + terbilang(n % 1_000_000_000) if n % 1_000_000_000 != 0 else ''
    elif n >= 1_000_000:
        # juta
        return terbilang(n // 1_000_000) + ' juta ' + terbilang(n % 1_000_000) if n % 1_000_000 != 0 else ''
    elif n >= 1000:
        #ribuan
        if n // 1000 == 1:
            return " seribu " + terbilang(n % 1000) if n % 1000 != 0 else ''
        else:
            return terbilang(n // 1000) + ' ribu ' + terbilang(n % 1000) if n % 1000 != 0 else ''        
    elif n >= 100:
        # ratusan
        if n == 100:
            return "seratus"
        elif n // 100 == 1:
            return " seratus " + terbilang(n % 100) if n % 100 != 0 else ''
        
        else:
            return terbilang(n // 100) + ' ratus ' + terbilang(n % 100) if n % 100 != 0 else ''
    elif n >= 20:
        # puluhan
        return terbilang(n // 10) + ' puluh ' + terbilang(n % 10) if n % 10 != 0 else ''
    else:
        # belasan
        if n == 10:
            return ' sepuluh'
        elif n == 11:
            return ' sebelas'
        else: 
            return terbilang(n % 10) + ' belas'
            
    
    
# test
n = 12.45

print(f'{n:,} = {terbilang(n)}')