def heapify(array, index, heap_size):
  # calcola l'indice del figlio sinistro
  left_child = 2 * index + 1
  # calcola l'indice del figlio destro
  right_child = 2 * index + 2
  # inizializza l'indice del figlio massimo come quello del nodo corrente
  largest = index

  # se il figlio sinistro esiste e il suo valore è maggiore di quello del nodo corrente, imposta l'indice del figlio massimo come quello del figlio sinistro
  if left_child < heap_size and array[left_child] > array[largest]:
    largest = left_child
  # se il figlio destro esiste e il suo valore è maggiore di quello del nodo corrente, imposta l'indice del figlio massimo come quello del figlio destro
  if right_child < heap_size and array[right_child] > array[largest]:
    largest = right_child

  # se l'indice del figlio massimo è diverso da quello del nodo corrente, scambia i valori e chiama ricorsivamente heapify() per il figlio massimo
  if largest != index:
    array[largest], array[index] = array[index], array[largest]
    heapify(array, largest, heap_size)


# funzione per ordinare i file per hash usando l'algoritmo di ordinamento a cuscino
def heap_sort_hashes(files):
  # crea una copia della lista di file
  copy = files[:]