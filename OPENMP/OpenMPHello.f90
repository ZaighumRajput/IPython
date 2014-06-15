program test
	use omp_lib
	integer :: thread_num
	
	! How many threads do we want to use?
	!$ call omp_set_num_threads(10)
	
	print *, "Testing openmp ..."
	
	!$omp parallel
	!$omp critical
	!$ thread_num = omp_get_thread_num()
	!$ print *, "This thread = ", thread_num
	!$omp end critical
	!$omp end parallel
end program test