% 1/8 th mask
Z=[0	1	2	0	3	4	0	5	6
0	7	8	9	10	11	12	13	14
0	0	15	16	17	18	19	20	21
0	0	0	0	22	23	0	24	25
0	0	0	0	26	27	28	29	30
0	0	0	0	0	0	31	32	33
0	0	0	0	0	0	34	35	36
0	0	0	0	0	0	0	37	38
0	0	0	0	0	0	0	0	39
];
%quarter
[n,m]=size(Z);
A=Z'+Z;
A(1:n+1:end)=diag(Z);
B = rot90(A);
C = rot90(B);
D = rot90(C);
% full
mask=zeros(2*n-1,2*n-1);
mask(1:n,1:n)=C;
mask(1:n,n:end)=B;
mask(n:end,1:n)=D;
mask(n:end,n:end)=A;
NX=2*n-1;NY=2*n-1;
clear A B C D Z n m



