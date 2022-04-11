# -*- coding: utf-8 -*-
# 앞에서 주어진 코드처럼 다음 결과를 출력하는 프로그램을 작성하시오

compressed_text_size = 148
dictionary_size = 25
total = compressed_text_size + dictionary_size
original_Text_Size = 240
compression = 100 - (float(total) / float(original_Text_Size) * 100)
print('Compressed text size: {} characters'.format(compressed_text_size,))
print('     Dictionary size: {} characters'.format(dictionary_size))
print('              Total : {} characters'.format(total))
print('  Original text size: {} characters'.format(original_Text_Size))
print('         Compression: {}%'.format(round(compression, 2)))