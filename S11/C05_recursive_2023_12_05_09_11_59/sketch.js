const MAX_DEPTH = 13

function setup() {
  createCanvas(600, 600)
  rectMode(CENTER)
  colorMode(HSB, 1, 1, 1)
}

function drawElement(depth) {
  if (depth > 0) {
    noStroke()
    fill(depth / MAX_DEPTH, 1, 0.3, 0.4)
    rect(0, 0, 5, 30)
    fill(depth / MAX_DEPTH, 1, 1, 0.4)
    rect(0, -50, 100, 10)
    
    for (r of [-1, 1]) {
      push()
      rotate(PI / 4 * r)
      translate(0, -60)
      scale(0.85)
      drawElement(depth - 1)
      pop()
    }
  }
}

function draw() {
  background(0.2)
  
  translate(width / 2, height / 2 + 100)
  drawElement(MAX_DEPTH)
  noLoop()
}