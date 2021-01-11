

void setup() 
{
  size(500,500);
}

void draw()
{
  //background(200);
  int margem = 20;
  float n = round(map(mouseX,0,width,3,12));
  float a = TWO_PI/n;
  int r = (width/2)-margem;
  translate(width/2,height/2);
  beginShape();
  for(int i=0; i<n; i++)
  {
    float x = r*cos(i*a);
    float y = r*sin(i*a);
    vertex(x,y);
  }
  endShape(CLOSE);
}
