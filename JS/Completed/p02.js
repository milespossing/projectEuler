var output = 0;

var current = 1;
var last = 0;
while (current < 4000000){
    var temp = current;
    current = current + last;
    last = temp;
    if (current % 2 === 0) output += current;
}

console.log(output);

// Answer: 4613732