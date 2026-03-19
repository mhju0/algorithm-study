function solution(intStrs, k, s, l) {
    const answer = [];
    for (const n of intStrs){
        if (Number(n.substr(s,l)) > k) answer.push(Number(n.substr(s,l)));
    }
    return answer;
}