import 'package:dart_application_1/dart_application_1.dart' as dart_application_1;
import 'dart:convert';

class Dependente {
  late String _nome;

  Dependente(String nome) {
    this._nome = nome;
  }

  Map<String, dynamic> toJson() {
    return {
      'nome': _nome,
    };
  }
}

class Funcionario {
  late String _nome;
  late List<Dependente> _dependentes;

  Funcionario(String nome, List<Dependente> dependentes) {
    this._nome = nome;
    this._dependentes = dependentes;
  }

  Map<String, dynamic> toJson() {
    return {
      'nome': _nome,
      'dependentes': _dependentes.map((dependente) => dependente.toJson()).toList(),
    };
  }
}

class EquipeProjeto {
  late String _nomeProjeto;
  late List<Funcionario> _funcionarios;

  EquipeProjeto(String nomeprojeto, List<Funcionario> funcionarios) {
    _nomeProjeto = nomeprojeto;
    _funcionarios = funcionarios;
  }

  Map<String, dynamic> toJson() {
    return {
      'nomeProjeto': _nomeProjeto,
      'funcionarios': _funcionarios.map((funcionario) => funcionario.toJson()).toList(),
    };
  }
}

void main() {
  var dependente1 = Dependente('Dependente1');
  var dependente2 = Dependente('Dependente2');

  var funcionario1 = Funcionario('Claudio', [dependente1]);
  var funcionario2 = Funcionario('Fernanda', [dependente2]);

  var ListaFuncionarios = [funcionario1, funcionario2];

  var equipeProjeto = EquipeProjeto('Projeto1', ListaFuncionarios);

  var EquipeProjetoJson = jsonEncode(equipeProjeto.toJson());
  print(EquipeProjetoJson);
}
