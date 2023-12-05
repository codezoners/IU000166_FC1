let slider

function setup() {
  createCanvas(600, 600)
  rectMode(CENTER)
  angleMode(DEGREES)
  textSize(36)
  textAlign(CENTER, CENTER)

  slider = createSlider(0, 200, 0) // min, max, default value.
  slider.position(20, 20)
}

function element(depth) {
  stroke(0)
  fill(depth * 40, 255 - depth * 40, 0, 50)
  circle(0, 0, 50)

  if (depth > 1) {          //  RECURSE!
    push()
    rotate(slider.value())
    scale(0.9)
    line(0, 0, 0, 60)
    translate(0, 60)
    element(depth - 1)
    pop()

    push()
    rotate(-slider.value())
    scale(0.9)
    line(0, 0, 0, 60)
    translate(0, 60)
    element(depth - 1)
    pop()
  }
}

function draw() {
  background(220)

  push()
  translate(width / 2, height / 2)
  element(10)
  rotate(180)
  element(10)
  pop()

  stroke(255)
  fill(0)
  text(slider.value(), width / 2, 30)
}
