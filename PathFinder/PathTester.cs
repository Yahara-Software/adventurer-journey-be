using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PathFinder
{
    internal class PathTester
    {
        public bool TestParsing(DirectionParser directionParser, List<string> incomingPaths, List<List<DirectionTraveled>> expectedDirectionsTraveled)
        { 
            if (incomingPaths.Count != expectedDirectionsTraveled.Count)
            {
                Console.WriteLine("Incoming paths do not equal the expected directions");
                return false;
            }

            for (int pathIndex = 0;  pathIndex < incomingPaths.Count; pathIndex++) 
            { 
                var parsedResults = directionParser.Parse(incomingPaths[pathIndex]);
                var expectedResults = expectedDirectionsTraveled[pathIndex];

                var areResultsEqual = parsedResults.SequenceEqual(expectedResults);
                if (!areResultsEqual)
                {
                    Console.WriteLine($"{parsedResults} does not parse into {expectedResults}");
                    return false;
                }
            }

            return true;
        }

        public bool TestCalculation(DistanceLineCalculator distanceCalculator, List<List<DirectionTraveled>> incomingDirectionsTraveled, List<double> expectedPathDistance)
        {
            if (expectedPathDistance.Count != incomingDirectionsTraveled.Count)
            {
                Console.WriteLine("Incoming directions do not match amount of expected distances");
                return false;
            }

            for (int pathIndex = 0; pathIndex < incomingDirectionsTraveled.Count; pathIndex++)
            {
                var expectedDistance = expectedPathDistance[pathIndex];
                var incomingDirections = incomingDirectionsTraveled[pathIndex];
                var calcualatedDistance = distanceCalculator.CalcEuclideanDistance(incomingDirections);

                var areResultsEqual = calcualatedDistance == expectedDistance;
                if (!areResultsEqual)
                {
                    Console.WriteLine($"{incomingDirections} does not calculate into {calcualatedDistance}");
                    return false;
                }
            }

            return true;
        }
    }
}
