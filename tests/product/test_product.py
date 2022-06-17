from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(1, "miojo", "nissan lámen", "25/12/2019", "25/12/2023",
                    "2512190001", "Armazenar em ambiente seco")

    assert produto.id == 1
    assert produto.nome_do_produto == "miojo"
    assert produto.nome_da_empresa == "nissan lámen"
    assert produto.data_de_fabricacao == "25/12/2019"
    assert produto.data_de_validade == "25/12/2023"
    assert produto.numero_de_serie == "2512190001"
    assert produto.instrucoes_de_armazenamento == "Armazenar em ambiente seco"

    pass
