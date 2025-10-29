# CMPS 2200 Recitation 06
## Answers

**Name:**________Maeren Hay_________________
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
for n>=2, work recurrence is W(n)=W(n-1)+W(n-2)+c
solution: W(n)=θ((1+ sqrt(5)/2)^n) = W(n) =θ^n (exponential)
- **3)**
S(n)-max(S(n-1), S(n-2))+c when n>=2
solution: S(n)=θ(n)
- **4)**
The pattern I recongize is that the counts are the fibonachi numbers themselves. This means that the most computations are happening to the smallest problems.For example while finding f5, f1 is computed 5 times (counts=5).
- **6)**
The max number of calls is 1 time for any i, therefore the work is W(n)=O(n) and the span is S(n)=O(n)
- **8)**
The max number of calls is 2 times for any i, therefore the work is W(n)=O(n) and the span is S(n)=O(n)
