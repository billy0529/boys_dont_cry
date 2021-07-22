function plus (a) {
    return function (x) {
      return a + x;
    }
  }
  var plus3 = plus(3);
  var plus5 = plus(5);