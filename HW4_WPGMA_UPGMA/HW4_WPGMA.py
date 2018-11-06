import numpy as np

# # Test1
# Genome_1 = [ 'A' , 'B' , 'C' , 'D' ]
# Genome_2 = [ 'A' , 'B' , 'C' , 'D' ]

# Test2
Genome_1 = [ 'A' , 'B' , 'C' , 'D' , 'E' , 'F' ]
Genome_2 = [ 'A' , 'B' , 'C' , 'D' , 'E' , 'F' ]
# Test1
# M = np.array (
#     [ [ 0.0 , 16.0 , 16.0 , 10.0 ] , [ 0 , 0 , 8.0 , 8.0 ] , [ 0 , 0 , 0 , 4.0 ] , [ 0 , 0 , 0 , 0 ] ] )

# Test2
M = np.array (
    [ [ 0.0 , 5.0 , 4.0 , 7.0 , 6.0 , 8.0 ] , [ 0.0 , 0.0 , 7.0 , 10.0 , 9.0 , 11.0 ] ,
      [ 0.0 , 0.0 , 0.0 , 7.0 , 6.0 , 8.0 ] , [ 0.0 , 0.0 , 0.0 , 0.0 , 5.0 , 9.0 ] ,
      [ 0 , 0 , 0 , 0 , 0 , 8.0 ] , [ 0 , 0 , 0 , 0 , 0 , 0 ] ] )

dictionary = {'A': 0 , 'B': 0 , 'C': 0 , 'D': 0 , 'E': 0 , 'F': 0}
# dictionary = {'A': 0 , 'B': 0 , 'C': 0 , 'D': 0}
result = Genome_1.copy ( )


def find_min(M):
    minval = np.min ( M[ np.nonzero ( M ) ] )
    position = np.where ( M == minval )
    return position


node_1 = list ( )
node_2 = list ( )


def newick(M , index1 , index2 , value):
    global dictionary
    global result
    global Genome_1
    global Genome_2
    global node_1
    global node_2
    node_1 = Genome_1[ index1 ]
    node_2 = Genome_2[ index2 ]
    new_node = node_1 + node_2
    distance = value / 2

    if (len ( new_node ) == 2):

        Genome_1[ index1 ] = new_node
        Genome_2[ index1 ] = new_node
        result[ index1 ] = '(' + node_1 + ':' + str ( distance ) + ', ' + node_2 + ':' + str ( distance ) + ')'
        dictionary[ new_node ] = distance

    else:
        distance_1 = distance - dictionary[ node_1 ]
        distance_2 = distance - dictionary[ node_2 ]
        Genome_1[ index1 ] = new_node
        Genome_2[ index1 ] = new_node

        result[ index1 ] = '(' + result[ index1 ] + ':' + str ( round ( distance_1 , 2 ) ) + ', ' + result[ index2 ] + ':' + str ( round ( distance_2 , 2 ) ) + ')'
        dictionary[ new_node ] = distance


    Genome_1 = Genome_1[ :index2 ] + Genome_1[ index2 + 1: ]
    Genome_2 = Genome_2[ :index2 ] + Genome_2[ index2 + 1: ]
    result = result[ :index2 ] + result[ index2 + 1: ]
# print ( 'res' , result )


# def newick(M , index1 , index2 , value):
#     global dictionary
#     global result
#     global Genome_1
#     global Genome_2
#     node_1 = Genome_1[ index1 ]
#     node_2 = Genome_2[ index2 ]
#     new_node = node_1 + node_2
#     distance = value / 2
#

#     if (len ( new_node ) == 2):
#
#         Genome_1[ index1 ] = new_node
#         Genome_2[ index1 ] = new_node
#         result[ index1 ] = '(' + node_1 + ':' + str ( distance ) + ', ' + node_2 + ':' + str ( distance ) + ')'
#         dictionary[ new_node ] = distance
#
#     else:
#         distance_1 = distance - dictionary[ node_1 ]
#         distance_2 = distance - dictionary[ node_2 ]
#         Genome_1[ index1 ] = new_node
#         Genome_2[ index1 ] = new_node
#
#         result[ index1 ] = '(' + result[ index1 ] + ':' + str ( distance_1 ) + ', ' + result[
#             index2 ] + ':' + str ( distance_2 ) + ')'
#         dictionary[ new_node ] = distance
#
#     Genome_1 = Genome_1[ :index2 ] + Genome_1[ index2 + 1: ]
#     Genome_2 = Genome_2[ :index2 ] + Genome_2[ index2 + 1: ]
#     result = result[ :index2 ] + result[ index2 + 1: ]
#     # print ( 'res' , result )


def insert_in_matrix_upgma(M , index1 , index2):
    row = [ 0 for x in range ( 0 , len ( M ) ) ]
    column = [ 0 for x in range ( 0 , len ( M ) ) ]
    # print ( 'i1' , index1 , 'i2' , index2 )
    cluster_len_1 = len ( node_1 )
    cluster_len_2 = len ( node_2 )
    sum_len = cluster_len_1 + cluster_len_2
    # new_value = (M[ index1 ][ i ] * cluste1_len_1) + (M[ index2 ][ i ] * cluste1_len_2) / (
    #             cluste1_len_1 + cluste1_len_2)
    # print ( 'node_1' , node_1 , 'node_2' , node_2 , 'cl1' , cluster_len_1 , 'cl2' , cluster_len_2 )
    for i in range ( 0 , len ( M ) ):
        if (i < index1) and (i < index2):
            column[ i ] = (M[ i ][ index1 ] * cluster_len_1 + M[ i ][ index2 ] * cluster_len_2) / sum_len
            # print ( "column" , column[ i ] , 'i' , i , 'Mii1' , M[ i ][ index1 ] , "Mi2i" ,
            #         M[ i ][ index2 ] )
        elif (i > index1) and (i < index2):
            row[ i ] = (M[ index1 ][ i ] * cluster_len_1 + M[ i ][ index2 ] * cluster_len_2) / sum_len
            # print ( "row1" , row[ i ] , 'i' , i , "  i1" , index1 , "i2" , index2 , 'Mi1i' , M[ index1 ][ i ] , "Mii2" ,
            #         M[ i ][ index2 ] )
        elif (i > index1) and (i > index2):
            row[ i ] = (M[ index1 ][ i ] * cluster_len_1 + M[ index2 ][ i ] * cluster_len_2) / sum_len
            # print ( "row2" , row[ i ] , 'i' , i , "i1" , index1 , "i2" , index2 , 'Mi1i' , M[ index1 ][ i ] , "Mi2i" ,
            #         M[ index2 ][ i ] )
    # print ( "  \nrow" , row , "   column" , column )
    del row[ index2 ]
    del row[ index1 ]
    del column[ index1 ]

    M = np.delete ( M , index1 , axis=0 )
    M = np.delete ( M , index2 - 1 , axis=0 )
    M = np.delete ( M , index1 , axis=1 )
    M = np.delete ( M , index2 - 1 , axis=1 )

    M = np.insert ( M , index1 , row , axis=0 )
    M = np.insert ( M , index1 , column , axis=1 )
    return M


# def wpgma(M):
#     while (len ( M ) > 1):
#         position = find_min ( M )
#         index1 = int ( position[ 0 ] )
#         index2 = int ( position[ 1 ] )
#         newick ( M , index1 , index2 , M[ index1 , index2 ] )
#         M = insert_in_matrix ( M , index1 , index2 )
#
#     else:
#         return result[ 0 ]


def upgma(M):
    while (len ( M ) > 1):
        position = find_min ( M )
        index1 = int ( position[ 0 ] )
        index2 = int ( position[ 1 ] )
        newick ( M , index1 , index2 , M[ index1 , index2 ] )
        # print ( 'i1' , index1 , 'i2' , index2 , 'Genome1' ,
        #         Genome_1 , 'Genome2' , Genome_2 )
        M = insert_in_matrix_upgma ( M , index1 , index2 )

        # Genome1_1=

    else:
        return result[ 0 ]


print ( 'Matrix \n' , np.matrix ( M ) )
print ( 'UPGMA' , upgma ( M ) )

# print ( 'Matrix \n' , np.matrix ( M ) )
# print ( 'WPGMA' , wpgma ( M ) )
