import csv
import matplotlib.pyplot as plt

def createPlots():
    file = "../../media/resultats/résultats_experience.csv"
    densiteAxis = []
    sizeAxis = []
    knownMethod = []
    result = {}
    try:
        with open(file, newline='\n') as csvfile:
            read = csv.reader(csvfile, delimiter=',')
            for data in read:
                readData(data,densiteAxis,sizeAxis,knownMethod,result)
    except Exception as e:
        print(e)
        print("Error reading csv file, no plot created")
        return
    
    densiteAxis.sort()
    sizeAxis.sort()
    ResultDensiteTime = {}
    ResultSizeTime = {}
    ResultDensiteError = {}
    ResultSizeError = {}
    for method in knownMethod:
        ResultDensiteTime[method] = {}
        ResultSizeTime[method] = {}
        ResultDensiteError[method] = {}
        ResultSizeError[method] = {}
        for d in densiteAxis:
            ResultDensiteTime[method][d] = []
            ResultDensiteError[method][d] = []
        for s in sizeAxis:
            ResultSizeTime[method][s] = []
            ResultSizeError[method][s] = []
            

    for method in result:
        for d,s in result[method]:
            time = result[method][(d,s)][0]
            error = result[method][(d,s)][1]
            ResultDensiteTime[method][d].append(time)
            ResultDensiteError[method][d].append(error)
            ResultSizeTime[method][s].append(time)
            ResultSizeError[method][s].append(error)

    
    for method in ResultDensiteTime:
        data = []
        for d in ResultDensiteTime[method]:
            i = ResultDensiteTime[method][d]
            l = len(i)
            data.append(sum(i)/l)
        
        plt.plot(densiteAxis,data,label=method)
        plt.xlabel('Densité')
        plt.ylabel('Temps')
        plt.title('Temps de click selon Densité de cible')
    
    plt.legend()
    plt.savefig('../../media/resultats/dens-temp.png')
    plt.show()
    
    
    for method in ResultDensiteError:
        data = []
        for d in ResultDensiteError[method]:
            i = ResultDensiteError[method][d]
            l = len(i)
            data.append(sum(i)/l)
        
        plt.plot(densiteAxis,data,label=method)
        plt.xlabel('Densité')
        plt.ylabel('Erreurs')
        plt.title("Nombre d'erreurs selon Densité de cible")
    
    plt.legend()
    plt.savefig('../../media/resultats/dens-error.png')
    plt.show()
    
    for method in ResultSizeTime:
        data = []
        for d in ResultSizeTime[method]:
            i = ResultSizeTime[method][d]
            l = len(i)
            data.append(sum(i)/l)
        
        plt.plot(sizeAxis,data,label=method)
        plt.xlabel('Taille de cible')
        plt.ylabel('Temps')
        plt.title('Temps de click selon Taille de cible')
    
    plt.legend()
    plt.savefig('../../media/resultats/size-temp.png')
    plt.show()
    
    
    for method in ResultSizeError:
        data = []
        for d in ResultSizeError[method]:
            i = ResultSizeError[method][d]
            l = len(i)
            data.append(sum(i)/l)
        
        plt.plot(sizeAxis,data,label=method)
        plt.xlabel('Taille de cible')
        plt.ylabel('Erreurs')
        plt.title("Nombre d'erreurs selon Taille de cible")
    
    plt.legend()
    plt.savefig('../../media/resultats/size-error.png')
    plt.show()


def readData(data,densiteAxis,sizeAxis,knownMethod,result):
    user = data[0]
    id = data[1]
    time = float(data[2])
    errors = int(data[3])
    t = data[4]
    d = int(data[5])
    s = int(data[6])
    if t not in knownMethod:
        knownMethod.append(t)
        result[t] = {}
    if d not in densiteAxis:
        densiteAxis.append(d)
    if s not in sizeAxis:
        sizeAxis.append(s)
    result[t][(d,s)] = (time,errors)
    
    
if __name__ == "__main__":
    createPlots()