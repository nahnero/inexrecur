/* Started Mon 30 Mar 17:37:57 2020 by nahnero. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

       void setup (char* X1, char* W1, char* dic1, int z);
static void InexRecur  (char* W, int i, int z, int k, int l, int d);
static void CalculateD (char* W);
static int  O          (char a, int i);
static int  C          (char a);
static void sort       (char* arr[], int n);

static char *X;
static char *W;
static char *dic;
static char *Xs; /* Xsorted */
static char *X2;
static char *B;
/* static int  *S; */
static int  *D;
static char **BWT;
static int  Wlen;
/* int  out[2]; */


int main (void){
	printf ("\t\t   Mutation  i  z  k  l\n");
	setup ("googol$", "lol", "glo", 1);
	/* setup ("googol$", "goog", "glo", 0); */
	/* setup ("googol$", "gool", "glo", 1); */
	return 0;
}


void setup (char* X1, char* W1, char* dic1, int z){

	int i, length; i = length = 0;
	X     = X1;
	/* reverse */
	W     = W1;
	while (W1[++i]);
	Wlen  = i;
	dic   = dic1;

	while (X[++length]);

	D   = (int*)  calloc (length, sizeof (int));
	BWT = (char**)calloc (length, sizeof (char*));
	Xs  = (char*) calloc (length, sizeof (char));
	B   = (char*) calloc (length, sizeof (char));
	X2  = (char*) calloc (2*length+1, sizeof (char));
	for (i = 0; i != length; i++)
		BWT[i] = (char*)malloc (length*sizeof (char) + 2);

	sprintf (X2, "%s%s", X, X);

	for (i = 0; i != length; i++)
		sprintf (BWT[i], "%.*s", (int)length, X2+i);

	sort (BWT, length);
	/* CalculateD (W1); */
	D[0] = 0; D[1] = 0;
	D[2] = 0; D[3] = 1;

	for (i = 0; i != length; i++) B [i] = BWT[i][length-1];
	for (i = 0; i != length; i++) Xs[i] = BWT[i][0];

	i = 0; while (X[++i]);
	InexRecur (W1, Wlen - 1, z, 0, i - 1, 1);

	free (D); free (Xs);
	free (B); free (X2);
	for (i = 0; i != length ; i++) free (BWT[i]);
	free (BWT);
}

static int myCompare(const void* a, const void* b){
	return strcmp (*(const char**)a, *(const char**)b);
}

void sort(char* arr[], int n){
    	qsort (arr, n, sizeof(char*), myCompare);
}

int C (char a){
	int i = 0;
	while (X[++i]) if (Xs[i] == a) return i - 1;
	return 0;
}

int O (char a, int i){
	int acc = 0, j;
	for (j = 0; j <= i; j++) {
		if (B[j] == a) acc++;
	}
	return acc;
}

/* Ignacio Amat */

void CalculateD (char* W){
	short z = 0, j = 0, i;
	char buf[BUFSIZ] = {'\0'};
	extern int Wlen;
	for (i = 0; i != Wlen; i++){
		sprintf (buf, "%.*s", i, W+j);
		if (!strstr (X, buf)){
			z++;
			j = i + 1;
		}
		D[i] = z;
	}
}

void InexRecur (char* W, int i, int z, int k, int l, int depth){
	if (i < 0){
		if (z < 0){
			return;
		} else {
			printf ("-------------------"
				" {%d,%d} "
				"-------------\n", k, l);
			return;
		}
	}
	if (z < D[i]){return;}
    	printf ("%*sDeletion\r\t\t     [%c]    %2d %2d %2d %2d\n",
            depth, " ", W[i], i-1, z-1, k, l);
	InexRecur (W, i-1, z-1, k, l, depth + 1);
	int ki, li, m;
	for (m = 0; m != 3; m++){
		ki = C (dic [m]) + O (dic [m], k-1) + 1;
		li = C (dic [m]) + O (dic [m], l);
		if (ki <= li){
    	printf ("%*sInsertion\r\t\t     [%c]    %2d %2d %2d %2d\n",
            depth, " ", dic[m], i, z-1, ki, li);
			InexRecur (W, i, z-1, ki, li, depth + 1);
			if (dic [m] == W[i]){
    	printf ("%*sMatch\r\t\t     [%c]    %2d %2d %2d %2d\n",
            depth, " ", dic[m], i-1, z, ki, li);
				InexRecur (W, i-1, z, ki, li, depth + 1);
			} else {
    	printf ("%*sSubstitution\r\t\t [%c] -> [%c] %2d %2d %2d %2d\n",
            depth, " ",dic[m], W[i], i-1, z-1, ki, li);
				InexRecur (W, i-1, z-1, ki, li, depth + 1);
			}
		}
	}
	return;
}
