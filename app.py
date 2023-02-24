from barfi import st_barfi, barfi_schemas, Block
import streamlit as st

from barfi import Block




add = Block(name='Addition')
add.add_input(name='my input')
sub = Block(name='Subtraction')
mul = Block(name='Multiplication')
div = Block(name='Division')

barfi_result = st_barfi(base_blocks= {'Op 1': [add, sub], 'Op 2': [mul, div]})
