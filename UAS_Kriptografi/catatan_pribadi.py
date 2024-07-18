def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Selamat datang di EncryptNote!")
    while True:
        print("\nMenu:")
        print("1. Buat Catatan Baru")
        print("2. Baca Catatan")
        print("3. Keluar")
        choice = input("Pilih opsi (1/2/3): ")

        if choice == '1':
            note = input("Masukkan catatan Anda: ")
            shift = int(input("Masukkan nilai pergeseran untuk enkripsi (misalnya, 3): "))
            encrypted_note = encrypt(note, shift)
            with open("notes.txt", "a") as file:
                file.write(f"{encrypted_note}\n")
            print("Catatan telah dienkripsi dan disimpan.")

        elif choice == '2':
            shift = int(input("Masukkan nilai pergeseran untuk dekripsi (misalnya, 3): "))
            try:
                with open("notes.txt", "r") as file:
                    notes = file.readlines()
                print("Catatan Anda:")
                for encrypted_note in notes:
                    decrypted_note = decrypt(encrypted_note.strip(), shift)
                    print(f"- {decrypted_note}")
            except FileNotFoundError:
                print("Belum ada catatan yang disimpan.")
        
        elif choice == '3':
            print("Terima kasih telah menggunakan EncryptNote. Sampai jumpa!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
