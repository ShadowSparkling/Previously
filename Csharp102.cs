using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Csharp101
{
    internal class Csharp102
    {
        static void Main(string[] args) {
            // Console.WriteLine("This is my first program. :|)");
            // Console.WriteLine("May I know your name to thank you?");
            // string name101 = Console.ReadLine();
            // // Console.WriteLine("Thanks " + name101);
            // Console.WriteLine( $"Thanks {name101}. Really Appreciated your efforts ;)");
            // Console.ReadKey();



            // // A program to give a rectangle of desired rows and columns with desireed symbol.            
            // Console.WriteLine("Enter the number of rows: ");
            // int rows = Convert.ToInt32(Console.ReadLine());
            // Console.WriteLine("Enter the number of columns: ");
            // int columns = Convert.ToInt32(Console.ReadLine());
            // Console.WriteLine("And your symbol? ");
            // string symbol = Console.ReadLine();
            // Console.WriteLine("\n\n");
            // 
            // for (int i = 0; i < rows; i++)
            // {
            //     for (int j = 0; j < columns; j++)
            //     {
            //         Console.Write(symbol);
            //     }
            //     Console.WriteLine();
            // }



            // // Number gessing game with C#
            // Random random = new Random();
            // bool playAgain = true;
            // int min = 1;
            // int max = 100;
            // int number;
            // int guess;
            // int Noofguesses;
            // string response;
            // 
            // 
            // while (playAgain)
            // {
            //     guess = 0;
            //     Noofguesses = 0;
            //     number = random.Next(min, max + 1);
            //     response = "";
            // 
            //     while (guess != number)
            //     {
            //         Console.WriteLine($"Guess a number between {min} and {max}: ");
            //         guess = Convert.ToInt32((Console.ReadLine()));
            //         Console.WriteLine($"Guess: {guess}");
            // 
            //         if(guess > number)
            //         {
            //             Console.WriteLine("Too high guess!");
            //         }
            //         
            //         else if(guess < number)
            //         {
            //             Console.WriteLine("Too low guess!");
            //         }
            //         Noofguesses++;
            //     }
            //     Console.WriteLine($"Number: {number}");
            //     Console.WriteLine("YOU WIN.");
            //     Console.WriteLine($"It took you {Noofguesses} to do that.");
            // 
            //     Console.WriteLine("Would you like to play again (Y/N)?");
            //     response = Console.ReadLine();
            //     response = response.ToUpper();
            // 
            //     if (response == "Y")
            //     {
            //         playAgain = true;
            //     }
            //     else
            //     {
            //         playAgain = false;
            //     }
            // 
            // }

            // Console.WriteLine("Thanks for playing!!!");



            // //CALCULATOR PROGRAM
            // Console.WriteLine("----------------");
            // Console.WriteLine("BASIC CALCULATOR");
            // Console.WriteLine("----------------");
            // 
            // do { 
            // double result;
            // double num1 = 0;
            // double num2 = 0;
            // 
            // Console.WriteLine("Enter your numbers:");
            // Console.WriteLine("First number:");
            // num1 = Convert.ToDouble(Console.ReadLine());
            // Console.WriteLine($"Your second number is {num1}");
            // Console.WriteLine("Second number:");
            // num2 = Convert.ToDouble(Console.ReadLine());
            // Console.WriteLine($"Your second number is {num2}");
            // 
            // Console.WriteLine("Enter an option: " +
            //     "\n\t +: Addition" + "\n\t -: Subtraction" + "\n\t *: Multiplication" + "\n\t /: Division");
            // string option = Console.ReadLine();
            // Console.WriteLine($"Your option: {option}");
            // switch (option)
            // {
            //     case "+":
            //             result = num1 + num2;
            //             Console.WriteLine(result);                
            //     break;
            //     
            //     case "-":
            //             result = num1 - num2;
            //             Console.WriteLine(result);                
            //     break;
            // 
            //     case "*":
            //         result = num1 * num2;
            //         Console.WriteLine(result);
            //         break;
            // 
            //     case "/":
            //         result = num1 / num2;
            //         Console.WriteLine(result);
            //         break;
            //     default: Console.WriteLine("That wasn't a valid option.");
            //         break;
            // }
            //     Console.WriteLine("Would you like to continue (Y/N)?");
            //     }
            // while(Console.ReadLine().ToUpper() == "Y");
            // 
            // Console.WriteLine("Adios");







            Console.ReadLine();

        }
    }
}
