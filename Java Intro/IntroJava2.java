// Jonathan Klein
// 5/1/2019
// IntroJava2.java

public class IntroJava2 {
    private static void lineBreak(String n){
        System.out.println("============= " + n + " =============");
    }

    private static String middleThree(String str) {
        if(str.length() >= 3) {
            return str.substring(str.length()/2-1, str.length()/2+2);
        }
        else {
            return "String must be at least 3 characters.";
        }
    }

    public static void main(String[] args){
        lineBreak("Part 1");
        String myName = "Jonathan";
        int nameLength = myName.length();
        System.out.println("My name is " + myName + " and it contains " + nameLength + " letters.");

        lineBreak("Part 2");
        String name1 = "Adrian";
        String name2 = "adrian";
        String name3 = "Adrian";
        System.out.println(name1.equals(name2));
        System.out.println(name2.equals(name3));
        System.out.println(name3.equals(name1));

        lineBreak("Part 3");
        String nameA = "Chris";
        String nameB = "Alison";
        String nameC = "David";
        System.out.println(nameA.compareTo(nameB));
        System.out.println(nameB.compareTo(nameC));
        System.out.println(nameC.compareTo(nameA));

        lineBreak("Part 4");
        System.out.println(myName.indexOf("J"));
        System.out.println(myName.indexOf("o"));
        System.out.println(myName.indexOf("n"));
        System.out.println(myName.indexOf("x"));

        lineBreak("Part 5");
        System.out.println(myName.substring(0, 1));
        System.out.println(myName.substring(2, 3));
        System.out.println(myName.substring(1, 4));
        System.out.println(myName.substring(nameLength-2, nameLength));
        System.out.println(myName.substring(4, nameLength));

        lineBreak("BONUS");
        System.out.println(middleThree("123454321"));
    }
}
