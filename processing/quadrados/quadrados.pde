float a = 0;

void setup()
{
  size(800,600);
}

void draw() 
{
  background(200);
  translate(width/2, height/2);

  pushMatrix();
  translate(width/4, height/4);
  rotate(a);
  rect(-26, -26, 52, 52);
  popMatrix();
  
  pushMatrix();
  translate(-width/4, height/4);
  rotate(-a);
  rect(-26, -26, 52, 52);
  popMatrix();
  
  pushMatrix();
  translate(-width/4, -height/4);
  rotate(a);
  rect(-26, -26, 52, 52);
  popMatrix();
  
  pushMatrix();
  translate(width/4, -height/4);
  rotate(a);
  rect(-26, -26, 52, 52);
  popMatrix();
  
  a+=0.05;
}
