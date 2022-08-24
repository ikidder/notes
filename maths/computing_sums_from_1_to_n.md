# computing sums from 1 to n
https://www.khanacademy.org/computing/computer-science/algorithms/sorting-algorithms/a/analysis-of-selection-sort

How do you compute the sum `8 + 7 + 6 + 5 + 4 + 3 + 2 + 1` quickly? Here's a trick. Let's add the numbers in a sneaky order. First, let's add 8 + 1, the largest and smallest values. We get 9. Then, let's add 7 + 2, the second-largest and second-smallest values. Interesting, we get 9 again. How about 6 + 3? Also 9. Finally, 5 + 4. Once again, 9! So what do we have?

`(8+1) + (7+2) + (6+3) + (5+4) = 9 + 9 + 9 + 9 = 4 * 9 = 36`

There were four pairs of numbers, each of which added up to 9. So here's the general trick to sum up any sequence of consecutive integers:
1. Add the smallest and the largest number.
2. Multiply by the number of pairs.

## arithmetic series
sequence to sum is from 1 to n

there are n numbers
there are n/2 pairs
therefore: sum of numbers from 1 to n = (n + 1)(n / 2) = (n²/2 + n/2)