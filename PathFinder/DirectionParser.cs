using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace PathFinder
{
    internal class DirectionParser
    {
        private Dictionary<string, Direction> directionLookups = new Dictionary<string, Direction>()
        {
            { "F", Direction.Forward },
            { "B", Direction.Backward },
            { "L", Direction.Left},
            { "R", Direction.Right }
        };

        public List<DirectionTraveled> Parse(string directionString)
        {
            var directionParts = Regex.Split(directionString, @"([FBLR])");
            
            var directionPieces = new List<DirectionTraveled>();
            for (int index = 0; index + 1 < directionParts.Length; index += 2)
            {
                var distance = directionParts[index];
                var direction = directionParts[index + 1];
                directionPieces.Add(new DirectionTraveled
                {
                    Distance = int.Parse(distance),
                    Direction = directionLookups[direction]
                });
            }    
            
            return directionPieces;
        }        
    }
}

enum Direction
{
    Forward,
    Backward,
    Left,
    Right
}

struct DirectionTraveled
{
    public Direction Direction;
    public int Distance;

    public override string ToString()
    {
        return $"Traveled {Distance} in {Direction} direction";
    }
}

