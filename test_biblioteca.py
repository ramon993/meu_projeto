import pytest
from biblioteca import livros, usuarios, adicionar_livro, registrar_usuario, emprestar_livro

def test_adicionar_livro():
    adicionar_livro("Livro Teste", "Autor X")
    assert any(l["titulo"]=="Livro Teste" for l in livros)

def test_registrar_usuario():
    registrar_usuario("Fulano")
    assert any(u["nome"]=="Fulano" for u in usuarios)

def test_emprestar_livro():
    adicionar_livro("Livro Y", "Autor Y")
    registrar_usuario("Beltrano")
    emprestar_livro("Beltrano","Livro Y")
    usuario = next(u for u in usuarios if u["nome"]=="Beltrano")
    assert "Livro Y" in usuario["livros_emprestados"]
