"use strict";

let n = 123;
console.log("Value of integer n = ", n);

n=12.345;
console.log("New value of floating point n = ", n);

console.log("145e4=", 145e4);
console.log("145e-4=", 145e-4);

console.log("20 * '20' =", 20 * "20"); //Number 20 * string 20 = 400, implicite data change was script to number
console.log("'20' * 20 = ", "20" * 20);

console.log("Infinity = ", Infinity);

console.log("POSITIVIE_INFINITY will return : ", Number.POSITIVIE_INFINITY);
console.log("1 / 0 = ", 1/0)

console.log("NEGATIVE_INFINITY will return : ", Number.NEGATIVE_INFINITY);
console.log("-1 / 0 = ", -1/0)

console.log("String divided by integer: = ", "A string" / 2);

console.log("Value of 0xEF : ", 0xEF);

var num = 16;

console.log("The binary value of 16 is :", num.toString(2));
console.log(" The octal decimal value of 16 is : ", num.toString(8));
console.log("The decimal value of 16 is : ", num.toString(10));
console.log("The hexadecimal value of 16 is : ", num.toString(16));
console.log("The duo trigesimal or base-32 value of 16 is : ", num.toString(32));

var a = 10;
console.log("Type of number before toString() :", typeof a);//number

var b = a.toString();
console.log("Type of number after toString() :", typeof b)//string

var x = 3.4567;

console.log("3.4567 rounded to 0 decimals : ", x.toFixed(0));
console.log("3.4567 rounded to 2 decimals : ", x.toFixed(2));
console.log("3.4567 rounded to 5 decimals : ", x.toFixed(5));

var y = 25.678;

console.log("Value of 25.678 without specifiying precision : ", y.toPrecision());
console.log("Value of 25.678 when precision is 2 : ", y.toPrecision(2));
console.log("Value of 25.678 when precision is 5 : ", y.toPrecision(5));

console.log("MAX_VALUE will return : ", Number.MAX_VALUE);
console.log("MIN_VALUE will return : ", Number.MIN_VALUE);