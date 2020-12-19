using System;

class Program
{
    static void Main(string[] args)
    {
        //met le titre de l'app
        Console.Title = "saif-land";
        
        //écris une ligne avec du contenu
        Console.WriteLine("bonjour comment vous appellez-vous");

        //demande au joueur une réponse
        string reponse = Console.ReadLine();

        //répond au joueur
        Console.WriteLine("bonjour " + reponse);
        Console.WriteLine("j'espere que vous allez bien");
        Console.WriteLine("si oui c'est une autre chose pour le royaume de saif-land");

        //laisse un moment d'attente
        Console.Read();
    }
}