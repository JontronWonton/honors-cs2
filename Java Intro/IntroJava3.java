// Jonathan Klein
// 5/3/19
// IntroJava3.java

import java.util.Scanner;

public class IntroJava3 {
    private static void lineBreak(String n){
        System.out.println("============= " + n + " =============");
    }

    private static double farenheitToCelsius(double f){
        return (5*(f-32))/9;
    }

    private static double celsiusToFarenheit(double c){
        return (((9*c)/5))+32;
    }

    private static String firstThree(){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a string of at least 3 letters.");
        String result = input.nextLine();
        try{
            return result.substring(0, 3);
        } catch(IndexOutOfBoundsException e){
            return "String must be at least 3 letters.";
        }

    }

    public static void main(String[] args) {
        lineBreak("Part 1");
        System.out.println("   J    A   V     V  A\n   J   A A   V   V  A A\nJ  J  AAAAA   V V  AAAAA\n JJ  A     A   V  A     A");

        lineBreak("Part 2");
        int num1 = 4;
        int num2 = 2;
        int num3 = 8;

        System.out.println(num1+num2);
        System.out.println(num1-num2);
        System.out.println(num1*num2);
        System.out.println(num1/num2);
        System.out.println(num3/num2);

        double num4 = 3.1415926535897932384624633832795028841971;
        double num5 = 2.7182818284590452353602874713527;

        System.out.println(num4/num5);
        System.out.println(num1%num2);

        lineBreak("Part 3");
        System.out.println(farenheitToCelsius(77));
        System.out.println(celsiusToFarenheit(23));

        lineBreak("Part 4");
        Scanner input = new Scanner(System.in);
        System.out.println("What is your name?");
        String nameTest = input.nextLine();
        System.out.println("Nice to meet you, " + nameTest);

        lineBreak("Part 5");
        input = new Scanner(System.in);
        System.out.println("Enter a name.");
        String name = input.nextLine();
        input = new Scanner(System.in);
        System.out.println("Enter an adjective.");
        String adjective = input.nextLine();
        input = new Scanner(System.in);
        System.out.println("Enter a verb.");
        String verb = input.nextLine();
        input = new Scanner(System.in);
        System.out.println("Enter an adverb.");
        String adverb = input.nextLine();
        input = new Scanner(System.in);
        System.out.println("Enter a place.");
        String place = input.nextLine();

        System.out.println("Hello, my name is "+name+" and I am very "+adjective+". My favorite thing to do is "+verb+". I do this very "+adverb+". I especially like to "+verb+" at "+place+".");

        lineBreak("BONUS");
        System.out.println(firstThree());
    }

}
