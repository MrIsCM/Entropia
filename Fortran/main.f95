program Entropia
	implicit none

	integer, parameter :: n = 10000 	! Number of elements 
	integer, parameter :: cycles = 1E7 	! Number of cycles
	
	double precision :: k, l 		    ! Probability of transformation to 1 and 0 (respectively)

	double precision :: cell(n) 		! Array of cells
	cell = 0 						    ! Initial state of the cells 

	k = 1 
	l = 0.5 

	write(*,*) cycles

	call FTNEP(n, cycles, k, l, cell) 	! Call the Fortran subroutine

end program Entropia

subroutine FTNEP(n, ciclos, k, l, cell)
	implicit none
	integer, intent(in) :: n, ciclos
	double precision, intent(in) :: k, l
	double precision, intent(inout) :: cell(n)

	integer :: i, num(ciclos)
	double precision :: dice(ciclos), suma(ciclos)
	double precision :: aux(ciclos)

	call random_seed()
	call random_number(dice)
	call random_number(aux)

	num = int(aux * n) + 1

!open(10, file = 'data.dat', status = 'unknown')

	suma = 0.0
	do i = 1, ciclos
		if ( cell(num(i)) == 0 ) then
			if ( dice(i) < k ) then
				cell(num(i)) = 1
			end if
		else 
			if ( dice(i) < l ) then
				cell(num(i)) = 0
			end if
		end if

		suma(i) = sum(cell)
		!write(10, *) i, suma(i)
	end do
	
!close(10)

end subroutine FTNEP