function solution(num_list) {
    let multiple = 1;
    let sum = 0;
    for (let i=0; i<num_list.length;i++){
        multiple *= num_list[i];
        sum += num_list[i];
    }
    const squareOfSum = sum ** 2;
    return multiple < squareOfSum ? 1 : 0;
}