function solution(a, b) {
    var answer = 0;
    let num1 = parseInt(a+''+b);
    let num2 = 2*a*b;
    return Math.max(num1,num2)
}