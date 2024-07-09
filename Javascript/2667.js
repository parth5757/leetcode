// 2667. Create Hello World Function
// Write a function createHelloWorld. It should return a new function that always returns "Hello World".
 

// Example 1:

// Input: args = []
// Output: "Hello World"
// Explanation:
// const f = createHelloWorld();
// f(); // "Hello World"

// The function returned by createHelloWorld should always return "Hello World".
// Example 2:

// Input: args = [{},null,42]
// Output: "Hello World"
// Explanation:
// const f = createHelloWorld();
// f({}, null, 42); // "Hello World"

// Any arguments could be passed to the function but it should still always return "Hello World".
 

// Constraints:

// 0 <= args.length <= 10



var createHelloWorld = function() {
    
    return function(...args) {
        return "Hello World";
    };
};

// wrong approach
// args = [{}, null, 42];
// console.log(createHelloWorld(args));


//  the other methos to run js code (right approach)

// Step 1: Invoke createHelloWorld to get the inner function
var helloWorldFunction = createHelloWorld();

// Step 2: Call the inner function (which always returns "Hello World")
console.log(helloWorldFunction());
