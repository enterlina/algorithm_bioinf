import random


def GeneratorSequence(seq_len):
    Letters = 'ACGT'
    Generated_DNA = ''
    for i in range ( 1 , seq_len + 1 ):
        Generated_DNA += random.choice ( Letters )
    #
    # DNA = random.shuffle(Generated_DNA.split())
    return Generated_DNA

print ( GeneratorSequence ( 10 ) )
print ( GeneratorSequence ( 100 ) )
print ( GeneratorSequence ( 1000 ) )
print (GeneratorSequence ( 100000 ))
