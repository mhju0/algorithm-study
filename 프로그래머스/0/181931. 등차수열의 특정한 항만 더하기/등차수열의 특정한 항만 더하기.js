function solution(a, d, included) {
    let value = a;
    let sum = 0;
    for (let i=0; i < included.length; i++){
        value = a + (d * i);
        sum += included[i] === true ? value : 0;
    }
    return sum;
}