

# CMPS 2200 Assignment 1

**Name:**Zach Goodman


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.

Yes it is. This is because $2^{n+1}$ simplifies to $2*2^n$. Since we ignore constants, this can be looked at as $2^n$ which is in $O(2^n)$.
.  
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  
$2^{2^n}$ is not in $O(2^n)$ because $2^{2^n}$ simplifies to $4^n$ which obviously grows faster than $2^n$. Since there is no value C where $2^{2^n} <= C*(2^n)$, $2^{2^n}$ is not in $O(2^n)$.
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
. 
$n^{1.01}$ is not in $O(\mathrm{log}^2 n)$ because since polynomial functions grow faster than logarithmic functions, $n^{1.01}$ grows faster than $O(\mathrm{log}^2 n)$. Furthermore, there is no constant value C where $n^{1.01} <= C(\mathrm{log}^2 n)$.
.  
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  
$n^{1.01}$ grows faster than $Omega(\mathrm{log}^2 n)$. Since this is the case, yes $n^{1.01} \in \Omega(\mathrm{log}^2 n)$.
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  
Similar to 1c, $\sqrt{n}$ is a polynomial function, and polynomial functions increase faster than logarithmic functions, which is what $O((\mathrm{log} n)^3)$ is. Also, since there is no constant C where $\sqrt{n} <= C((\mathrm{log} n)^3)$, $\sqrt{n}$ is NOT in $O((\mathrm{log} n)^3)$.
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
Yes. Similar to 1d, since $\sqrt{n}$ grows faster than $Omega((\mathrm{log} n)^3)$, $\sqrt{n}$ is in $Omega((\mathrm{log} n)^3)$.


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  This function recursively calculates to find the xth Fibonacci number. If x is 0 or 1, it returns x, which is the base case. This is because 0 and 1 are the first two numbers in the Fibonacci sequence. Otherwise, it recursively calls on itself until the base case as been reached, but while doing that, it is updating the variables ra and rb and returning the sum of ra+rb, which is how the Fibonacci number is obtained.
.  
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  The work is O(n) because the function linearly iterates through the list. Since it is not being run in parallel, the span is also O(n).
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  
.  
.  Even though the function makes recursive calls, it splits the list into two and only considers each element once. Therefore the work is O(n).

Since this function is not parallelized, the span is also O(n).
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  In this case, it doesn't matter how many threads are used because each element still must be considered once. Therefore, work is still O(n)


However, now since the function is parallelized, the span is equivalent to the depth of the recursion tree. This means the span will be O(log(n))
.  
.  
.  
.  
.  
.  

