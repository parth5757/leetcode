// /**
//  * @param {number} n
//  * @param {number} w
//  * @param {number} maxWeight
//  * @return {number}
//  */
// var maxContainers = function(n, w, maxWeight) {
//     if (n >= 1 && n <= 1000 && w >= 1 && w <= 1000 && maxWeight >= 1 && maxWeight <= 10 ** 9) {
//         let N = n * n;
//         for (i=0; i <= N; i++){
//             if(i*w == maxWeight){
//                 return i;
//             }
//         }
//     }
//     else{
//         return "Entered values crossing limits";
//    } 
// };
// n = 2, w = 3, maxWeight = 15;
// console.log("Test Case 1", maxContainers(n, w, maxWeight));
// n = 3, w = 5, maxWeight = 25;
// console.log("Test Case 2", maxContainers(n, w, maxWeight));
// n = 5, w = 20, maxWeight = 200;
// console.log("Test Case 3", maxContainers(n, w, maxWeight));
// n = 4, w = 16, maxWeight = 400;
// console.log("Test Case 4", maxContainers(n, w, maxWeight));



/**
 * @param {number} n
 * @param {number} w
 * @param {number} maxWeight
 * @return {number}
 */
var maxContainers = function(n, w, maxWeight) {
    if (n >= 1 && n <= 1000 && w >= 1 && w <= 1000 && maxWeight >= 1 && maxWeight <= 10 ** 9){
        let N = n * n;
        let possibleContainers = Math.floor(maxWeight / w);
        let Ans = Math.min(possibleContainers, N)
        return Ans
    }  else {
        return "Entered values crossing limits";
    }
};
n = 2, w = 3, maxWeight = 15;
console.log("Test Case 1", maxContainers(n, w, maxWeight));
n = 3, w = 5, maxWeight = 25;
console.log("Test Case 2", maxContainers(n, w, maxWeight));
n = 5, w = 20, maxWeight = 200;
console.log("Test Case 3", maxContainers(n, w, maxWeight));
n = 4, w = 16, maxWeight = 400
console.log("Test Case 4", maxContainers(n, w, maxWeight));
