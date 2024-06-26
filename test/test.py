from ..Class_simplexe import Simplex
import pytest 

def test_data_ingestion():
    s1 = Simplex()
    s1.read_data('data.txt')
    assert s1.number_constraint == len(s1.bound)
    assert len(s1.obj_cost) == len(s1.cost_constraint[0])
    

def Constraint_matrix():
    s2 = Simplex()
    s2.read_data('data.text')
    assert s2.cost_constraint[0][1] == 2
    assert s2.cost_constraint[2][2] == 28 
    