function solution(num_list) {
    const last = num_list.at(-1);
    const prev = num_list.at(-2);
    const newValue = last > prev ? last - prev : last * 2;
    num_list.push(newValue);
    return num_list
}