## About this code
This code is a solver I did for a college project. The idea was to be able to simulate all the possible physical scenarios, independent of dimensions, using only the lagrangian of the system ant it's associated Euler-Lagrange equations.

## Usage
To use the solver, simply install the package via pip or import via downloading the script given in the release, and call one of the solver functions (mainly elSolver)

The lagrangian of the system you wish to simulate has to be in the format given in the examples in the file

## Method used
I'll try to explain a bit the maths behind the method. We start from the Euler-Lagrange equations for a n-dimensional system. The E-L equation for the i-dimension will be:


```math
\frac{\partial L}{\partial q_i} - \frac{\text{d}}{\text{d}t}\frac{\partial L}{\partial \dot{q}_i} = 0
```

If we apply the chain rule to the time derivative, we get:

```math
\frac{\partial L}{\partial q_i} - \left(\sum_{j=1}^n\frac{\partial^2 L}{\partial \dot{q}_i \partial q_j}\dot{q_j} + \frac{\partial^2 L}{\partial \dot{q}_i\dot{q}_j}\ddot{q_j}\right) = 0
```
Where $j$ spans all the different dimensions of the system. Now, our objective is to get all the $\ddot{q}_j$. We can do this if we express this equation as a linear system of equations, if we consider each row to be one of the i-dimension equation, and the columns to be the summation in $j$.
```math
\begin{array}{l}
\sum_{j=1}^n \frac{\partial^2 L}{\partial \dot{q}_1\dot{q}_j} \ddot{q_j} = \frac{\partial L}{\partial q_1} - \sum_{j=1}^n\frac{\partial^2 L}{\partial \dot{q}_1 \partial q_j}\dot{q_j}
\\
\sum_{j=1}^n \frac{\partial^2 L}{\partial \dot{q}_2\dot{q}_j} \ddot{q_j} = \frac{\partial L}{\partial q_2} - \sum_{j=1}^n\frac{\partial^2 L}{\partial \dot{q}_2 \partial q_j}\dot{q_j}
\\
\vdots
\\
\sum_{j=1}^n \frac{\partial^2 L}{\partial \dot{q}_n\dot{q}_j} \ddot{q_j} = \frac{\partial L}{\partial q_n} - \sum_{j=1}^n\frac{\partial^2 L}{\partial \dot{q}_n \partial q_j}\dot{q_j}
\end{array}
```

For each iteration in time, we can obtain all the $`\frac{\partial^2 L}{\partial \dot{q}_i\dot{q}_j}`$, $`\frac{\partial L}{\partial q_i}`$ and $`\sum_{j=1}^n\frac{\partial^2 L}{\partial \dot{q}_1 \partial q_j}\dot{q_j}`$ with relative ease. Then, we can solve the linear equations system to get $`\ddot{q}_j`$ for all dimensions, an then, use methods to get the next point in time for the position and velocity.

## About the future
The only piece of code uploaded now is the solver, with some silly examples, but it can tackle some more complex cases (I'll try to upload some in the future). Although in some systems, it's not able to work at all, for unspecified reasons. If any of the people who download it find something interesting about it, let me know!
