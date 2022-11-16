import scrapy
from scrapy.selector import Selector

data = {
    "nome": [],
    "genero": [],
    "presença_plenario": [],
    "ausencia_plenario": [],
    "ausencia_justificada_plenario": [],
    "presenca_comissao": [],
    "ausencia_comissao": [],
    "ausencia_justificada_comissao": [],
    "data_nascimento": [],
    "gasto_total_par": [],
    "gasto_jan_par": [],
    "gasto_fev_par": [],
    "gasto_mar_par": [],
    "gasto_abr_par": [],
    "gasto_maio_par": [],
    "gasto_junho_par": [],
    "gasto_jul_par": [],
    "gasto_agosto_par": [],
    "gasto_set_par": [],
    "gasto_out_par": [],
    "gasto_nov_par": [],
    "gasto_dez_par": [],
    "salario_bruto_par": [],
    "gasto_total_gab": [],
    "gasto_jan_gab": [],
    "gasto_fev_gab": [],
    "gasto_mar_gab": [],
    "gasto_abr_gab": [],
    "gasto_maio_gab": [],
    "gasto_junho_gab": [],
    "gasto_jul_gab": [],
    "gasto_agosto_gab": [],
    "gasto_set_gab": [],
    "gasto_out_gab": [],
    "gasto_nov_gab": [],
    "gasto_dez_gab": [],
    "salario_bruto": [],
    "quant_viagem": [],
    "quant_viagem": [],
}


class GetInfosSpider(scrapy.Spider):
    name = "infos"

    def start_requests(self):
        urls = [
            "https://www.camara.leg.br/deputados/204528",
            "https://www.camara.leg.br/deputados/204545",
            "https://www.camara.leg.br/deputados/74057",
            "https://www.camara.leg.br/deputados/204353",
            "https://www.camara.leg.br/deputados/204400",
            "https://www.camara.leg.br/deputados/73696",
            "https://www.camara.leg.br/deputados/123756",
            "https://www.camara.leg.br/deputados/204509",
            "https://www.camara.leg.br/deputados/73701",
            "https://www.camara.leg.br/deputados/204374",
            "https://www.camara.leg.br/deputados/160589",
            "https://www.camara.leg.br/deputados/213762",
            "https://www.camara.leg.br/deputados/204507",
            "https://www.camara.leg.br/deputados/164360",
            "https://www.camara.leg.br/deputados/204369",
            "https://www.camara.leg.br/deputados/204380",
            "https://www.camara.leg.br/deputados/204462",
            "https://www.camara.leg.br/deputados/178928",
            "https://www.camara.leg.br/deputados/178939",
            "https://www.camara.leg.br/deputados/204459",
            "https://www.camara.leg.br/deputados/81297",
            "https://www.camara.leg.br/deputados/204434",
            "https://www.camara.leg.br/deputados/178994",
            "https://www.camara.leg.br/deputados/204421",
            "https://www.camara.leg.br/deputados/178989",
            "https://www.camara.leg.br/deputados/204525",
            "https://www.camara.leg.br/deputados/178945",
            "https://www.camara.leg.br/deputados/204357",
            "https://www.camara.leg.br/deputados/204535",
            "https://www.camara.leg.br/deputados/178961",
            "https://www.camara.leg.br/deputados/204360",
            "https://www.camara.leg.br/deputados/178946",
            "https://www.camara.leg.br/deputados/204534",
            "https://www.camara.leg.br/deputados/204464",
            "https://www.camara.leg.br/deputados/178901",
            "https://www.camara.leg.br/deputados/204466",
            "https://www.camara.leg.br/deputados/215044",
            "https://www.camara.leg.br/deputados/74784",
            "https://www.camara.leg.br/deputados/178866",
            "https://www.camara.leg.br/deputados/166402",
            "https://www.camara.leg.br/deputados/204458",
            "https://www.camara.leg.br/deputados/204471",
            "https://www.camara.leg.br/deputados/204430",
            "https://www.camara.leg.br/deputados/74398",
            "https://www.camara.leg.br/deputados/204540",
            "https://www.camara.leg.br/deputados/178956",
            "https://www.camara.leg.br/deputados/204428",
            "https://www.camara.leg.br/deputados/204432",
            "https://www.camara.leg.br/deputados/204453",
            "https://www.camara.leg.br/deputados/66179",
            "https://www.camara.leg.br/deputados/205535",
            "https://www.camara.leg.br/deputados/204377",
            "https://www.camara.leg.br/deputados/73943",
            "https://www.camara.leg.br/deputados/204529",
            "https://www.camara.leg.br/deputados/204565",
            "https://www.camara.leg.br/deputados/160639",
            "https://www.camara.leg.br/deputados/160641",
            "https://www.camara.leg.br/deputados/204467",
            "https://www.camara.leg.br/deputados/178925",
            "https://www.camara.leg.br/deputados/74075",
            "https://www.camara.leg.br/deputados/220008",
            "https://www.camara.leg.br/deputados/160575",
            "https://www.camara.leg.br/deputados/204407",
            "https://www.camara.leg.br/deputados/204354",
            "https://www.camara.leg.br/deputados/160598",
            "https://www.camara.leg.br/deputados/178966",
            "https://www.camara.leg.br/deputados/107283",
            "https://www.camara.leg.br/deputados/198197",
            "https://www.camara.leg.br/deputados/67138",
            "https://www.camara.leg.br/deputados/74848",
            "https://www.camara.leg.br/deputados/108338",
            "https://www.camara.leg.br/deputados/178839",
            "https://www.camara.leg.br/deputados/204468",
            "https://www.camara.leg.br/deputados/204546",
            "https://www.camara.leg.br/deputados/160534",
            "https://www.camara.leg.br/deputados/178832",
            "https://www.camara.leg.br/deputados/204375",
            "https://www.camara.leg.br/deputados/139285",
            "https://www.camara.leg.br/deputados/204405",
            "https://www.camara.leg.br/deputados/204410",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # url = response.url
        nome = response.css("ul.informacoes-deputado").getall()

        data["nome"].append(Selector(text=nome[0]).xpath("//li/text()").get())
        data["genero"].append("F")
        dias = response.css("dd.list-table__definition-description").getall()
        numero = Selector(text=dias[0]).xpath("//dd/text()").get().strip().split(" ")
        data["presença_plenario"].append(numero[0])
        numero = Selector(text=dias[2]).xpath("//dd/text()").get().strip().split(" ")
        data["ausencia_plenario"].append(numero[0])
        numero = Selector(text=dias[1]).xpath("//dd/text()").get().strip().split(" ")
        data["ausencia_justificada_plenario"].append(numero[0])
        numero = Selector(text=dias[3]).xpath("//dd/text()").get().strip().split(" ")
        data["presenca_comissao"].append(numero[0])
        numero = Selector(text=dias[5]).xpath("//dd/text()").get().strip().split(" ")
        data["ausencia_comissao"].append(numero[0])
        numero = Selector(text=dias[4]).xpath("//dd/text()").get().strip().split(" ")
        data["ausencia_justificada_comissao"].append(numero[0])
        nascimento = Selector(text=nome[0]).xpath("//li/text()").getall()
        data["data_nascimento"].append(nascimento[4])
        gasto_total = response.css("#percentualgastocotaparlamentar").getall()
        valores = Selector(text=gasto_total[0]).xpath("//td/text()").getall()
        data["gasto_total_par"] = valores[1]
        gasto_mensal = response.css("#gastomensalcotaparlamentar").getall()
        valores = Selector(text=gasto_mensal[0]).xpath("//td/text()").getall()
        data["gasto_jan_par"].append(valores[1])
        data["gasto_fev_par"].append(valores[4])
        data["gasto_mar_par"].append(valores[7])
        data["gasto_abr_par"].append(valores[10])
        data["gasto_maio_par"].append(valores[13])
        data["gasto_junho_par"].append(valores[16])
        data["gasto_jul_par"].append(valores[19])
        data["gasto_agosto_par"].append(valores[22])
        data["gasto_set_par"].append(valores[25])
        data["gasto_out_par"].append(valores[28])
        data["gasto_nov_par"].append(valores[31])
        data["gasto_dez_par"].append(0)
        # filename = nome + ".html"
        #    with open(filename, "wb") as f:
        #        f.write(response.body)
        #    self.log(f"Saved file {filename}")
        print(
            "------------------------------------------ COMEÇO -----------------------------------------"
        )
        # print(Selector(text=nome[0]).xpath("//li/text()").getall())
        # print("------------------- POSIÇÃO 0 --------------------------")
        # print(valores)
        print("--------aaaaaa----")
        print(data)
        print(
            "------------------------------------------ FIM -----------------------------------------"
        )
        # print(Selector(text=nome[0]).xpath("//li/text()").getall())
