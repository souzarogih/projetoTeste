import pytest
from app.validacao import validar_cpf

class TestValidacaoCPF:
    def test_cpf_valido(self):
        print("Teste válido de CPF")
        assert validar_cpf("529.982.247-25")
        assert validar_cpf("52998224725")
        assert validar_cpf("123.456.789-09")
        assert validar_cpf("012.345.678-90")
        assert validar_cpf("123.456.789-09")
        assert validar_cpf("012.345.678-90")

    def test_cpf_invalido_tamanho_errado(self):
        print("Testando CPF com tamanho errado")
        assert not validar_cpf("00000000000")
        assert not validar_cpf("09850156811")
        assert not validar_cpf("123.456.789-0")
        assert not validar_cpf("11111111111")
        assert not validar_cpf("1234567890")
        assert not validar_cpf("98765432109")
        assert not validar_cpf("015680009811150156811")

    def test_cpf_invalido_digito_errado(self):
        print("Testando CPF com dígito verificador errado")
        assert not validar_cpf("529.982.247-26")
        assert not validar_cpf("1234567843290")
        assert not validar_cpf("123.456.789-0")
        assert not validar_cpf("abc.abc.abc-ab")
        assert not validar_cpf("1111.22222-12")

    def test_cpf_com_caracteres_invalidos(self):
        print("Testando CPF com caracteres inválidos")
        assert not validar_cpf("abc.def.ghi-jk")
        assert not validar_cpf("111.111.111-1a")
        assert not validar_cpf("1234567843290")
        assert not validar_cpf("123.456.789-0")
        assert not validar_cpf("abc.abc.abc-ab")
        assert not validar_cpf("1111.22222-12")

    def test_cpf_com_espacos_em_branco(self):
        print("Teste de CPF com espaços")
        assert validar_cpf(" 529.982.247-25 ")
        assert validar_cpf(" 52998224725 ")

    def test_cpf_com_caracteres_especiais_misturados(self):
        print("Testando com caracteres especiais")
        assert not validar_cpf("52@.98#.247-2*5")
        assert not validar_cpf("123123123-12")
        assert not validar_cpf("11111111111")
        assert not validar_cpf("111111111-11")
        assert not validar_cpf("99999999999")
        assert not validar_cpf("999999999-99")
        assert not validar_cpf("000000000-00")

    def test_cpf_com_mais_de_11_digitos(self):
        print("Testando com mais de 11 dígitos")
        assert not validar_cpf("529.257.127-321")
        assert not validar_cpf("325.128.247-568")

    def test_cpf_com_pontuacao_incompleta(self):
        print("Testando CPF incompleto")
        assert validar_cpf("529982.24725")
        assert validar_cpf("24725.529982")