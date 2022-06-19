A = [  1      1     1;
      0.9    0.1    0;
       0      1    0.9]
   
b = [0; 5; 5]
##b;  % If don't have a ";" will recognzie to a command of Octave.
  
theta3_ans = [0; 0; 5]
theta3_cal = [0; 50; -50]
A1 = A(:, 1)

##cA = theta3_cal' * A
A_c = A * theta3_cal
A_a = A * theta3_ans

##theta3_o1 = [0; 5; 0]
##theta3_o2 = [0; 0; 1]
##theta3_o3 = [1; 0; 4]
##A_o1 = A * theta3_o1
##A_o2 = A * theta3_o2
##A_o3 = A * theta3_o3
##AT_o1 = A' * theta3_o1
##AT_o2 = A' * theta3_o2
##AT_o3 = A' * theta3_o3

AT_a = A' * theta3_ans