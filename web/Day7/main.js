//Task1
var name = "John Britto";
//let age = 25; 
//const square = 16; 

var name = "John Robinson"
let age =27;
const square = 19

//Task2 

const readline = require('readline').createInterface({
     input: process.stdin,
     output: process.stdout
 });
 readline.question("Enter your age: ", (input) => {
 const age = parseInt(input, 10);

if (age>0 && age<=12) {
    console.log("Child")
} else if (age>12 && age<=19) {
    console.log("Teenager")
} else if (age>20) {
    console.log("Adult")
} else {
    console.log("Invalid Age")
}
 readline.close();
 });

//Task3
for (let i=1;i<=10;i++){
    console.log(i);
}

let j=1;
while(j<=10){
    console.log(j);
    j++;

}

let k =1
do {
    console.log(k)
    k++
} while (k<=10)