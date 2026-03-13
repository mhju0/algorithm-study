function solution(str1, str2) {
    var answer = '';
    // str1.(홀) str2.(짝)?
    // 조건: 길이 똑같음
    stringLength = str1.length;
    for (i=0; i < stringLength; i++){
        answer += str1[i] + str2[i];
    }
        
    return answer;
}