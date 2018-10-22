import numpy as np

# Genome_1 = "TCCT"
# Genome_2 = "ATCT"

# Genome_1 = "TCCCAGT"
# Genome_2 = "AATTGCC"
# #
Genome_1 = "TCCCAGTTATGTCAGGGGACACGAGCATGCAGAGAC"
Genome_2 = "AATTGCCGCCGTCGTTTTCAGCAGTTATGTCAGATC"

len_Genome1 = len ( Genome_1 )
len_Genome2 = len ( Genome_2 )

match = 1
mismatch = -1
gapopen = -100
gapscore = -0.01


gap = '-'

Aligned_G1 = list ( )
Aligned_G2 = list ( )

print ('Original sequence:')

print ("Genome 1:" , Genome_1)
print ("Genome 2:" , Genome_2)
print("match:", match )
print("mismatch:", mismatch )
print("gapopen:", gapopen)
print("gapscore:", gapscore)


M = [ [ 0 for x in range ( len_Genome1 + 1 ) ] for y in range ( len_Genome2 + 1 ) ]

diag = [ [ 0 for x in range ( len_Genome1 + 1 ) ] for y in range ( len_Genome2 + 1 ) ]
left = [ [ gapopen for x in range ( len_Genome1 + 1 ) ] for y in range ( len_Genome2 + 1 ) ]
top = [ [ gapopen for x in range ( len_Genome1 + 1 ) ] for y in range ( len_Genome2 + 1 ) ]

Path_M = [ [ '-' for x in range ( len ( Genome_1 ) ) ] for y in range ( len ( Genome_2 ) ) ]

while len ( Genome_1 ) < len_Genome1:
    Genome_1 += gap
while len ( Genome_2 ) < len_Genome2:
    Genome_2 += gap

for i in range ( 0 , len ( Genome_1 ) + 1 ):
    for j in range ( 0 , len ( Genome_2 ) + 1 ):
        counter = 1
        if counter > 0:
            if j == 1:
                left[ i ][ j ] = M[ i ][ j - 1 ] + (gapopen + gapscore)
            if j > 1:
                left[ i ][ j ] = max ( M[ i ][ j - 1 ] + (gapopen + gapscore) , left[ i ][ j - 1 ] + gapscore )
        if counter > 0:
            if i == 1:
                top[ i ][ j ] = M[ i - 1 ][ j ] + (gapopen + gapscore)
            if i > 1:
                top[ i ][ j ] = max ( M[ i - 1 ][ j ] + (gapopen + gapscore) , top[ i - 1 ][ j ] + gapscore )
        if (i == 0) and (j == 0):
            M[ i ][ j ] = 0
        if (i == 0) and (j > 0):
            M[ i ][ j ] = left[ i ][ j ]
        if (i > 0) and (j == 0):
            M[ i ][ j ] = top[ i ][ j ]

        if (i > 0) and (j > 0):
            if Genome_2[ i - 1 ] == Genome_1[ j - 1 ]:
                match_cost = match
            else:
                match_cost = mismatch

            M[ i ][ j ] = max ( (M[ i - 1 ][ j - 1 ] + match_cost) , top[ i ][ j ] , left[ i ][ j ] )

            if M[ i ][ j ] == top[ i ][ j ]:
                Path_M[ i - 1 ][ j - 1 ] = "top"
                counter = 0
            if M[ i ][ j ] == left[ i ][ j ]:
                Path_M[ i - 1 ][ j - 1 ] = "left"
                counter = 0

            if M[ i ][ j ] == (M[ i - 1 ][ j - 1 ] + match_cost):
                Path_M[ i - 1 ][ j - 1 ] = "diag"
                counter += 1

# print ('\ndiag\n' , np.matrix ( diag ))
# print ('\ntop\n' , np.matrix ( top ))
# print ('\nleft\n' , np.matrix ( left ))
# print ('\nAligned Matrix\n' , np.matrix ( M ))
# print ('\nPathM\n' , np.matrix ( Path_M ))

# Restore Alignment
k = len ( Genome_1 ) - 1
m = len ( Genome_2 ) - 1



while (m >= 0) & (k >= 0):
    if Path_M[ m ][ k ] == 'diag':
        Aligned_G1.append ( Genome_1[ k ] )
        Aligned_G2.append ( Genome_2[ m ] )
        k -= 1
        m -= 1
    elif Path_M[ m ][ k ] == 'left':
        Aligned_G1.append ( Genome_1[ k ] )
        Aligned_G2.append ( gap )
        k -= 1
    elif Path_M[ m ][ k ] == 'top':
        Aligned_G1.append ( gap )
        Aligned_G2.append ( Genome_2[ m ] )
        m -= 1

if m >= 0 and k <= 0:
    while m >= 0:
        Aligned_G1.append ( gap )
        Aligned_G2.append ( Genome_2[ m ] )
        m -= 1

elif m <= 0 and k >= 0:
    while k >= 0:
        Aligned_G1.append ( Genome_1[ k ] )
        Aligned_G2.append ( gap )
        k -= 1

Final_G1 = ''.join ( list ( reversed ( Aligned_G1 ) ) )
Final_G2 = ''.join ( list ( reversed ( Aligned_G2 ) ) )

print ('\nAligned Genome1:\n' , Final_G1)
print ('Aligned Genome2:\n' , Final_G2)
