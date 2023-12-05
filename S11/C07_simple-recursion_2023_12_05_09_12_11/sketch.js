function setup() {
  createCanvas(600, 600)
  colorMode(HSB, 1.0, 1.0, 1.0, 1.0)
  rectMode(CENTER)
}

function element(depth) {
  const hue = map(depth, 10, 1, 0, 1)
  fill(1, 0.5)
  noStroke()
  circle(0, 0, 10)
  
  fill(hue, 1, 1, 0.5)
  rect(0, -60, 100, 5)
  
  
  if (depth > 1) {
    push()
    rotate(PI / 4 + frameCount / 100)
    shearX(PI / 8)
    translate(0, -70)
    scale(0.9)
    element(depth - 1)
    pop()

    push()
    rotate(-PI / 4 - frameCount / 100)
    shearX(-PI / 8)
    translate(0, -70)
    scale(0.9)
    element(depth - 1)
    pop()
  }
}

function draw() {
  background(0.7)
  
  translate(width / 2, height / 2)
  
  element(8)
  rotate(PI)
  element(8)
  
  //console.log(frameCount)
}
