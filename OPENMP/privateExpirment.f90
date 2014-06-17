program privateExperiment
	! private
	! Expirement with firstprivate and lastprivate directives of OpenMP
	! uwhspc
	use omp_lib
	implicit none
	real(kind=8) :: y
	integer :: n
	integer :: i, nthreads
	real(kind=8), dimension(10000) :: x
	n = 1000
	
	
	nthreads = 3
	!$ call omp_set_num_threads(nthreads)
	!$ print "('Using OpenMP with ',i3,' threads')", nthreads
	
	y = 2.d0
	!$omp parallel do firstprivate(y) lastprivate(y) if (n > 1000)
	do i=1,n
		y = y + 10.d0
		x(i) = y
		!omp critical
		print *, "i = ",i,"  x(i) = ",x(i)
		!omp end critical
	enddo
	
	print *, "At end, y = ", y





end program privateExperiment