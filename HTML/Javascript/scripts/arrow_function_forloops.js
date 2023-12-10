let factorial = (x) => {
    let fact = 1;
    for (i = x; i > 0; i--){
        fact = fact * i
    }
    return fact;
}
let result = factorial(6);
console.log("The result is", result);