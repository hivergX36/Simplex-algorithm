import re 

class Simplex:
    
    def __init__(self) -> None:
        self.number_iteration = 0 
        self.number_obj = 0
        self.obj_function = 0
        self.cost_index_choosen = 0 
        self.number_constraint = 0 
        self.number_variables = 0 
        self.matrix = []
        self.number_spread_variables = 0
        self.number_variables_standard = 0 
        self.obj_cost = [] 
        self.obj_standard_cost = [] 
        self.cost_constraint = []
        self.matrix_cost = []
        self.bound = []
        self.input_variable = 0 
        self.output_variable = 0
        
        
            
    def checknumber(self,lignes,indice):
        ParsedList = []
        compteur1 = 0
        compteur2 = 0
        while(lignes[indice][compteur1] != "," and lignes[indice][compteur2] != ","):
              while(lignes[indice][compteur2] != ","):
                    compteur2 += 1
              print(lignes[indice][compteur1:compteur2])
              ParsedList.append(float(lignes[indice][compteur1:compteur2]))
              compteur1 = compteur2 + 1
              compteur2 = compteur1
              if compteur1 > len(lignes[indice]) - 1:
                    break
        return ParsedList
    
            
    def read_data(self,text):
        fichier = open(text, "r",encoding="utf8")
        lines = fichier.readlines()
        lines = [lines[i] for i in range(len(lines)) if lines[i] != "\n"]
        lines = [ re.sub("\n", "", lines[i]) for i in range(len(lines))]
        print("lines: ", lines)
        self.number_obj, self.number_variables, self.number_constraint = self.checknumber(lines,1)
        self.number_variables = int(self.number_variables)
        self.number_obj = int(self.number_obj)
        self.number_constraint = int(self.number_constraint)
        self.number_variables_standard = int(self.number_variables + self.number_constraint)
        self.number_spread_variables = int(self.number_constraint)
        self.obj_cost = self.checknumber(lines,3)
        self.obj_standard_cost = self.checknumber(lines,3)
        self.cost_constraint = [self.checknumber(lines,i) for i in range(5, 5 + int(self.number_constraint))]
        print("cost_constraint", self.cost_constraint)
        self.bound = self.checknumber(lines, 9)
        print("bound", self.bound)
        for i in range(self.number_spread_variables):
            self.obj_standard_cost.append(0)
        for k in range(self.number_constraint):
            for l in range(self.number_spread_variables):
                self.cost_constraint[k].append(0)
        for l in range(self.number_constraint):
            self.cost_constraint[l].append(self.bound[l])
        for m in range(self.number_constraint):
            self.cost_constraint[m][m + self.number_obj + 1] = 1
        self.obj_standard_cost.append(0)
        print("objective costs: ", self.obj_cost)
        print("objective standard costs: ", self.obj_standard_cost)
        print("self.cost_constraint: ", self.cost_constraint)


    
    def choose_input_variable(self):
        max = 0
        for i in range(self.number_variables):
            if self.obj_standard_cost[i] > max:
                max = self.obj_standard_cost[i]
                self.input_variable = i
     
                    
                    
    def choose_pivot_row(self):
        var_comparaison = 0
        min = float("inf")
        index_choosen = self.input_variable
        for j in range(self.number_constraint):
            if self.cost_constraint[j][index_choosen] > 0:
                var_comparaison = self.cost_constraint[j][-1]/self.cost_constraint[j][index_choosen]
                print("var coparison:", var_comparaison)
                if  var_comparaison < min:
                    min = var_comparaison
                    self.output_variable = j
                    
    def pivot_dictionnary(self):
        factor = self.cost_constraint[self.output_variable][self.input_variable]
        pivot = [self.cost_constraint[self.output_variable][j]/factor for j in range(self.number_variables_standard + 1)]
        for j in range(self.number_constraint):
            if j != self.output_variable:
                factor = self.cost_constraint[j][self.input_variable]
                for i in range(self.number_variables_standard + 1):
                    self.cost_constraint[j][i] -= factor * pivot[i]
        factor = self.obj_standard_cost[self.input_variable]
        for i in range(self.number_variables_standard + 1):
            self.obj_standard_cost[i] -= factor * pivot[i]
        self.cost_constraint[self.output_variable] = pivot
                    
                    
    def display_simplexe(self):
        print("Objective costs: ", self.obj_cost)
        print("Standard costs: ", self.obj_standard_cost)
        print("Cost constraints: ", self.cost_constraint)
        print("Bound: ", self.bound)
            
        
        
    def solve_simplex(self):
            iteration_number = 0
            stop = False
            while not stop: 
                print("Iteration number: ", iteration_number)
                self.choose_input_variable()
                self.choose_pivot_row()
                self.pivot_dictionnary()
                self.display_simplexe()
                if sum([self.obj_standard_cost[i] for i in range(self.number_variables)]) <= 0:
                    print("Optimal solution found")
                    stop = True
                if iteration_number > self.number_variables:
                    print("the simplex is degenerated")
                    stop = True
                iteration_number += 1

            
                
        
        
        
            
        
                    
           
                
        
        
        
            
        

    