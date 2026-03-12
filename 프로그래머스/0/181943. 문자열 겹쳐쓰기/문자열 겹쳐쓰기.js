function solution(my_string, overwrite_string, s) {
    var answer = '';
    const myLength = my_string.length;
    const overwriteLength = overwrite_string.length;
    // 길이 체크
    // 0-s 까지 my_string 사용
    // s-overwrite_string.length 까지 overwrite_string 사용
    // my_string > s+overwrite_string 일 경우 my_string 다시 사용
    for (i=0; i < myLength || i < overwriteLength+s; i++){
        if (i<s){
            answer += my_string[i]
        }else{
            if (i < overwriteLength + s){
                answer += overwrite_string[i-s]
            }else if (myLength > overwriteLength + s){
                answer += my_string[i]
            }
        }
    }
    
    return answer;
}