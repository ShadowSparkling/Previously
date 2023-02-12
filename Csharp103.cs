using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Csharp101
{
    internal class Csharp103
    {

        // static void Main(string[] args)
        // {
        //     string name101 = "Hart";
        //     int age101 = 234;
        // 
        //     singHappyBirthday(name101, age101);
        // }
        // static void singHappyBirthday(string name, int age)
        // {
        //     Console.WriteLine("Happy Birthday " + name);
        //     Console.WriteLine("You are now of " + age);
        // }
        static void Main(string[] args)
        {

            Human human1 = new Human();

            human1.name = "Snape";
            human1.age = 65;

            human1.Eat();
            human1.Sleep();


            Console.ReadKey();
        }
    }
    class Human {

        public string name;
        public int age;

        public void Eat()
        {
            Console.WriteLine($"{name} is eating.");
        }
        public void Sleep()
        {
            Console.WriteLine($"{name} is sleeping.");
        }


    }


}
