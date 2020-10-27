"use strict";

let str_double_quotes = "JavaScript";
let str_single_quotes = 'programming language';

console.log("Welcome to " + str_double_quotes);
console.log("It is a " + str_single_quotes);

let str_back_sticks = `Is ${str_double_quotes} a ${str_single_quotes} ?`
console.log("String with back ticks :", str_back_sticks);

let sum = `${1+2+3}`
console.log(`The expression evaluated to a value of ${sum}.`);
console.log("The expression evaluated to a value of ${sum}.");

let sentence = "I \"love\" spinach" //include the backslash before each "" to include it
console.log("String defined with escape characters: ", sentence);

let multiline_str = 
`                    This is a 
                    String which 
                    spans multiple lines`;

console.log("A multi-line string: \n", multiline_str);

var name_str1 = "David";
var name_str2 = "David";

var name_obj1 = new String("David");
var name_obj2 = new String("David");

console.log("Type of name_str1: ", typeof name_str1)
console.log("Type of name_obj1: ", typeof name_obj1)

console.log("Is name_str1 == name_str2? ", name_str1 == name_str2);
console.log("Is name_str1 == name_obj1? ", name_str1 == name_obj1);
console.log("Is name_obj1 == name_obj2? ", name_obj1 == name_obj2);
console.log("Is the valueOf name_obj1 double equal to valueOf name_obj2? : ",
            name_obj1.valueOf() == name)name_obj2.valueOf());