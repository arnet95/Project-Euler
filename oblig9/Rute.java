import java.util.ArrayList;

class Rute {
    private final static String lookup = "0123456789";
    private boolean opptatt;
    public Rute neste;
    private int resultat = -1;
    private Boks boks;
    private Rad rad;
    public Kolonne kolonne;
    private Brett brett;
    public void settBoks(Boks b){
        boks = b;
    }
    public void settRad(Rad r){
        rad = r;
    }
    public void settKolonne(Kolonne k){
        kolonne = k;
    }

    public boolean opptatt(){
        return opptatt;
    }
    public int resultat(){
        return resultat;
    }
    public Rute(char c, Brett b){
        brett = b;
        if (c == '0'){
            opptatt = false;
        } else {
            opptatt = true;
            resultat = lookup.indexOf(c);
        }
    }
    public int[] finnAlleMuligeTall(){
        int counter = 9;
        ArrayList<Integer> listmuligheter = new ArrayList<Integer>();
        for (int i = 1; i <= 9; i++){
            if (boks.opptatte.indexOf(i) != -1){
                counter--;
            } else if (rad.opptatte.indexOf(i) != -1){
                counter--;
            } else if (kolonne.opptatte.indexOf(i) != -1){
                counter--;
            } else {
                listmuligheter.add(i);
            }
        }
        int[] muligheter = new int[listmuligheter.size()];
        for (int i = 0; i < listmuligheter.size(); i++){
            muligheter[i] = listmuligheter.get(i);
        }
        return muligheter;
    }
    public void fyllUtDenneRuteOgResten(){
        if (! opptatt){
            int[] muligeTall = finnAlleMuligeTall();
            for (int tall: muligeTall){
                resultat = tall;
                opptatt = true;
                boks.opptatte.add(tall);
                rad.opptatte.add(tall);
                kolonne.opptatte.add(tall);
                if (neste == null)
                    brett.skrivUt();
                else
                    neste.fyllUtDenneRuteOgResten();
                opptatt = false;
                boks.opptatte.remove((Integer) tall);
                rad.opptatte.remove((Integer) tall);
                kolonne.opptatte.remove((Integer) tall);
            }
        } else {
            if (neste == null)
                brett.skrivUt();
            else
                neste.fyllUtDenneRuteOgResten();
        }
    }
}
