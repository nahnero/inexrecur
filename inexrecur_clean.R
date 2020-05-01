#!/usr/bin/env Rscript
C <- function(a) {
  components <- gsub("[[:punct:]]","",X)
  components <- strsplit(components,"")
  components_sorted <- sort(components[[1]])
  idx <- min(which(components_sorted == a))
  C_num <- idx-1
  return(C_num)
}
O <- function(a,i) {
  i<-i+1
  coincidences <- grep(a,B)
  counter <- i>=coincidences
  O_num <- length(counter[counter==TRUE])
  return(O_num)
}

INEXRECUR <- function(W,i,z,k,l,sep) {
  if (i<0){
    if (z<0) {return({})}
    else {
      result <- list(c(k,l))
      return(result)
    }}
  if (z<D[i+1]) {return({})}
  I <- {}
  I <- c (I, INEXRECUR(W,i-1,z-1,k,l,sep));
  for (bi in b){
    ki <- C(bi) + O(bi,k-1) + 1  #Precalculate C and O function
    li <- C(bi) + O(bi,l)  #Precalculate C and O function
    if (ki<=li){
      I <- c (I, INEXRECUR(W,i,z-1,ki,li,sep));
      if (bi==W[[1]][i+1]){
        I <- c (I, INEXRECUR(W,i-1,z,ki,li,sep))
      }else{
        I <- c (I, INEXRECUR(W,i-1,z-1,ki,li,sep))
      }}}
  return(I)

} #end INEXRECUR

X <- "googol$"
SA_pre <- c()
SA_pre[1] <- X
for (i in 2:nchar(X)){
SA_pre[i] <- paste(substring(X,i,nchar(X)),
		   substring(X,1,i-1),sep='',collapse=NULL)
}
SA_list<-sort(SA_pre,index.return=TRUE)
SA<-SA_list$x
S<-SA_list$ix
B<-paste(substring(SA,nchar(X),nchar(X)),sep='',collapse=NULL)
b <- c("g","l","o")
D <- c(0,0,1)
W = list(c("l","o","l"))
i = 2
z = 1
a = INEXRECUR(W,i,z,0,6,"")
print (a)
