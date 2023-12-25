# TRAVAIL PRATIQUE DE CRYPTOGRAPHIE ET SECURITE INFORMATIQUE en Python
# CALCUL DU PLUS GRAND COMMUN DIVISEUR PAR L'ALGORITHME D'EUCLIDE

a = int(input("Inserer le premier nombre:"))
b = int(input("Inserer le deuxième nombre:"))

def pgcd(a,b):

    if a>b:
        r1=a
        r2=b

    else:
        r1=b
        r2=a

    while r2!=0:
        c=r1%r2
        r1=r2
        r2=c

    return r1

print("le plus grand commun diviseur de "+str(a)+" et de "+str(b)+" est: "+str(pgcd(a,b)))




# CALCUL DU PLUS GRAND COMMUN DIVISEUR PAR L'ALGORITHME D'EUCLIDE ETENDU

a = int(input("Inserer  le premier nombre:"))
b = int(input("Inserer le deuxième nombre:"))
 
def pgcd(a,b):

    s1=1
    s2=0
    t1=0
    t2=1
    s=0
    t=0

    if a==0 or b==0:
        if a==0 and b!=0:
            print("le plus grand commun diviseur vaut "+str(b)+" la valeur de s est 1\n la valeur de t est 1") 
        elif a!=0 and b==0:
            print("le plus grand commun diviseur vaut "+str(a)+" la valeur de s est 1\n la valeur de t est 1") 
        else:
            print("le plus grand commun diviseur vaut "+str(a)+" la valeur de s est 1\n la valeur de t est 1")
    else:    
        if a>b:
            r1=a
            r2=b
            r=r1%r2
        else:
            r1=b
            r2=a
            r=r1%r2
        while r2!=0:
        #calcul du quotient
            q=r1//r2
        #calcul de s et t
            s=s1-q*s2
            t=t1-q*t2
    #Mise à jour des valeurs de r1, r2, s1, s2, t1, t2

        #Mise à jour des r1, r2
            r=r1%r2
            r1=r2
            r2=r
        #Mise à jour des s1, s2    
            s1=s2
            s2=s
         #Mise à jour des t1, t2 
            t1=t2
            t2=t
        if a>b:
            print("le plus grand commun diviseur de "+str(a)+" et de "+str(b)+" par l'algorithme d'Euclide étendu est: "+str(r1)+"\n La valeur de s est: s="+str(s1)+"\n Et la valeur de t est: t="+str(t1))
        else:
            print("le plus grand commun diviseur de "+str(a)+" et de "+str(b)+" par l'algorithme d'Euclide étendu est: "+str(r1)+"\n La valeur de s est: s="+str(t1)+"\n Et la valeur de t est: t="+str(s1))
print(pgcd(a,b))