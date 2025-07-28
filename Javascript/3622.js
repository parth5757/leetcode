/**
 * @param {number} n
 * @return {boolean}
 */
var checkDivisibility = function(n) {
    digit = String(n);
    let addition = 0;
    let multiplication = 1;
    // console.log(digit, typeof(digit));
    // console.log(digit.length);
    for(i=0; i<digit.length;i++){
        // console.log(parseInt(i, 10), digit[i]) // not working
        addition = addition + Number(digit[i]);
        // console.log(addition);
        multiplication = multiplication * Number(digit[i]);
        // console.log(multiplication);
    }
    const total = addition + multiplication;
    // console.log(total, addition, multiplication);
    if(total == n){
        return true;
    } else if(total % n == 0){
        return true;
    } else{
        return false;
    }
};

const n = 99;
// console.log("Test case 1", checkDivisibility(n));
console.log(checkDivisibility(n));