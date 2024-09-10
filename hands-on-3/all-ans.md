2:Time this function for various n e.g. n = 1,2,3.... You should have small values of n all the way up to large values. Plot "time" vs "n" (time on y-axis and n on x-axis). Also, fit a curve to your data, hint it's a polynomial

![image](https://github.com/user-attachments/assets/9d45865e-a96b-415e-b4b9-c8c3cbe50e32)

3:Find polynomials that are upper and lower bounds on your curve from #2. From this specify a big-O, a big-Omega, and what big-theta is.
Ans:-To find upper and lower bounds, we can fit polynomials to the data 
and use them to determine Big-O, Big-Omega, and Big-Theta.
 Fit polynomial curve
 
p = polyfit(n_values, times, 2);

fitted_curve = polyval(p, n_values);

 Plot the fitted curve
hold on;

plot(n_values, fitted_curve, 'r-', 'LineWidth', 2);

legend('Data', 'Fitted Curve');

 Display the polynomial coefficients
disp('Polynomial Coefficients:');

disp(p);

Now, to find the upper and lower bounds, we can use the coefficients 
of the fitted polynomial. Let's say the polynomial is of the form 
ax^2 + bx + c.

Upper Bound (Big-O): The highest degree term dominates the function. 
So, the upper bound is O(n^2).

Lower Bound (Big-Omega): The lowest degree term dominates the 
function. So, the lower bound is Ω(n^2).

Big-Theta: Since upper and lower bounds are the same, Big-Theta is 
Θ(n^2)
