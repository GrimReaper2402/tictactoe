import java.util.*;
public class pass1 {
    public static void main(String args[]){
        Scanner scc=new Scanner(System.in);
        System.out.println("Enter the no of lines: ");
        int n = scc.nextInt();
        System.out.println("Enter the code:");
        scc.nextLine();
        String code[]=new String[n];
        for (int i = 0; i < n; i++) {
            code[i]=scc.nextLine();
        }

        String[] symbol=new String[10];
        String[] constant=new String[10];
        int lc=0,sc=0,cc=1,index;

        System.out.println("LC\t|\tPass1");

        for (int i = 0; i < code.length; i++) {
            String[] str= code[i].split(" ");
            int j=0;
            int len=str.length;
            while (j<len){

                switch (str[j]){
                    case "START":
                        lc =Integer.parseInt(str[j+1]);
                        System.out.print("\t\t|\t(AD,01) (c,"+lc+")");
                        j+=2;
                        break;
                    case "A":
                        index=java.util.Arrays.asList(symbol).indexOf("A");
                        if(index==-1){
                            symbol[sc]="A";
                            System.out.print("(S,"+sc+") ");
                            sc++;
                        }else {
                            System.out.print("(S,"+index+") ");
                        }
                        j++;
                        break;
                    case "B":
                        index=java.util.Arrays.asList(symbol).indexOf("B");
                        if(index==-1){
                            symbol[sc]="B";
                            System.out.print("(S,"+sc+") ");
                            sc++;
                        }else {
                            System.out.print("(S,"+index+") ");
                        }
                        j++;
                        break;
                    case "C":
                        index=java.util.Arrays.asList(symbol).indexOf("C");
                        if(index==-1){
                            symbol[sc]="C";
                            System.out.print("(S,"+sc+") ");
                            sc++;
                        }else {
                            System.out.print("(S,"+index+") ");
                        }
                        j++;
                        break;
                    case "DS":
                        System.out.print("(DL,0) ");
                        j++;
                        break;
                    case"1":
                        index=java.util.Arrays.asList(constant).indexOf("1");
                        if(index==-1){
                            constant[cc]="1";
                            System.out.print("(C,"+cc+") ");
                            cc++;
                        }else {
                            System.out.print("(C,"+index+") ");
                        }
                        j++;
                        break;
                    case"READ":
                        System.out.print("(IS,09) ");j++;
                        break;
                    case"MOVER":
                        System.out.print("(IS,04) ");j++;
                        break;
                    case"AREG,":
                        System.out.print("(RG,01) ");j++;
                        break;
                    case"ADD":
                        System.out.print("(IS,01) ");j++;
                        break;
                    case"MOVEM":
                        System.out.print("(IS,05) ");j++;
                        break;
                    case"PRINT":
                        System.out.print("(IS,10) ");j++;
                        break;
                    case"END":
                        System.out.print("(AD,02) ");j++;
                        break;
                }

            }
            System.out.print("\n"+lc+"\t\t|\t");
            lc++;
        }
    }
}
