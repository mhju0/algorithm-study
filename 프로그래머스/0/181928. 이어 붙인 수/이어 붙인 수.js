function solution(num_list) {
    //reduce 사용 연습
    const {even, odd} = num_list.reduce((acc,cur) => {
        cur % 2 === 0 ? acc.even += cur : acc.odd += cur;
        return acc;
    }, {even: '', odd: ''});
    return Number(even) + Number(odd);
}