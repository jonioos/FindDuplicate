import os
import hashlib
import time
from datetime import datetime
from heapify import heap_sort_hashes

def main():
    # chiedi all'utente di inserire il percorso della cartella
    percorso = input('Inserisci il percorso della cartella:')
    start_time = time.time()

    # ottiene la lista dei file nella cartella
    lista_files = []
    for root, dirs, files in os.walk(percorso, topdown=False):
        for name in files:
            lista_files.append(os.path.join(root, name))
    
    files = lista_files

    # ordina i file per hash usando l'algoritmo di ordinamento a cuscino
    files = heap_sort_hashes(files)

    # inizializza una variabile per memorizzare l'hash precedente
    previous_hash = None
    previous_file = None
    log = ""
    # cicla attraverso ogni file nella cartella
    for file in files:
        # calcola l'hash del file
        if(os.path.isfile(file)):
            print(f"Analizzo {file}")
            hash = hashlib.sha1(open(os.path.join(percorso, file), 'rb').read()).hexdigest()
            # se l'hash è uguale all'hash precedente, il file è un duplicato
            if hash == previous_hash:
                print(f'Il file "{file}" è un duplicato di un altro file "{previous_file}" nella cartella')
                log += f"[{file}]\n{previous_file}\n{percorso}/{file}\n\n"
            # altrimenti, aggiorna l'hash precedente
            else:
                previous_hash = hash
                previous_file = file
    elapsed_time = time.time() - start_time
    d = datetime.now().strftime("%Y%m%d_%H:%M:%S")
    f = open(f"duplicate_log{d}.txt", "w")
    f.write(log)
    f.close()
    print('Il tempo trascorso è: {:.2f} secondi'.format(elapsed_time))
    

main()