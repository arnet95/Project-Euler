import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class Oblig9main{
    private static Brett sudokuBrett;
    private static int total = 0;
    private static int lengde = 9;
    public static void main(String[] args) throws FileNotFoundException{
        File infile = new File("p096_sudoku.txt");
        Scanner input = new Scanner(infile);
        for (int n = 1; n <= 50; n++){
            input.nextLine();
            sudokuBrett = new Brett();
            for (int i = 0; i < 9; i++){
                String linje = input.nextLine();
                for (int j = 0; j < lengde; j++){
                    sudokuBrett.settInn(i, j, linje.charAt(j));
                }
            }
            sudokuBrett.delInnRuter();
            sudokuBrett.fyllUtAlleRutene();
            total += sudokuBrett.res;
        }
        System.out.println(total);
    }

}
