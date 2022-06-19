function [J, grad] = cofiCostFunc(params, Y, R, num_users, num_movies, ...
                                  num_features, lambda)
%COFICOSTFUNC Collaborative filtering cost function
%   [J, grad] = COFICOSTFUNC(params, Y, R, num_users, num_movies, ...
%   num_features, lambda) returns the cost and gradient for the
%   collaborative filtering problem.
%

% Unfold the U and W matrices from params
X = reshape(params(1:num_movies*num_features), num_movies, num_features);
Theta = reshape(params(num_movies*num_features+1:end), ...
                num_users, num_features);

            
% You need to return the following values correctly
J = 0;
X_grad = zeros(size(X));
Theta_grad = zeros(size(Theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost function and gradient for collaborative
%               filtering. Concretely, you should first implement the cost
%               function (without regularization) and make sure it is
%               matches our costs. After that, you should implement the 
%               gradient and use the checkCostFunction routine to check
%               that the gradient is correct. Finally, you should implement
%               regularization.
%
% Notes: X - num_movies  x num_features matrix of movie features
%        Theta - num_users  x num_features matrix of user features
%        Y - num_movies x num_users matrix of user ratings of movies
%        R - num_movies x num_users matrix, where R(i, j) = 1 if the 
%            i-th movie was rated by the j-th user
%
% You should set the following variables correctly:
%
%        X_grad - num_movies x num_features matrix, containing the 
%                 partial derivatives w.r.t. to each element of X
%        Theta_grad - num_users x num_features matrix, containing the 
%                     partial derivatives w.r.t. to each element of Theta
%

##[nm, nu] = size(R);
##sum = 0;
##
##for i = 1 : nm,
##    for j = 1 : nu,
##        if R(i, j) == 1,
##            sum = sum + ((Theta(j, :) * X(i, :)' - Y(i, j)) .^ 2);
##        endif
##    endfor
##endfor
##
##J = (1 / 2) * sum;
 
##J = (1 / 2) * sum((Theta' * X - Y(R == 1)));
##J = (1 / 2) * sum(sum((Theta' * X) .* R));

##predY = (X*Theta') .* R;
##J = 1/2 * sum(sum((predY-Y).^2)) + lambda/2 * sum(sum(Theta.^2)) + lambda/2 * sum(sum(X.^2));

##for i = 1 : num_movies
##    sum1 = zeros(1,num_features);
##    for j = 1 : num_users
##        if R(i,j) == 1
##            sum1 = sum1 + (Theta(j,:) * X(i,:)' - Y(i,j)) .* Theta(j,:);
##        end
##    end
##    X_grad(i,:) = sum1 + lambda * X(i,:);
##end
##
##for j = 1 : num_users
##    sum2 = zeros(1,num_features);
##    for i = 1 : num_movies
##        if R(i,j) == 1
##            sum2 = sum2 + (Theta(j,:) * X(i,:)' - Y(i,j)) .* X(i,:);
##        end
##    end
##    Theta_grad(j,:) = sum2 + lambda * Theta(j,:);
##end

% ͨ�����R��������ֵ�����
J = sum(sum(((X * Theta') .* R - Y .* R) .^ 2)) / 2;

X_grad = ((X * Theta') .* R - Y .* R) * Theta;
Theta_grad = ((X * Theta') .* R - Y .* R)' * X;

% ����
J += (lambda / 2) * sum(sum(Theta .^ 2)) + (lambda / 2) * sum(sum(X .^ 2));
X_grad += lambda * X;
Theta_grad += lambda * Theta;

% =============================================================

grad = [X_grad(:); Theta_grad(:)];

end