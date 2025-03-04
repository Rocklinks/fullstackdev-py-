let string ="Hello world";
console.log(string.length)

const numbers =[3,4,5,7,8,1,2,4,6,8]
const even = numbers.filter(num=> num%2===0);
console.log(even);

//Task3
let person ={
    firstname:"Raja",
    lastname:"Ganesh",
    name: function(){
        console.log("Hello " + this.firstname +" " +this.lastname);
    }
};

person.name();