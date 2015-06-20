class Brett {
    private Rute[][] brettMatrise;
    private Rad[] rader;
    private Kolonne[] kolonner;
    private Boks[][] bokser;
    private Rute foran;
    public int res = 0;
    public Brett(){
        rader = new Rad[9];
        kolonner = new Kolonne[9];
        bokser = new Boks[3][3];
        brettMatrise = new Rute[9][9];
        for (int i = 0; i < 9; i++){
            rader[i] = new Rad();
            kolonner[i] = new Kolonne();
        }
        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                bokser[i][j] = new Boks();
            }
        }
    }
    public void settInn(int i, int j, char c){
        brettMatrise[i][j] = new Rute(c, this);
    }
    public int taUt(int i, int j){
        return brettMatrise[i][j].resultat();
    }
    public void delInnRuter(){
        for (int i = 0; i < 9; i++){
            for (int j = 0; j < 9; j++){
                Rute r = brettMatrise[i][j];
                boolean ruteOpptatt = r.opptatt();
                Rad rad = rader[i];
                Kolonne kolonne = kolonner[j];
                Boks boks = bokser[i/3][j/3];
                if (ruteOpptatt){
                    int c = r.resultat();
                    rad.opptatte.add(c);
                    kolonne.opptatte.add(c);
                    boks.opptatte.add(c);
                }
                r.settRad(rad);
                r.settBoks(boks);
                r.settKolonne(kolonne);

            }
        }
        //Lager lenkeliste
        for (int i = 8; i >= 0; i--){
            for (int j = 8; j >= 0; j--){
                brettMatrise[i][j].neste = foran;
                foran = brettMatrise[i][j];
            }
        }
    }


    public void skrivUt(){
        int result = 0;
        result += foran.resultat()*100;
        result += foran.neste.resultat()*10;
        result += foran.neste.neste.resultat();
        res = result;
    }
    public void fyllUtAlleRutene(){
        System.out.println("Hello");
        foran.fyllUtDenneRuteOgResten();
    }
}
