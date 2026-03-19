function solution(l, r) {
    // l 과 r 사이 정수를 문자 배열로 만들기 
    // 그 배열에서 "0" "5" not includes 빼기?
    // empty [] => -1
    answer = []
    for (i=l; i <= r; i++){
        if (i.toString().split("").every(char => char === "0" || char === "5")){
            answer.push(i);
        }
    }
    return answer.length === 0 ? [-1]: answer;
}