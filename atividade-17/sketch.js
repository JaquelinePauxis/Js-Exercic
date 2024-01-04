var  caixa;
var gato;
function setup()
// pre-config
{

  createCanvas(400, 400);
  caixa = new Box(200, 200,20,20);
  gato = new Box(300, 100,20,20);

}

function draw()
{
  background(28);
  caixa.show();
  gato.show()

}
