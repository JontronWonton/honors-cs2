public class IntroJava1 {
    private static void lineBreak(String n){
        System.out.println("============= " + n + " =============");
}
    public static void main(String[] args) {
        lineBreak("Part 2");
        String firstName = "Jonathan";
        String lastName = "Klein";
        int age = 15;
        double gpa = 99.7;
        boolean graduated = false;
        String wholeName = firstName + " " + lastName;
        int xp;
        String college;

        System.out.println(firstName);
        System.out.println(lastName);
        System.out.println(age);
        System.out.println(gpa);
        System.out.println(graduated);
        System.out.println(wholeName);

        lineBreak("Part 3");
        xp = 1;
        System.out.println("First Name: " + firstName + "\nLast Name: " + lastName + "\nAge: " + age + "\nGPA: " + gpa + "\nGraduated: " + graduated + "\nFull Name: " + wholeName);

        lineBreak("Part 4");
        xp++;
        age += 2;
        graduated = true;
        college = "Harvard University";
        String personalMessage = "Hello, I am " +
                wholeName + ", and I am " + age +
                " years old and my GPA is " + gpa +
                ". I am interested in attending " +
                college;
        System.out.println(personalMessage);
        System.out.println("XP: " + xp);

        lineBreak("BONUS");
    }


}
