import re 

class Simplex:
    
    def __init__(self) -> None:
        self.obj_cost = []  
        self.cost_constraint = []
        self.lower_bound = []
        
        
            
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
        self.obj_cost = self.checknumber(lines,1)[0]
        print("price: ", self.aggregator_price)
        self.time_list = self.checknumber(lines,3)
        print("time_list", self.time_list)
        self.revenu_list = self.checknumber(lines,5)
        print("revenu_list", self.revenu_list)
        self.aggregator_quantity = self.checknumber(lines,7)
        print (self.aggregator_quantity)
        self.nb_player = len(self.revenu_list)