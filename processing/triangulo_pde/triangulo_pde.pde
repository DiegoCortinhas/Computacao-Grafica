
float[] roda(float cx, float cy, float px, float py, float a )
{
  float _px = ((px-cx)*cos(a)-(py-cy)*sin(a))+cx;
  float _py = ((px-cx)*sin(a)+(py-cy)*cos(a))+cy;
  return new float[] { _px, _py };
}

int np = 0;
float p1x, p1y, p2x, p2y;

void setup() 
{
  size(800,600);
}

void draw()
{
  if(np == 2)
  {
    float p3[] = roda(p1x, p1y, p2x, p2y, -PI/3);
    beginShape();
    vertex(p1x, p1y);
    vertex(p2x, p2y);
    vertex(p3[0], p3[1]);
    endShape(CLOSE);
    np = 0;
  }
}

  void mouseReleased()
  {
    if(np == 0)
    {
      p1x = mouseX;
      p1y = mouseY;
      np = 1;
    }
    else if(np == 1)
    {
      p2x = mouseX;
      p2y = mouseY;
      np = 2;
    }
  }
  
 
