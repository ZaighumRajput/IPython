// OpenMP.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cmath>



int _tmain(int argc, _TCHAR* argv[])
{
	const int size = 256;
	double sinTable[size];

#pragma omp parallel for
	for(int n=0; n< size; ++n)
		sinTable[n] = std::sin(2 * 3.1456 * n/size);


	return 0;
}

