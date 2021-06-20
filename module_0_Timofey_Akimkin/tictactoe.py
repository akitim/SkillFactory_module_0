# -*- coding: utf-8 -*-
"""Tictactoe.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11RC4Ey83-6eAHUJSlsbEHTdU1KN00l5y
"""

s0 = [' ', '   ', 0, '   ',   1, '   ',  2,  '   ']
s1 = [ 0, ' | ', 'x', ' | ', 'x', ' | ','o', ' | ']
s2 = [ 1, ' | ', 'o', ' | ', 'o', ' | ','x', ' | ']
s3 = [ 2, ' | ', ' ', ' | ', ' ', ' | ','o', ' | ']
 
hline = '    _ _ _ _ _ _ _ _ _ '
def field_init():
  return [[' ', ' ', ' '] for i in range(3) ]
 
# turn = list(map( int, input().split() ))
# turn
# field_ = field_init ()
 
field_ = [ ['=', '=', '='], 
           ['=', 'x', '='],
           ['=', '=', '='] ]
 
# def is_game_end(field_):
  # if 
 
 def field_print ( field ):
  pass 
for i in range(3): 
  print (*field_[i])
  print ()
 
print ()
print (*s0)
print (hline)
print ('')
print (*s1)
print (hline)
print ('')
print (*s2)
print (hline)
print ('')
print (*s3)
print (hline)

"""Вывод поля"""

field_ = [ [' ', 'O', 'O'], 
           ['X', 'X', ' '],
           [' ', ' ', ' '] ]

field_ = field_init ()
 
hline = '   |_ ___| _ __| _ __| '
 
s0 = [' ', '   ', '0', '   ', '1', '   ', '2', '   ']
s1 = ['0', ' | ', 'Х', ' | ', 'x', ' | ', 'o', ' | ']
s2 = ['1', ' | ', 'О', ' | ', 'o', ' | ', 'x', ' | ']
s3 = ['2', ' | ', ' ', ' | ', ' ', ' | ', 'o', ' | ']
 
def field_print ( field_ ):
    field_out = [ [' ', '   ', '  0', '   ', '  1', '   ', '  2',
                   '   \n     _______________________   ',], [], [], [] ]
    for i in range(1,4):
        for j in range (8):
            if j == 0:
                field_out[i].append (i - 1)
            elif j % 2:
                field_out[i].append ('  |  ') #field_[i-1] [] #[0 1 2] [1 3 5 7]
            else:
                #print ( i,' ', j, '  ', j//2 - 1 )
                field_out[i].append ( field_[i-1] [j//2-1] )
 
    print ( *field_out[0] ) # вывод игрового поля
    print ('    |       |       |       |' )
    for k in field_out[1:3]:
        print ( *k )
        print ('    |_ _ _ _| _ _ _ |_ _ _ _| \n    |       |       |       |' )
        #print ('')
    print ( *field_out[3] )
    print ('    |_______|_______|_______|  ' )
 
#print ('i', ' ',  'j', 'j//2-1')
field_print ( field_ )

def check_valid_move(mv, field_): #проверка правильности хода
    ls = mv. split () 
    if len(ls) != 2:
        return 'Так ходить нельзя! Сделайте другой ход :)'
    else:
        [row, col] = list ( map (int, (ls ) ) )
    if any ( [row not in [0, 1, 2] , col not in [0, 1, 2] ] ):
        return 'Так ходить нельзя! Сделайте другой ход =).'
    elif field_[row] [col] != ' ':
        return 'Клетка занята! ¯\_(ツ)_/¯ Сделайте другой ход. '
    else: return 'ok'
 
check_valid_move(input(), field_)

field_ = [ ['5', 'O', 'X'], 
           ['X', 'eX', 'X'],
           ['wX', 'X', 'l'] ]
 
ls = [ [ c == 'X' for c in s ] for s in field_ ]
#all ( ls )
list ( map (all, [ [ c == 'X'for c in s ] for s in field_ ] ) )
#[ [ i[j] for i in field_ ] for j in range (3) ]
[ field_ [i] [i] for i in range (3) ]
[ field_ [i] [2-i] for i in range (3) ]

def check_win ( xo, field_ ):
    is_rows = list ( map (all, [ [ c == xo for c in s ] for s in field_ ] ) )
 
    field_t = [ [ s[i] for s in field_ ] for i in range (3) ]
    is_cols = list ( map (all, [ [ c == xo for c in s ] for s in field_t] ) )
 
    is_diag_1 = [ field_[i] [i] == xo for  i in range (3) ]
 
    is_diag_2 = [ field_[i] [i] == xo for  i in range (3) ]
    
    if any ( is_rows ):  #проверяем выигрыш по строкам
        return True
    elif any ( is_cols ): #проверяем выигрыш по столбцам
        return True
    elif all (  is_diag_1  ): #проверяем выигрыш по главной диагонали
        return True
    elif all (  is_diag_2  ): #проверяем выигрыш по второй диагонали
        return True
    else: return False
 
field_ = [ ['X', 'eX', 'X'], 
           ['wX', 'X', 'eX'],
           ['rX', 'X', 'eX'] ]
 
check_win ('X', field_)

field_ = [ ['5', ' ', 'X'], 
           ['X', 'eX', 'X'],
           ['wX', 'X', ' '] ] 
def is_final ( field_ ):
    ''' Проверка, сделан ли последний ход: True, если сделан; False - если нет'''
    f = []
    for s in field_: f += s #разворачиваем игровое поле в "простой" список                
    return all ( [ c != ' ' for c in f ] )
         
is_final (field_)

"""# **Ядро**"""

def field_init():
  '''Инициализирует игровое поле пробелами'''

  return [[' ', ' ', ' '] for i in range(3) ]


def field_print ( field_ ):
  field_out = [ [' ', '   ', '  0', '   ', '  1', '   ', '  2',
                   '   \n     _______________________   ',], [], [], [] ]
  for i in range(1,4):
    for j in range (8):
      if j == 0:
        field_out[i].append (i - 1)
      elif j % 2:
        field_out[i].append ('  |  ') #field_[i-1] [] #[0 1 2] [1 3 5 7]
      else:
        #print ( i,' ', j, '  ', j//2 - 1 )
        field_out[i].append ( field_[i-1] [j//2-1] )
 
  print ( *field_out[0] ) # вывод игрового поля
  print ('    |       |       |       |' )
  for k in field_out[1:3]:
    print ( *k )
    print ('    |_ _ _ _| _ _ _ |_ _ _ _| \n    |       |       |       |' )
        #print ('')
  print ( *field_out[3] )
  print ('    |_______|_______|_______|  ' )
 

def check_valid_move(mv, field_): 
  '''Проверка правильности хода. 1й аргумент - ход в виде строки, 2й аргумент игровое поле
      в виде списка из 3 списков по 3 элемента - символа. Возвращает сообщение в зависимости от ошибки ввода.'''

  ls = mv.split () 

  if len(ls) != 2 or any ( [ s not in [ '0', '1', '2' ] for s in ls] ):
      return 'Так ходить нельзя! Сделайте другой ход :)'

  [row, col] = list ( map (int, (ls ) ) )

  if field_[row] [col] != ' ':
     return 'Клетка занята! ¯\_(ツ)_/¯ Сделайте другой ход. '
  else: return 'ok'


def check_win ( xo, field_ ):
  '''Проверка выигрыша крестиков или ноликов. 1й аргумент - символ, 2й - игровое поле
      в виде списка из 3 списков по 3 элемента - символа;
      возвращает True в случае выигрыша, False - при отсутствии выигрышной комбинации'''
    
  is_rows = list ( map (all, [ [ c == xo for c in s ] for s in field_ ] ) )
 
  field_t = [ [ s[i] for s in field_ ] for i in range (3) ]
  is_cols = list ( map (all, [ [ c == xo for c in s ] for s in field_t] ) )
 
  is_diag_1 = [ field_ [ i ] [ i ] == xo for i in range (3) ]
 
  is_diag_2 = [ field_ [ i ] [ 2 - i ] == xo for i in range (3) ]
    
  if any ( is_rows ):  #проверяем выигрыш по строкам
    return True
  elif any ( is_cols ): #проверяем выигрыш по столбцам
    return True
  elif all (  is_diag_1  ): #проверяем выигрыш по главной диагонали
    return True
  elif all (  is_diag_2  ): #проверяем выигрыш по побочной диагонали
    return True
  else: return False


def is_final ( field_ ):
  ''' Проверка, сделан ли последний ход: True, если сделан; False - если нет'''

  f = []
  for s in field_: f += s #разворачиваем игровое поле в "простой" список                
  return all ( [ c != ' ' for c in f ] )

#============================================================================
def game_core_v1():
  print ( 'Правила игры: игроки по очереди ставят на поле крестики и нолики, \nпока одному из игроков не удастся поставить три своих значка в одну линию.' )
  print ('\nКак ходить: через пробел вводятся координаты клетки, в которую нужно поставить значок.\nНапример, если ввести 1 1, ход будет сделан в центральную клетку.\n\n' )

  symbol = {'X': 'крестики', 'O' : 'нолики'}
  xo = ('X', 'O')
  yesno = True

  while yesno:   #цикл повторной игры
    field_ = field_init ()
    field_print (field_)
  
    while True:   #игровой цикл
      for i in range (2):

        print ( f'\n\nХодят { symbol.get ( xo [ i ] ) }:' )
 
        while True: #проверка корректности ввода
          move_str = input ()
          if check_valid_move ( move_str, field_ ) == 'ok':
            break
          else:
            print ( check_valid_move ( move_str, field_ ) )
    
        [row, col] = list ( map (int, ( move_str.split () ) ) )
        field_ [row] [col] = xo[i]

        field_print ( field_ )

        if check_win (xo [ i ], field_):
          print ( f"\n\nВыиграли { symbol.get ( xo [ i ] ) }!" )
          return None   #выход из цикла в случае выигрышного хода

        if is_final (field_):
          print ( '\n\nНичья!' )
          return None   #выход из цикла в случае конца игры

    print ('Хотите сыграть ещё? (y/n)')
    yesno = input() == y
game_core_v1()