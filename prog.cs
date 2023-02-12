using System;

namespace prog
{
    class Car //New class
    {
        // string color = "red"; //Field

        // public void Main(string[] args)
        // {
        //     Console.WriteLine("This is a test class. The color is " + color + ".");
        // }

        int maxSpeed;
        string name;
        static void Main(string[] args)
        {
            Car Ford = new Car();
            Ford.name = "Ford";
            Ford.maxSpeed = 234;

            Console.WriteLine($"The name of this car is {Ford.name} and the highest speed it can reach is {Ford.maxSpeed}kmph.");
        }
    };
};