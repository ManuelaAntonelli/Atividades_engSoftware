import java.util.List;
import java.util.NoSuchElementException;

class AlunosInterador implements Interador<Alunos> {
    
    private int currentIndex = 0;
    private List<Alunos> alunos;

    public AlunosInterador(List<Alunos> alunos){
        this.alunos = alunos;
    }

    @Override
    public boolean hasNext() {
        return currentIndex < alunos.size();
    }

    @Override
    public Alunos next() {
        if (!hasNext()){
            throw new NoSuchElementException();
        }
        return alunos.get(currentIndex++);
    }
}
