#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

/* 
i used this.value instead of object.value to make it more versatile 
and reusable for any other object the method is called on 
*/
function incr() {
  this.value++;
}
myObject.incr = incr;

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
