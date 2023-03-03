# définition d'une classe Processus
class Processus:
    def __init__(self, pid, temps_arrivee, temps_execution):
        self.pid = pid
        self.temps_arrivee = temps_arrivee
        self.temps_execution = temps_execution
        self.temps_restant = temps_execution

# fonction pour exécuter un processus pour un quantum de temps
def executer_processus(processus, quantum):
    if processus.temps_restant <= quantum:
        temps_execution = processus.temps_restant
        processus.temps_restant = 0
    else:
        temps_execution = quantum
        processus.temps_restant -= quantum
    return temps_execution

# fonction pour implémenter l'algorithme Round Robin
def round_robin(processus_liste, quantum):
    temps_total = 0
    n = len(processus_liste)
    file_attente = []
    for i in range(n):
        file_attente.append(processus_liste[i])
    
    while True:
        processus_en_cours = file_attente.pop(0)
        temps_execution = executer_processus(processus_en_cours, quantum)
        temps_total += temps_execution
        for i in range(n):
            if processus_liste[i].temps_arrivee <= temps_total and processus_liste[i] not in file_attente and processus_liste[i].temps_restant > 0:
                file_attente.append(processus_liste[i])
        if processus_en_cours.temps_restant > 0:
            file_attente.append(processus_en_cours)
        if len(file_attente) == 0:
            break
    
    return temps_total

# exemple d'utilisation de l'algorithme Round Robin
processus_liste = [Processus(1, 0, 10), Processus(2, 1, 5), Processus(3, 2, 8)]
quantum = 2
temps_execution_total = round_robin(processus_liste, quantum)
print("Temps d'exécution total : ", temps_execution_total)
