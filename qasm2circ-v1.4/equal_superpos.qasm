    defbox	fx,6,0,'O_{f(x)}(x, a)'

    qubit 	q0,0
    qubit 	q1,0
    qubit 	q2,0
    qubit 	...,0
    qubit 	qn,0
    qubit 	a,0

	h	q0
	h   q1
	h   q2
	h   ...
	h   qn
	fx q0,q1,q2,...,qn,a
