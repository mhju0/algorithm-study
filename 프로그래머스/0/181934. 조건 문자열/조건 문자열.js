function solution(ineq, eq, n, m) {
    // 일단 eq 에 따라 두가지로 나누고 그 안에서 비교하기
    // >=
    // <=
    // >
    // <
    const nEqualm = (n === m);
    const nGreaterm = (n > m);
    const nLesserm = (n < m);
    if (eq === '='){
        if (ineq === '>'){
            return nEqualm || nGreaterm === true ? 1 : 0;
        }else{
            return nEqualm || nLesserm === true ? 1 : 0;
        }
    }else{
        if (ineq === '>'){
            return nGreaterm === true ? 1 : 0;
        }else{
            return nLesserm === true ? 1 : 0;
        }
    }
    
}