from collections import Counter


class CompleteReport:
    def generate(products):
        manuf_dates = list()
        exp_dates = list()
        company_names = list()

        for prod in products:
            manuf_dates.append(prod["data_de_fabricacao"])
            exp_dates.append(prod["data_de_validade"])
            company_names.append(prod["nome_da_empresa"])

        oldest_manuf_date = min(manuf_dates)
        recently_exp_date = min(exp_dates)
        companies = Counter(company_names)
        company_counter = companies.most_common(1)[0][0]

        companies_quantities = ""
        for company, quantity in companies.items():
          companies_quantities += f"- {company}: {quantity}\n"

        return (
            f"Data de fabricação mais antiga: {oldest_manuf_date}\n"
            f"Data de validade mais próxima: {recently_exp_date}\n"
            f"Empresa com mais produtos: {company_counter}\n"
            f"Produtos estocados por empresa:\n"
            f"{companies_quantities}"
        )


#c.items(), to convert to a list of (elem, cnt) pairs