function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%

##for k = 1 : num_labels,
##    J = 1 / m * sum((-y)' .* log(sigmoid(X * nn_params)) - (1 - y)' .* log(1 - sigmoid(X * nn_params)))
##J = (1/m) * (-y'*log(sigmoid(X*nn_params)) - (1-y)'*log(1-sigmoid(X*nn_params))) + lambda / (2*m) * sum(nn_params(2:end).^2);

a1 = [ones(m, 1) X];
z2 = a1 * Theta1'; % use the Theta 1 and 2, which reshape from the unrolled vector nn_params.
a2 = sigmoid(z2);
a2 = [ones(m, 1) a2];
z3 = a2 * Theta2';
h = sigmoid(z3); % sigmoid(sigmoid([ones(m, 1) X] * Theta1') * Theta2')

y_k = zeros(m, num_labels); % 封装 yk，主要问题是如何表示yk
for i = 1:m
    y_k(i, y(i)) = 1;
end

J = (1 / m)* sum(sum((-y_k) .* log(h) - (1 - y_k) .* log(1 - h)));


##for j = 1 : 25,
##    for k = 1 : 400,
##        s_T1 = sum(Theta1(j, k) .^ 2)
##    end
##end
##  
##for j = 1 : 10,
##    for k = 1 : 25,        
##        s_T2 = sum(Theta2(j, k) .^ 2)
##    end    
##end

##r = lambda / (2 * m) * (sum(s_T1) + sum(s_T2))
r = (lambda / (2 * m)) * (sum(sum(Theta1(:, 2:end) .^ 2)) + sum(sum(Theta2(:, 2:end) .^ 2)));
J = J + r


for t = 1 : m,
    a1 = [1 X(t, :)]';
    z2 = Theta1 * a1;
    a2 = sigmoid(z2);
    a2 = [1; a2];
    z3 = Theta2 * a2;
    a3 = sigmoid(z3);
    
    z2 = [1; z2];
    delta3 = a3 - y_k'(:, t);
    delta2 = (Theta2' * delta3) .* sigmoidGradient(z2);
    delta2 = delta2(2:end); % removing delta2_0
    
    Theta1_grad = Theta1_grad + delta2 * a1';
    Theta2_grad = Theta2_grad + delta3 * a2';
    
end

% Update our new delta matrix
Theta1_grad = (1 / m) .* (Theta1_grad)
Theta1_grad(:, 2:end) = Theta1_grad(:, 2:end) + (lambda / m) * Theta1(:, 2:end);

Theta2_grad = (1 / m) .* (Theta2_grad)
Theta2_grad(:, 2:end) = Theta2_grad(:, 2:end) + (lambda / m) * Theta2(:, 2:end);


% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
