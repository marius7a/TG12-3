class ListStatistik:
    
    # Die __init__-Methode nimmt eine Liste von Zahlen entgegen.
    def __init__(self, data_list):
        self.data_list = data_list
    
    # ermittelt den größten Wert aus der Liste    
    def list_max(self):
        return max(self.data_list) 
    
    # ermittelt den kleinsten Wert aus der Liste
    def list_min(self):
        return min(self.data_list) 
    
    # ermittelt die Summe aller Elemente aus der Liste
    def list_sum(self):
        return sum(self.data_list) 
    
    # ermittelt den Mittelwert aller Elemente aus der Liste
    def list_mean(self):
        
            return sum(self.data_list) / len(self.data_list)
        
    
    # ermittelt den Median aller Elemente aus der Liste
    # D.h. Alle Werte werden der Größe nach sortiert.
    # Bei ungerader Anzahl von Elementen wird das mittlere aller Elemente zurück gegeben
    # Bei gerader Anzahl von Elementen wird der Mittelwert der beiden mittleren Elemente zurück gegeben.
    def list_median(self):
        sorted_list = sorted(self.data_list)
        n = len(sorted_list)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_list[mid - 1] + sorted_list[mid]) / 2.0
        return sorted_list[mid]

# Testbeispiel:
numbers = [1, 12, -5, -23, 19, 7]
print(numbers)                      # [1, 12, -5, -23, 19, 7]
numbers_sorted = numbers.copy()     # Kopie mit allen Elementen
numbers_sorted.sort()
print(numbers_sorted)               # [-23, -5, 1, 7, 12, 19]

ls = ListStatistik(numbers)
print("Max: ", ls.list_max())       # Max:  19
print("Min: ", ls.list_min())       # Min:  -23
print("Sum: ", ls.list_sum())       # Sum:  11
print("Mean: ", ls.list_mean())     # Mean:  1.8333333333333333
print("Median: ", ls.list_median()) # Median:  4.0
