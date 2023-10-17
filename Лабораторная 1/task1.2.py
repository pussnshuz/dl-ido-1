# TODO Найдите количество книг, которое можно разместить на дискете
diskette_size = 1.44
page_count = 100
lines = 50
symbols = 25
one_symbol = 4
mb_in_kb, byte_in_kb = 1024, 1024
diskette_size_in_byte = diskette_size*byte_in_kb*mb_in_kb
one_book = one_symbol*symbols*lines*page_count
books = round(diskette_size_in_byte//one_book)
print("Количество книг, помещающихся на дискету:", books)
