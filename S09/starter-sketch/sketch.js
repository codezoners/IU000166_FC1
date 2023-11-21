function setup() {
  createCanvas(400, 400)

  const x = 3;

  {
    const x = 11;
  }

  console.log(x);

  // Where is y?
  y = 45;
  console.log(window.y);
}

function draw() {
  background(220)
  circle(width / 2, height / 2, 300)

  console.log("HELLO")
}
