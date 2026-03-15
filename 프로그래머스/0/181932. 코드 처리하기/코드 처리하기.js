function solution(code) {
    let answer = '';
    let mode = 0;
    for (let i = 0; i < code.length; i++){
        if(code[i] ==='1') {
            // switch mode between 1 and 0;
            mode = 1 - mode;
            // check i is even or odd using mode; 
            // mode 0 returns i is even, mode 1 returns i is odd
        } else if (i % 2 === mode) {
            answer += code[i];
        }
    }
    // Use OR logical operator because '' is false
    // Shorter than return answer === '' ? 'EMPTY' : answer
    return answer || 'EMPTY';
}