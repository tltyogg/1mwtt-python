// Day 1

// Hours in a year. How many hours are in a year?
// const hours = 365.25*24.0;
// console.log("There are " + hours + " hours in a year.");


// Minutes in a decade. How many minutes are in a decade?

// const minutes = 365.25*24*10*60;
// console.log("There are " + minutes + " minutes in a decade.");


// Your age is seconds. How many seconds old are you?

// const age = ((365.25*24*60*36)*60)+(13*24*60*60);
// console.log("I am " + age + " seconds old!");


// Calculate @Cristina Tarantino's age in milliseconds
// const cristina = ((365.25*24*60*32)*60*1000)+(13*24*60*60*1000);
// console.log("Cristina is " + cristina + " milliseconds old!");

// Day 2

// Music A 440 Hz 1 octave is double the frequency tempered piano A' 880 Hz
// Calculate and console.log the frequency each of the 12 notes between A and A' Hint: the notes are NOT in a linear scale, but in a geometric scale


// Planets Calculate and console log how many 'minutes' the Moon travels in a day.
// Hint: first calculate how many degrees the Moons travels in the sky when the Earth returns to the same position during its daily rotation.




// Day 3

// Full name greeting. Write a program that asks for a person’s first name, then middle, and then last.
// Finally, it should greet the person using their full name.

// const fname = prompt("What is your first name?");
// const mname = prompt("What is your middle name?");
// const lname = prompt("What is your last name?");
//
// alert("Greetings " + fname + " " + mname + " " + lname + "!");


// Bigger, better favorite number. Write a program that asks for a person’s favorite number.
// Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)

// var number = prompt("What is your favorite number?");
// var bigger = parseInt(number) + 1;
//
// alert("I think you really meant " + bigger + "!");




// Angry boss. Write an angry boss program that rudely asks what you want.
// Whatever you answer, the angry boss should yell it back to you and then fire you.

// const want = prompt("What do YOU want?! ");
//
// alert('WHADDAYA MEAN \"' + want + '\"?!? YOU\'RE FIRED!!');




// Table of contents. Here’s something for you to do in order to play around more with center, ljust, and rjust:
// write a program that will display a table of contents

// console.log('Table of Contents'.center(50), "\n");
// console.log(('Chapter 1'.ljust(15)) + ('Getting Started'.center(20)) + ('page 1'.rjust(15)));
// console.log(('Chapter 2'.ljust(15)) + ('Numbers'.center(20)) + ('page 9'.rjust(15)));
// console.log(('Chapter 3'.ljust(15)) + ('Letters'.center(20)) + ('page 13'.rjust(15)));


// Day 4

// “99 Bottles of Beer on the Wall.” Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”


// var x = 99;
//
// while (x > 0) {
//   console.log( x + " bottles of beer on the Wall! " + x + " bottles of beer! Take one down, pass it around, ");
//   x = x-1;
//   console.log(x + " bottles of beer on the wall!");
// }
//
// console.log("No more bottles of beer on the wall. No more bottles of beer. Go to the store and buy some more, ");
// console.log("99 bottles of beer on the wall!");

// Deaf grandma

var greeting = prompt("Talk to Grandma : ");
var grandma = "";

function isUpperCase(str) {
  return str === str.toUpperCase();
}

function isLowercase(str) {
  return str === str.toLowerCase();
}

function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min) ) + min;
}

while (grandma == "") {
  if (isLowercase(greeting) || isUpperCase(greeting.charAt(0))) {
    alert("HUH?! SPEAK UP, GIRL!");
    count = 0;
    greeting = prompt("Talk to Grandma : ");
  }
  else if (isUpperCase(greeting) && greeting != "BYE") {
    alert("NO, NOT SINCE " + getRndInteger(1900, 1940) + "!");
    count = 0;
    greeting = prompt("Talk to Grandma : ");
  }
  else if (greeting === "") {
    alert("HUH?! SPEAK UP, GIRL!");
    count = 0;
    greeting = prompt("Talk to Grandma : ");
  }
  else if (greeting === "BYE") {
    alert("NO, NOT SINCE " + getRndInteger(1900, 1940) + "!");
    count++;
    console.log(count);
  }
  else if (count === 3) {
      alert("SEE YA!");
  }
  else {
      greeting = prompt("Talk to Grandma : ");
  }
}


// Leap years. Write a program that asks for a starting year and an ending year and then puts all the leap years between them (and including them, if they are also leap years).
// Leap years are years divisible by 4 (like 1984 and 2004).
// However, years divisible by 100 are not leap years (such as 1800 and 1900) unless they are also divisible by 400 (such as 1600 and 2000, which were in fact leap years). What a mess!





// Find something today in your life, that is a calculation. Go for a walk, look around the park, try to count something.
// Anything! And write a program about it. e.g. number of stairs, steps, windows, leaves estimated in the park, kids, dogs, estimate your books by bookshelf, toiletries, wardrobe.





// Building and sorting an array.
// Write the program that asks us to type as many words as we want (one word per line, continuing until we just press Enter on an empty line) and then repeats the words back to us in alphabetical order.
// Make sure to test your program thoroughly; for example, does hitting Enter on an empty line always exit your program? Even on the first line? And the second?





// Table of contents. Write a table of contents program here. Start the program with a list holding all of the information for your table of contents (chapter names, page numbers, and so on).
// Then print out the information from the list in a beautifully formatted table of contents. Use string formatting such as left align, right align, center.
