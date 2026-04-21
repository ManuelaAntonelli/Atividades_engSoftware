import java.util.List;

public class Company implements Aggregate<Alunos> {
    private List<Alunos> alunos;

    public Company(List<Alunos> Alunos){
        this.alunos = Alunos;
    }

    @Override
    public Interador<Alunos> createIterator(){
        return new AlunosInterador(alunos);
    }
}
