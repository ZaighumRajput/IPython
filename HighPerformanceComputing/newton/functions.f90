! $UWHPSC/codes/fortran/newton/functions.f90

module functions

contains

real(kind=8) function f_sqrt(x)
    implicit none
    real(kind=8), intent(in) :: x

    f_sqrt = x**2 - 4.d0

end function f_sqrt


real(kind=8) function fprime_sqrt(x)
    implicit none
    real(kind=8), intent(in) :: x
    
    fprime_sqrt = 2.d0 * x

end function fprime_sqrt

real(kind=8) function f_objective(x)
	implicit none
	real(kind=8), intent(in) :: x
	
	f_objective = sin(x) - 1.d0 + x**x
end function f_objective

real(kind=8) function f_objectivePrime(x)
	implicit none
	real(kind=8), intent(in) :: x
	
	f_objectivePrime = cos(x) + 2.d0*x
end function f_objectivePrime


end module functions
