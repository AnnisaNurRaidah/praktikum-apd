dataadmin = {
    'hatchu': {'password': 's2u', 'role': 'admin'}
}

daftarmember = {
    "carmen": {"password": "08123456789", "instrumen": "gitar", "harga": 750000, "role": "member"},
    "jiwoo": {"password": "0811112222", "instrumen": "piano", "harga": 1000000, "role": "member"},
    "juun": {'password': "0833334444", "instrumen": "gitar", "harga": 750000, "role": "member"}
}

def hitungharga(instrumen):
    if instrumen == 'gitar':
        return 750000
    elif instrumen == 'piano':
        return 1000000
    else:
        return 0

def carimember(keyword):
    hasil = []
    keywordlower = keyword.lower()
    
    for nama, data in daftarmember.items():
        if keywordlower in nama.lower() or keywordlower in data['instrumen'].lower():
            hasil.append((nama, data))
    
    return hasil

def userterdaftar(username):
    return username in dataadmin or username in daftarmember