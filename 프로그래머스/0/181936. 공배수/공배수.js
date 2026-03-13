function solution(number, n, m) {
    const divisibleByN = (number % n === 0);
    const divisibleByM = (number % m === 0);
    const divisibleByNM = divisibleByN && divisibleByM ? 1 : 0;
    return divisibleByNM
}