function solution(code) {
  // code 주어짐
  let answer = "";
  let mode = 0;
  // code 차례로 읽음. 1이 나오면 mode 변화  (for loop) 사용하고 안에 if? or ? :
  for (i = 0; i < code.length; i++) {
    if (mode === 0) {
      if (code[i] === '1') {
        mode = 1;
      } else {
        if (i % 2 === 0) {
          answer = answer + code[i];
        }
      }
    } else {
      if (code[i] === '1') {
        mode = 0;
      } else {
        if (i % 2 !== 0) {
          answer = answer + code[i];
        }
      }
    }
  }
  return answer === '' ? 'EMPTY' : answer;
}