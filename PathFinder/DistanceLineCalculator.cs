using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PathFinder
{
    internal class DistanceLineCalculator
    {
        public double CalcEuclideanDistance(List<DirectionTraveled> directionsTraveled)
        {
            var totalDistances = CalcTotalDistance(directionsTraveled);

            var vertical = totalDistances[Direction.Forward] - totalDistances[Direction.Backward];
            var horizontal = totalDistances[Direction.Right] - totalDistances[Direction.Left];

            var distance = Math.Sqrt(vertical * vertical + horizontal * horizontal);

            return distance;
        }

        private Dictionary<Direction, int> CalcTotalDistance(List<DirectionTraveled> directionsTraveled)
        {
            var totalDistances = new Dictionary<Direction, int>();
            foreach (Direction direction in Enum.GetValues(typeof(Direction)))
            {
                var distancesInDirection = directionsTraveled.Where(x => x.Direction == direction);
                var totalDistance = 0;
                foreach (var distance in distancesInDirection)
                {
                    totalDistance += distance.Distance;
                }
                totalDistances.Add(direction, totalDistance);
            }

            return totalDistances;
        }
    }
}
