function setup() {
  createCanvas(600, 600);
  rotSlider = createSlider(0, 100, 0);
  rotSlider.position(20, 20);
  
  translateSlider = createSlider(0, 100, 0);
  translateSlider.position(20, 50);
  
  scaleSlider = createSlider(0, 100, 0);
  scaleSlider.position(20, 80);
}

function element(depth) {
  if (depth > 0) {
    push();
    translate(0, translateSlider.value());
    rotate(rotSlider.value() / 100);
    scale(scaleSlider.value() / 100);
    circle(0, 0, 50);
    element(depth - 1);
    pop();
  }
}

function draw() {
  background(220);
  
  fill(0);
  
  translate(width / 2, height / 2);
  element(20);
}
