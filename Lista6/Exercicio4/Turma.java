import java.util.ArrayList;
import java.util.List;

public class Turma {
    
    public static void main(String[] args){
        List<Alunos> alunos = new ArrayList<>();
        alunos.add(new Alunos("José","Turma A"));
        alunos.add(new Alunos("Manu","Turma A"));
        alunos.add(new Alunos("Maria","Turma B"));
        alunos.add(new Alunos("Paulo","Turma C"));

        Company company = new Company(alunos);

        Interador<Alunos> interador = company.createIterator();
        
        while(interador.hasNext()) {
            Alunos aluno = interador.next();
            System.out.println("Nome: " + aluno.getName() + " - Turma: " + aluno.getTurma());
        }
    }   
}
