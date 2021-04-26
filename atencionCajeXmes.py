nom_caje=[]
hrs_aten=[]
nombreMes=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre',
           'octubre','noviembre','diciembre']
while True:
    nom_caje.append(input("ingrese nombre del cajero: "))
    desea_continuar=input("desea continuar si o no ")
    desea_continuar=desea_continuar.lower()
    if(desea_continuar=='no'):
        break
for i in range(len(nom_caje)):
    print("cajero: ",nom_caje[i] )
    hrs_aten_xcajero=[]
    for j in range(12):
        hrs_aten_xcajero.append(input("ingrese horas de atencion del mes: "+nombreMes[j]+":"))
    hrs_aten.append(hrs_aten_xcajero)


for i in range(len(nom_caje)):
    for j in range(12):
        print(hrs_aten[i][j],end='')
    print("\n")

print(hrs_aten[0][1])

def totalAnualHoraXCajero():

    for i in range (len(nom_caje)):
        sum = 0
        for j in range(12):
            sum=sum+int(hrs_aten[i][j])
        print("cajero: ",nom_caje[i],"suma anual: ",sum)

def totalMensuaTodosCajero():

    for i in range (12):
        sum = 0
        for j in range(len(nom_caje)):
            sum=sum+int(hrs_aten[j][i])
        print("total meS : ",nombreMes[i]," de todos los cajeros : ",sum)

def nombreytotalCajeroMasHorasAnuales():
    totalAnualXcajero=[]
    for i in range (len(nom_caje)):
        sum = 0
        for j in range(12):
            sum=sum+int(hrs_aten[i][j])
        totalAnualXcajero.append(sum)
    mayor = 0
    for j in range(len(nom_caje)):

        if totalAnualXcajero[j]>mayor:
            mayor=totalAnualXcajero[j]
            posicion=j
    print("cajero con mas horas anuales es : ",nom_caje[posicion],", suma anual: ",mayor)



def mesMasHorasTrabajadas():
    listaTotalesXMes=[]
    for i in range (12):
        sum = 0
        for j in range(len(nom_caje)):
            sum=sum+int(hrs_aten[j][i])
        listaTotalesXMes.append(sum)
    mayor = 0
    for j in range(12):

        if listaTotalesXMes[j]>mayor:
            mayor=listaTotalesXMes[j]
            posicion=j
    print("el mes con mas horas trabajadas es : ",nombreMes[posicion]," , suma: ",mayor)

totalAnualHoraXCajero()
totalMensuaTodosCajero()
nombreytotalCajeroMasHorasAnuales()
mesMasHorasTrabajadas()