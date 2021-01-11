float x0 = -2;
float xf = 2;
float y0 = 3;
float yf = -0.1;
float deltaX = 0.05;

void setup()
{
  size(600,400);
}

int xt(float x)
{
  return (int)(width*(x-x0)/(xf-x0));
}

int yt(float y)
{
  return (int)(height*(y-y0)/(yf-y0));
}

float f2(float x)
{
  return cos(10*x)*x*0.1;
}

float f(float x)
{
  return x*x;
}

void draw()
{
  float x = x0;
  noFill();
  beginShape();
  while(x < xf)
  {
    vertex(xt(x), yt(f2(x)));
    x += deltaX;
  }
  endShape();
  
}