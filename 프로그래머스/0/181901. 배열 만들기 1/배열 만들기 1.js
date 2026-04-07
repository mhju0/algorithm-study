function solution(n, k) {
    // one line code
    return new Array(n).fill(0).map((_,i) => i+1).filter(num => num % k === 0 );
}