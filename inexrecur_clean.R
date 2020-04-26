#!/usr/bin/env Rscript
#EJERCICIO: ALGORITMO BWA-INEXRECUR DE HENG LI Y RICHARD DURBIN
#COMPLETA LAS LINEAS CON EL TAG #COMPLETAR
#INVOCA LA FUNCION "INEXRECUR" RECURSIVAMENTE PARA RESOLVER EL ALGORITMO
#ACUMULA LAS SOLUCIONES OBTENIDAS EN LAS RECURSIONES MEDIANTE LA FUNCIÓN "union"

C <- function(a) {

  components <- gsub("[[:punct:]]","",X)
  components <- strsplit(components,"")
  components_sorted <- sort(components[[1]])
  idx <- min(which(components_sorted == a))
  C_num <- idx-1
  return(C_num)

}

O <- function(a,i) {

  ## To match with the real algorithm
  i<-i+1

  ## Find coincidences in B vector
  coincidences <- grep(a,B)
  ## Count number of coincidences (i starts at 1)
  counter <- i>=coincidences
  O_num <- length(counter[counter==TRUE])
  return(O_num)

}

INEXRECUR <- function(W,i,z,k,l,sep) {
  #print(paste("i: ",i," z: ",z))
  ## INPUTS
  # W = Subsecuencia a alinear con X
  # i = Posici?n
  # z = Permited errors
  # k = L?mite inferior del intervalo SA
  # l = L?mite superior del intervalo SA
  ## OUTPUTS
  # I = Alineamientos obtenidos

####################### CUERPO PRINCIPAL ####################

  if (i<0){
    if (z<0) {
      return({})
    }
    else {
      result <- list(c(k,l))
      return(result)
    }
  }
  if (z<D[i+1]) {
    return({})
  }

  I <- {}
  I <- c (I, INEXRECUR(W,i-1,z-1,k,l,sep));#COMPLETAR DELECION


  for (bi in b){
    ki <- C(bi) + O(bi,k-1) + 1  #Precalculate C and O function
    li <- C(bi) + O(bi,l)  #Precalculate C and O function
    if (ki<=li){
      I <- c (I, INEXRECUR(W,i,z-1,ki,li,sep));  #COMPLETAR INSERCION
      if (bi==W[[1]][i+1]){
        I <- c (I, INEXRECUR(W,i-1,z,ki,li,sep))   #COMPLETAR MATCH
      }else{
        I <- c (I, INEXRECUR(W,i-1,z-1,ki,li,sep)) #COMPLETAR SUSTITUCION
      }
    }
  }
  return(I)

} #end INEXRECUR

#ejemplo con busqueda de W="lol" en X="googol$"
X <- "googol$"

#### OBTENER SUFIXARRAY DE X

SA_pre <- c()
SA_pre[1] <- X
for (i in 2:nchar(X)){
  SA_pre[i] <- paste(substring(X,i,nchar(X)),substring(X,1,i-1),sep='',collapse=NULL)
}
SA_list<-sort(SA_pre,index.return=TRUE)
SA<-SA_list$x
S<-SA_list$ix
B<-paste(substring(SA,nchar(X),nchar(X)),sep='',collapse=NULL)


########################## INPUTS ###########################

b <- c("g","l","o")


D <- c(0,0,1)
W = list(c("l","o","l"))
i = 2
z = 1
a = INEXRECUR(W,i,z,0,6,"")
print (a)
