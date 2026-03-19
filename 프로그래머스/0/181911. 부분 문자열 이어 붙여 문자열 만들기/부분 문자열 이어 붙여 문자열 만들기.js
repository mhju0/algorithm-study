function solution(my_strings, parts) {
    let i = 0;
    let answer = "";
    for (const [s,e] of parts){
        answer += my_strings[i].slice(s,e+1);
        i++;
    }
    return answer
}