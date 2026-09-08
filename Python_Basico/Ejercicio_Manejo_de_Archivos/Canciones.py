def read_file(path):
    Sorted_songs = []
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for number, line in enumerate(lines, start=1):
            Sorted_songs.append(line.strip())

    Sorted_songs.sort()      
    return Sorted_songs
        
def Write_and_sorted(path, text):
    with open(path, 'w', encoding= "utf-8") as file:
        file.write(str(text))

def main():
    path = "Canciones.txt"
    New_path = "Canciones_Ordenadas.txt"
    New_list = read_file(path)
    Write_and_sorted(New_path, New_list)

main()