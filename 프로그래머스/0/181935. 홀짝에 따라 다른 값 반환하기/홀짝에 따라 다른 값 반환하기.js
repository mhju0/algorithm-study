function solution(n) {
    const ifOdd = (n % 2 !== 0);
    let sum = 0;
    //홀수 시나리오
    if (ifOdd){
        for (i=1; i <=n; i += 2){
            sum += i;
        }
    }else{
        //짝수 시나리오
        for (i=2; i <=n; i += 2){
            sum += i**2;
        }
    }
    return sum;
}