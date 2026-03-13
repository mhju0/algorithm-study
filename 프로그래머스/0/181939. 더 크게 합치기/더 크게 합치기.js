function solution(a, b) {
    var answer = 0;
    answer = Math.max(`${a}${b}`, `${b}${a}`);
    return answer;
}