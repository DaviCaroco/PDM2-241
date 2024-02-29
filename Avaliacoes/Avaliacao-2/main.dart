class Dependente {
  late String _nome;

  Dependente(String nome) {
    this._nome = nome;
  }
}

class Funcionario {
  late String _nome;
  late List<Dependente> _dependentes;

  Funcionario(String nome, List<Dependente> dependentes) {
    this._nome = nome;
    this._dependentes = dependentes;
  }
}

class EquipeProjeto {
  late String _nomeProjeto;
  late List<Funcionario> _funcionarios;

  EquipeProjeto(String nomeprojeto, List<Funcionario> funcionarios) {
    _nomeProjeto = nomeprojeto;
    _funcionarios = funcionarios;
  }
}


void main() {
  var ObjetoD1 = Dependente("Objeto1");
  var ObjetoD2 = Dependente("Objeto2");
  var ObjetoD3 = Dependente("Objeto3");
  var ObjetoD4 = Dependente("Objeto4");
  var ObjetoD5 = Dependente("Objeto5");
  
  var ObjetoF1 = Funcionario("Claudio", [ObjetoD1]);
  var ObjetoF2 = Funcionario("Paula", [ObjetoD2]);
  var ObjetoF3 = Funcionario("Roberto", [ObjetoD3]);
  var ObjetoF4 = Funcionario("Jonas", [ObjetoD4]);
  var ObjetoF5 = Funcionario("Erick", [ObjetoD5]);

  var Lista = [ObjetoF1,ObjetoF2,ObjetoF3,ObjetoF4,ObjetoF5];

  var Equipe = EquipeProjeto("Projeto", Lista);
  
}
