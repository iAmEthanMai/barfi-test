from barfi import st_barfi, barfi_schemas, Block
import streamlit as st

from barfi import Block




add = Block(name='Addition')
sub = Block(name='Subtraction')
mul = Block(name='Multiplication')
div = Block(name='Division')

barfi_result = st_barfi(base_blocks= [add, sub, mul, div])
# or if you want to use a category to organise them in the frontend sub-menu
barfi_result = st_barfi(base_blocks= {'Op 1': [add, sub], 'Op 2': [mul, div]})
