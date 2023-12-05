let rotSlider, distSlider, scaleSlider;

function setup() {
  // create canvas
  createCanvas(800, 800);
  textSize(15);
  noStroke();

  // create sliders
  rotSlider = createSlider(0, 200, 0);
  rotSlider.position(20, 20);
  distSlider = createSlider(0, 100, 0);
  distSlider.position(20, 50);
  scaleSlider = createSlider(0, 100, 0);
  scaleSlider.position(20, 80);
}

function element(depth) {
  if (depth > 0) {
    fill(0);
    stroke(0);
    strokeWeight(3);
    circle(0, 0, 20);
    
    push();
    rotate(rotSlider.value() / 100);
    line(0, 0, 0, -distSlider.value());
    translate(0, -distSlider.value());
    scale(scaleSlider.value() / 50);
    element(depth - 1);
    pop();

    push();
    rotate(-rotSlider.value() / 100);
    line(0, 0, 0, -distSlider.value());
    translate(0, -distSlider.value());
    scale(scaleSlider.value() / 50);
    element(depth - 1);
    pop();
}
}

function draw() {
  background(128);
  
  text('distance', 50 + distSlider.width, distSlider.y + 15);
  text('scale', 50 + scaleSlider.width, scaleSlider.y + 15);
  text('rotation', 50 + rotSlider.width, rotSlider.y + 15);
  translate(width / 2, height / 2);
  element(5);
  rotate(PI);
  element(5);
}