# class animals_taxonomy ( list):
animals = {'None': [ 'Chordata' ] , 'Chordata': [ 'Reptilia' , 'Aves' ] , 'Aves': [ 'Squamata' ]}

path = ''


# def add(animals , parent , child):
#     self.animals[ parent ].append ( parent )
#     self.animals[ child ] = child

# print (animals['Chordata'][0], animals['Chordata'][1], )

def tree(animals , child):
    for item in animals:
        if child in animals[ item ]:
            return item


print( tree ( animals , 'Aves' ))

# def get(animals , child):
#     path = tree ( animals , child )
#     if path == "None":
#         return
#
#     if child in animals[ child ]:
#         return
#     elif animals[ space ][ 0 ] != "None":
#         self.get ( self.names[ space ][ 0 ] , var )
#         return
#     else:
#         print("None")
#     return



def search_taxon(animals , start ):
    path = [ ]
    k = start
    for i in animals:
        while k != 'None':
            k = tree ( animals , k )
            path.append ( k )
        #     print ('path', path,'k',k)
        # print (' '.join(path[::-1]))
    return (' '.join(path[::-1]))
print("search taxon", search_taxon(animals , 'Squamata' ))

#
# k='Squamata'
# for i in animals:
#     while k!= 'None':
#         k = tree ( animals , k )
#         path.append(k)
#
# print (' '.join(path[::-1]))


# n = int ( input ( ) )
# for i in range ( n ):
#     s.input ( ).split ( )
#     if s[ 0 ] == "add":
#         add ( s[ 1 ] , s[ 2 ] )
#     if s[ 0 ] == "get":
#         get ( s[ 1 ] )
