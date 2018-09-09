var output = 0;
for (i = 3; i < 1000; i++){
    if (i % 3 === 0 || i % 5 === 0) output += i;
}

document.getElementById("answer").innerText = output.toString();