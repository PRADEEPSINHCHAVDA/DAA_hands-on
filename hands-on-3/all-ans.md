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

4:Find the approximate (eye ball it) location of "n_0" . Do this by zooming in on your plot and indicating on the plot where n_0 is and why you picked this value. Hint: I should see data that does not follow the trend of the polynomial you determined in #2

Ans:
![image](https://github.com/user-attachments/assets/b4fcb148-af63-4829-ad37-b0fec96acaaf)

The plot shows a clear deviation at \(n_0 = 300\), where the actual timing data starts diverging from the polynomial fit. This suggests a shift in behavior due to system limitations, overhead, or increased algorithmic complexity. By observing this point, we identify the limits of the polynomial model's accuracy. Beyond \(n_0\), the method behaves differently, indicating additional factors the model couldn't capture.

4.1:If I modified the function to be:

x = f(n)

x = 1;

y = 1;

for i = 1:n

for j = 1:n

x = x + 1;

   y = i + j;
   
 Will this increate how long it takes the algorithm to run (e.x. you are timing the function like in #2)?

Ans:

Adding y = i + j; to the nested loops introduces an additional constant-time operation inside each iteration. However, this change does not affect the overall time complexity of the algorithm, which remains O(n²) due to the nested loops. While the total execution time will increase slightly, this additional operation has a minimal impact compared to the time spent in the nested loops.

5. Will it effect your results from #1?

Ans:adding y = i + j; will not affect the overall runtime complexity of the function.
