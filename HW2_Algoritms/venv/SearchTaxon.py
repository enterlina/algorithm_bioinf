class_item = {}

# class_item = {'None': [ 'Chordata' ] , 'Chordata': [ 'Reptilia' , 'Aves' , 'Mammalia' ] , 'Reptilia': [ 'Squamata' ] ,
#               'Squamata': [ 'Serpentes' ] , 'Serpentes': [ 'Pythonidae' ] ,
#               'Pythonidae': [ 'Python' , 'Morelia' , 'Morelia' , 'Morelia3' ]}


def add_class(class_item , parent_taxon , child):
    if parent_taxon not in class_item:
        class_item[ parent_taxon ] = [ ]

    class_item[ parent_taxon ].append ( child )
    # for item in child:
    #     if item not in class_item:
    #         class_item[ item ] = [ ]


def tree(class_item , child):
    for arr in class_item:
        for item in class_item[ arr ]:
            if item == child:
                return arr


def search_taxon(class_item , start):
    path = [ start ]
    k = start
    for arr in class_item:
        while k != "None":
            k = tree ( class_item , k )
            if k != "None":
                path.append ( k )
    return (' '.join ( path[ ::-1 ] ))

# print (search_taxon(class_item , 'Squamata'))

n = int ( input ( ) )
for i in range ( 0 , n ):
    class_list = input ( ).split ( )
    if class_list[ 0 ] == 'add' in class_list:
        parent_taxon = class_list[ 1 ]
        child = class_list[ 2 ]
        add_class ( class_item , parent_taxon , child )
    if class_list[ 0 ] == 'taxonomy' in class_list:
        taxon = class_list[ 1 ]
        print(search_taxon ( class_item , taxon ))
