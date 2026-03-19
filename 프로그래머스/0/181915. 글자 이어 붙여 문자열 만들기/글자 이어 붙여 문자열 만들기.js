function solution(my_string, index_list) {
    let answer = ""
    for (const n in index_list){
        answer += my_string[index_list[n]];
    }
    return answer;
}