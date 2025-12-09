using PathFinder;

var parser = new DirectionParser();
var directionPieces = parser.Parse("15F6B6B5L16R8B16F20L6F13F11R");

var calculator = new DistanceLineCalculator();
var euclideanDistance = calculator.CalcEuclideanDistance(directionPieces);

Console.WriteLine(euclideanDistance);