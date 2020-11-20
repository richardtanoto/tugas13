satuan = ['', 'one', 'two', 'three', 'four','five', 'six', 'seven', 'eight', 'nine']


def terbilang(n):
    if n % 1 > 0 :
        carititik = str(n).find(".")
        setelahtitik = str(n)[carititik+1:]
        sebelumtitik = str(n)[0:carititik]
        hasil1 = int(sebelumtitik)
        hasil2 = int(setelahtitik)

        return terbilang(hasil1)+" point "+terbilang(hasil2)

    elif n < 10:
        # satuan
        return satuan[n]     
    elif n >= 1_000_000_000:
        # milyar
        return terbilang(n // 1_000_000_000) + ' billion ' + terbilang(n % 1_000_000_000) if n % 1_000_000_000 != 0 else ''
    elif n >= 1_000_000:
        # juta
        return terbilang(n // 1_000_000) + ' million ' + terbilang(n % 1_000_000) if n % 1_000_000 != 0 else ''
    elif n >= 1000:
        #ribuan
        if n // 1000 == 1:
            return " a thousand " + terbilang(n % 1000) if n % 1000 != 0 else ''
        else:
            return terbilang(n // 1000) + ' thousand ' + terbilang(n % 1000) if n % 1000 != 0 else ''        
    elif n >= 100:
        # ratusan
        if n // 100 == 1:
            return " one hundred " + terbilang(n % 100) if n % 100 != 0 else ''
        else:
            return terbilang(n // 100) + ' hundred ' + terbilang(n % 100) if n % 100 != 0 else ''
    elif n == 20:
        # puluhan
        return ' twenty '
    elif n == 30:
        
        return ' thirty '
    elif n == 40:
        
        return ' forty '
    elif n == 50:
        
        return ' fifty '
    elif n == 60:
        
        return ' sixty '
    elif n == 70:
        
        return ' seventy '
    elif n == 80:
        return ' eighty '
    elif n == 90:
        return ' ninety '
    else:
        # belasan
        if n == 10:
            return ' ten'
        elif n == 11:
            return ' eleven'
        elif n == 12:
            return ' twelve'
        elif n == 15:
            return ' fifteen'
        else: 
            return terbilang(n % 10) + 'teen'
            
    
    
# test
n = 90

print(f'{n:,} = {terbilang(n)}')