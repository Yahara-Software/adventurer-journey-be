using PathFinder;

var directionString = "15F6B6B5L16R8B16F20L6F13F11R";
var parser = new DirectionParser();
var directionPieces = parser.Parse(directionString);

var calculator = new DistanceLineCalculator();
var euclideanDistance = calculator.CalcEuclideanDistance(directionPieces);

Console.WriteLine($"For the input {directionString}, you would need to walk {euclideanDistance} steps to reach the straight line distance.");