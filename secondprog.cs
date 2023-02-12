using System;

namespace secondprog
{
    class Program
    {
        static void MyMethod()
        {
            Console.WriteLine("I got executed.");
        }
        static void Main(string[] args)
        {
            MyMethod();
            MyMethod();
            MyMethod();
        }
    }
}