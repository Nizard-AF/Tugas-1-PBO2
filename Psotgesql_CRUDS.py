import psycopg2 as db
import os

con = None
connected = None
cursor = None

def connect():
    global connected
    global con
    global cursor
    try:
        con = db.connect( 
            host = "localhost", 
            database = "kampus", 
            port = 5432, 
            user = "nizard", 
            password = "123"
        )
        cursor = con.cursor()
        connected = True
    except:
        connected = False
    return cursor

def disconnect():
    global connected
    global con
    global cursor
    if (connected==True):
        cursor.close()
        con.close()
    else:
        con = None
    connected = False

def create_data():
    try:
        nim = input("Masukan NIM            : ")
        nama = input("Masukan Nama Lengkap   : ")
        idfa = input("Masukan ID Fakultas    : ")
        idpro = input("Masukan ID Prodi       : ")
        a = connect()
        sql = "insert into mahasiswa (nim, nama, idfakultas, idprodi) values ('"+nim+"', '"+nama+"', '"+idfa+"', '"+idpro+"')"
        a.execute(sql)
        con.commit()
        print ("Data berhasil dibuat. \n")

    except(Exception, db.Error) as error:
        print ("Galat, terjadi kesalahan memasukan data", error)

    finally:
        disconnect()

def read_data():
    try:
        a = connect()
        sql = "select * from mahasiswa"
        a.execute(sql)
        record = a.fetchall()
        
        for row in record:
            print("nim          = ", row[1])
            print("nama         = ", row[2])
            print("idfakultas   = ", row[3])
            print("idprodi      = ", row[4], "\n")
        return record

    except(Exception, db.Error) as error:
        print ("Galat, terjadi kesalahan menampilkan data", error)

    finally:
        disconnect()

def update_data():
    try:
        nim = input("Masukan NIM : ")
        a = connect()
        sql = "select * from mahasiswa where nim = '"+nim+"'"
        a.execute(sql)
        record = a.fetchall()
        print ("Data saat ini : ")
        
        for row in record:
            print("nim          = ", row[1])
            print("nama         = ", row[2])
            print("idfakultas   = ", row[3])
            print("idprodi      = ", row[4], "\n")
        
        row = a.rowcount

        if(row==1):
            print ("Silahkan input untuk mengubah data...")
            nama = input("Masukan Nama Lengkap  : ")
            idfa = input("Masukan ID Fakultas   : ")
            idpro = input("Masukan ID Prodi     : ")
            a = connect()
            sql = "update mahasiswa set nama='"+nama+"', idfakultas='"+idfa+"', idprodi='"+idpro+"' where nim='"+nim+"'"
            a.execute(sql)
            con.commit()
            print ("Update data selesai. \n")
            
            sql = "select * from mahasiswa where nim = '"+nim+"'"
            a.execute(sql)
            rec = a.fetchall()
            print ("Data setelah diubah : ")
            
            for row in rec:
                print("nim          = ", row[1])
                print("nama         = ", row[2])
                print("idfakultas   = ", row[3])
                print("idprodi      = ", row[4], "\n")
            
            return record
            
        else:
            print ("Data tidak ditemukan. \n")

    except(Exception, db.Error) as error:
        print ("Galat, terjadi kesalahan saat update data", error)

    finally:
        disconnect()
    
def delete_data():
    try:
        nim = input("Masukan NIM : ")
        a = connect()
        sql = "select * from mahasiswa where nim = '"+nim+"'"
        a.execute(sql)
        record = a.fetchall()
        print ("Data saat ini : ")
        
        for row in record:
            print("nim          = ", row[1])
            print("nama         = ", row[2])
            print("idfakultas   = ", row[3])
            print("idprodi      = ", row[4], "\n")
    
        row = a.rowcount

        if(row==1):
            jwb = input("Apakah anda ingin menghapus data ini? (y/t)")
            if(jwb.upper()=="Y"):
                a = connect()
                sql = "delete from mahasiswa where nim='"+nim+"'"
                a.execute(sql)
                con.commit()
                print ("Data berhasil dihapus. \n")
            else:
                print ("Data batal dihapus. \n")
        else:
            print ("Data tidak ditemukan. \n")

    except(Exception, db.Error) as error:
        print("Galat, terjadi kesalahan saat menghapus data", error)

    finally:
        disconnect()
    
def search_data():
    try:
        nim = input("Masukan NIM : ")
        a = connect()
        sql = "select * from mahasiswa where nim = '"+nim+"'"
        a.execute(sql)
        record = a.fetchall()
        for row in record:
            print("nim          = ", row[1])
            print("nama         = ", row[2])
            print("idfakultas   = ", row[3])
            print("idprodi      = ", row[4], "\n")
    
        print ("Pencarian Selesai. \n")
        return record

    except(Exception, db.Error) as error:
        print("Galat, terjadi kesalahan saat mencari data", error)

    finally:
        disconnect()

def show_menu():
    print("\n=== APLIKASI CRUDS PYTHON ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. Keluar")
    print("i. Test Koneksi\n")
    print("---------------------")
    print("Powered by Postgresql")
    print("---------------------")
    menu = input("Pilih menu> ")

    #clear screen
    os.system("cls")

    if menu == "1":
        create_data()
    elif menu == "2":
        read_data()
    elif menu == "3":
        update_data()
    elif menu == "4":
        delete_data()
    elif menu == "5":
        search_data()
    elif menu == "0":
        print ("\nProgram selesai...")
        print ( "---------------------" )
        print ( " created by nizard R1" )
        print ( "--------------------- \n" )
        exit()
    elif (menu.upper() == "I"):
        try:
            a = connect() 
            sql = "select * from mahasiswa limit 100"
            a.execute(sql)
            record = a.fetchall()
            print(record)
            print("\nPostgreSQL : Koneksi terhubung.")
        except:
            print("PostgreSQL : Koneksi gagal!!!")
    else:
        print("Menu salah!")

if __name__ == "__main__":
  while(True):
    show_menu() 