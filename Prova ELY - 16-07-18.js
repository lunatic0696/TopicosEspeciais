//Questão 1
function q1(){
var firstName = "Ermeson";
var interest = "manga";
var hobby = "read books";

var awesomeMessage = "Hi, my name is " + firstName + ". I love " + interest + ". In my spare time, I like to " + hobby + "."
console.log(awesomeMessage)
}
//Questão 2

var musicians = 1;

if (musicians <= 0) {
    console.log("not a group")
} else if (musicians === 1){
    console.log("solo")
} else if (musicians === 2){
    console.log("duet")
} else if (musicians === 3){
    console.log("trio")
} else if (musicians === 4){
    console.log("quartet")
} else{
    console.log("this is a large group")
}

//Questão 3
for (var x = 0; x <= 25; x++){
    for (var y = 0; y <= 99; y++){
        console.log(x + "-" + y)
    }
}

//Questão 4
var x = 1;

while (x <= 20) {
    var message = "";
    if (x % 3 === 0){
        message += "Julia"
    }
    if (x % 5 === 0){
        message += "James"
    }
    if (x % 5 !== 0 && x % 3 !==0){
        message += x
    }
    console.log(message);
    x+=1;
}

//Questão 5

var laugh = function(tamanho){
    var laugh = "";
    for (var x = 1; x <= tamanho; x++){
        if (x === tamanho){
            laugh += "ha!";
        }else{
            laugh += "ha";
        }
    }
    return laugh;
}

console.log(laugh(3));

//Questão 6
var numbers = [
    [243, 12, 23, 12, 45, 45, 78, 66, 223, 3],
    [34, 2, 1, 553, 23, 4, 66, 23, 4, 55],
    [67, 56, 45, 553, 44, 55, 5, 428, 452, 3],
    [12, 31, 55, 445, 79, 44, 674, 224, 4, 21],
    [4, 2, 3, 52, 13, 51, 44, 1, 67, 5],
    [5, 65, 4, 5, 5, 6, 5, 43, 23, 4424],
    [74, 532, 6, 7, 35, 17, 89, 43, 43, 66],
    [53, 6, 89, 10, 23, 52, 111, 44, 109, 80],
    [67, 6, 53, 537, 2, 168, 16, 2, 1, 8],
    [76, 7, 9, 6, 3, 73, 77, 100, 56, 100]
];

for (var x = 0; x <= numbers.length - 1; x++){
    for (var y = 0; y <= numbers[x].length - 1; y++){
        if (numbers[x][y] % 2 === 0){
            numbers[x][y] = "even";
        }else{
            numbers[x][y] = "odd";
        }
    }
}
console.log(numbers)

//Questão 7

var savingsAccount = {
 balance: 1000,
 interestRatePercent: 1,
 deposit: function addMoney(amount) {
 if (amount > 0) {
 savingsAccount.balance += amount;
 }
 },
 withdraw: function removeMoney(amount) {
 var verifyBalance = savingsAccount.balance - amount;
 if (amount > 0 && verifyBalance >= 0) {
 savingsAccount.balance -= amount;
 }
 },
 summary: function  printAccountSummary(balance,interestRatePercent){
    return "Welcome! Your balance is currently $"+this.balance+" and your interest rate is "+this.interestRatePercent+"%."
 },
 test: function test(){
    console.log(savingsAccount.summary())
    if (savingsAccount.printAccountSummary == "Welcome! Your balance is currently $1000 and your interest rate is 1%"){
        console.log("Funciona")
        return true
    }
 }
};

console.log(savingsAccount.test())