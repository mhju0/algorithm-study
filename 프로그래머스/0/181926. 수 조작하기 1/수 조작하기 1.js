function solution(n, control) {
    let sum = n;
    for (const command of control){
        if (command == 'w') sum += 1;
        else if (command == 's') sum -=1;
        else if (command == 'd') sum +=10;
        else if (command == 'a') sum -=10;
    }
    return sum;
}