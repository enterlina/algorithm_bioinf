class DNA ( ):
    pass


class RNA ( ):
    pass


string_RNA = "UCTGUUTCCT"
string_DNA = "ACTGAAACCT"


def count_gc(string_RNA):
    counter = 0
    gc_percent = 0
    gc_init = 'G'
    # gc_init = [ 'G' , 'C' ]
    for i in range[ 0 , len ( string_RNA ) + 1 ]:
        if gc_init in string_RNA:
            counter += 1
    gc_percent = counter * 100 / len ( string_RNA )
    return gc_percent

# if gc_init[ 0 ] or gc_init[ 1 ] in string_RNA:
print ( 'count RNA' , count_gc ( string_RNA ) )

# try:
#     #text block
# except:
#     raise('Wrong text etc')


# Создать классы Dna и Rna, объекты которых обладают следующими свойствами:
# Могут быть инициализированы строкой, соответствующей последовательности ДНК и РНК, соответственно
# Позволяют определить GC состав последовательности с помощью метода gc()
# Позволяют создать комплеметнарную последовательность с помощью метода reverse_complement()
#
# Объекты класса Dna дополнительно позволяют:
# Создавать объект класса Rna, соответствующий результату транскрипции последовательности оригинального объекта с использованием метода transcribe()
