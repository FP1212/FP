'''
Created on 17/10/2019

@author: FP
'''

import array

n=0;
k=0;

rq=0;
cq=0;

ro=0;
co=0;

p=255;

limite_inferior=0;
limite_superior=100000;


direccion=8;
cuadros_restantes=0;

import re 

parametros_in=open("prueba.txt","r");
acumulador=0;

for lineas in parametros_in.readlines():    
    
    temp = re.findall(r'\d+', lineas); 
    res = list(map(int, temp));
    if acumulador==0:
        n=res[0];
        k=res[1];
        tablero=[[0 for x in range(n)]for y in range(n)];        
        obstaculos=[[0 for x in range(2)]for y in range(k)];
    elif acumulador==1:
        rq=res[0]-1;
        cq=res[1]-1;
        tablero[rq][cq]=1;
    else:
        obstaculos.append(res);
    acumulador=acumulador+1;    


parametros_in.close();

def Adir(rq,cq,i):
    return rq-i,cq 
def Bdir (rq,cq,i):
    return rq,cq-i
def Cdir (rq,cq,i):
    return rq-i,cq-i
def Ddir (rq,cq,i):
    return rq+i,cq
def Edir (rq,cq,i):
    return rq,cq+i
def Fdir (rq,cq,i):
    return rq+i,cq+i
def Gdir (rq,cq,i):
    return rq-i,cq+i
def Hdir (rq,cq,i):
    return rq+i,cq-i

direcciones={0:Adir,1:Bdir,2:Cdir,3:Ddir,4:Edir,5:Fdir,6:Gdir,7:Hdir};

detectados_direccion=array.array('B', [True] * direccion);


if n<limite_inferior:n=0;
elif n>=limite_superior:n=limite_superior;

if k<=limite_inferior:k=limite_inferior;
elif k>=limite_superior:k=limite_superior;

for i in obstaculos:    
    tablero[i[0]-1][i[1]-1]=3;    

for i in range(n):  
    
    p=int(''.join(map(str, map(int, detectados_direccion))), 2)
    
    if p==0: break;         
    
    
    for j in range (direccion):
        try:
            resultado=direcciones[j](int(rq),int(cq),int(i+1));
            bandera=detectados_direccion[j];
                        
            q=resultado[0];
            c=resultado[1];       
                
            if tablero[q][c] !=3 and tablero[q][c] !=1 and (not(q>=n or c>=n or q<0 or c<0)) and bandera==True:
                            
                tablero[q][c]=2;
                cuadros_restantes=cuadros_restantes+1;                
                
            else:
                
                detectados_direccion[j]=False;                
      
            
        except: 
            detectados_direccion[j]=False;            
                       


print("Se Encontraron ",cuadros_restantes,"Cuadros Por Los Cuales Se Puede Desplazar La Reina");
