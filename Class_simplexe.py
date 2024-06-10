import re 

class Simplex:
    
    def __init__(self) -> None:
        self.number_obj = 0 
        self.number_constraint = 0 
        self.obj_cost = []  
        self.cost_constraint = []
        self.bound = []
        
        
            
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
        self.number_obj, self.number_constraint = self.checknumber(lines,1)
        print("objective number costs: ", self.number_obj)
        print("number of constraints: ", self.number_constraint)
        self.obj_cost = self.checknumber(lines,3)
        print("objective costs: ", self.obj_cost)
        self.cost_constraint = [self.checknumber(lines,i) for i in range(5, 5 + int(self.number_constraint))]
        print("cost_constraint", self.cost_constraint)
        self.bound = self.checknumber(lines, 9)
        print("bound", self.bound)

    