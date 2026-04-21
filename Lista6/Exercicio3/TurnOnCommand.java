class TurnOnCommand implements Command{
    private Receiver receiver;
    
    public TurnOnCommand(Receiver receiver){
        this.receiver = receiver;
    }

    @Override
    public void execute(){
        receiver.turnOn();
    }
}
