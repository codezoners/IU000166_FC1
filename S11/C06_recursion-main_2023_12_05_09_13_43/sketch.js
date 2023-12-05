function setup() {
  createCanvas(800, 800);
  strokeWeight(3);
  rotSlider = createSlider(0, 100, 0);
  rotSlider.position(20, 20);
  
  translateSlider = createSlider(0, 100, 0);
  translateSlider.position(20, 50);
  
  scaleSlider = createSlider(0, 100, 0);
  scaleSlider.position(20, 80);
}

function element(depth, colour) {
  if (depth > 0) {
    line(0, 25, 0, translateSlider.value())
    
    push();
    translate(0, translateSlider.value());
    //rotate(+rotSlider.value() / 100);
    rotate(+frameCount / 100)
    scale(scaleSlider.value() / 100);
    fill(255);
    circle(0, 0, 50);
    element(depth - 1, colour + 10);
    pop();
    
    push();
    translate(0, translateSlider.value());
    //rotate(-rotSlider.value() / 100);
    rotate(-frameCount / 100)
    scale(scaleSlider.value() / 100);
    fill(244);
    circle(0, 0, 50);
    element(depth - 1, colour + 10);
    pop();
  }
}

function draw() {
  background(150);
  
  translate(width / 2, height / 2);
  element(8, 0);
  rotate(PI * 2 / 3)
  element(8, 0);
  rotate(PI * 2 / 3)
  element(8, 0);
}
