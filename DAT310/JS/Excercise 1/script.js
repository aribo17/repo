function BankAccount(name, balance){
    this.name = name;
    this.balance = balance;
    this.deposit = deposit;
    this.withdraw = withdraw;
        
}

function deposit(amount){
    this.balance += amount;
}
 
function withdraw(amount){
    if(this.amount>= amount){
        this.balance -= amount;
    }
  
}
    