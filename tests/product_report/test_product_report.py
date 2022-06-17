from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(1, "miojo", "nissan lámen", "25/12/2019", "25/12/2023",
                     "2512190001", "Armazenar em ambiente seco")

    assert produto.__repr__() == (
        "O produto miojo fabricado em 25/12/2019"
        " por nissan lámen com validade até 25/12/2023"
        " precisa ser armazenado Armazenar em ambiente seco."
    )
    pass
