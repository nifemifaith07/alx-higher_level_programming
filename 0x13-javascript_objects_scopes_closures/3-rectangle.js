#!/usr/bin/node
// A class Rectangle that defines a rectangle
// Has an instance method called print that prints the rectangle using the character X

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let model = '';
      for (let j = 0; j < this.width; j++) {
        model += 'X';
      }
      console.log(model);
    }
  }
}
module.exports = Rectangle;
