program comparison
	! Would like to compare the speed of a parallel do loop
	! versus a normal do loop
	
	use omp_lib
	implicit none
	integer :: i, thread_num
	real(kind=8) :: t1, t2, elapsed_cpu_time_parallel
	real(kind=8) :: t3, t4, elapsed_cpu_time_normal
	integer, parameter :: n = 1000000
	real(kind=8), dimension(n) :: y
	real(kind=8) :: x

	
	
	print *, "Normal do"
	call cpu_time(t3)
	do i=1,n
		x = i
		y(i) = sin(exp(x))*cos(exp(x))*exp(sin(x))*acos(x)
	enddo
	call cpu_time(t4)
	elapsed_cpu_time_normal = t4 - t3
    print 2, elapsed_cpu_time_normal
2   format("It took the normal do loop" , f12.8, "seconds")
	
	
		
	!$ thread_num = 2
	!$ call omp_set_num_threads(thread_num)
	
	
	print *, "Parallel do loop..."
	call cpu_time(t1)
	!$omp parallel do private(x)
	do i=1,n
		x = i
		y(i) = sin(exp(x))*cos(exp(x))*exp(sin(x))*acos(x) !some complicated function
	enddo
	!$omp end parallel do
	call cpu_time(t2)
	elapsed_cpu_time_parallel = t2 - t1
	print 1, elapsed_cpu_time_parallel
1   format("It took the parallel do loop" , f12.8, "seconds")


	


end program comparison
	
