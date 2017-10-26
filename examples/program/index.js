function increment(n) {
  return n + 1;
}

exports.increment = increment;

if (require.main === module) {
  console.log(increment(1));
}
