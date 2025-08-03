from Class_simplexe import Simplex
import pytest 

def test_data_ingestion():
    s1 = Simplex()
    s1.read_data('data.txt')
    assert s1.number_constraint == len(s1.bound)
    

def test_len_constraint_matrix():
    s2 = Simplex()
    s2.read_data('data.txt')
    assert len(s2.obj_cost) == len(s2.cost_constraint[0])
    
def test_constraint_number_matrix():
    s2 = Simplex()
    s2.read_data('data.txt')
    assert s2.cost_constraint[0][1] == 1.0
    assert s2.cost_constraint[2][1] == 1.0
    
def test_index_choosen():
    s2 = Simplex()
    s2.read_data('data.txt')
    s2.choose_input_variable()
    assert s2.index_choosen == 0
