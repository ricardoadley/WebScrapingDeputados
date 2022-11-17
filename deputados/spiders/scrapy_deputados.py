import pandas as pd
import scrapy
from scrapy.selector import Selector


class GetInfosSpider(scrapy.Spider):
    name = "infos_deputados"
    custom_settings = {"FEEDS": {"deputados.csv": {"format": "csv"}}}

    def to_float(self, num):
        return float(num.replace(".", "").replace(",", ".").strip())

    def start_requests(self):
        urls = [
            "https://www.camara.leg.br/deputados/204554",
            "https://www.camara.leg.br/deputados/204521",
            "https://www.camara.leg.br/deputados/204379",
            "https://www.camara.leg.br/deputados/204560",
            "https://www.camara.leg.br/deputados/121948",
            "https://www.camara.leg.br/deputados/74646",
            "https://www.camara.leg.br/deputados/141372",
            "https://www.camara.leg.br/deputados/160508",
            "https://www.camara.leg.br/deputados/136811",
            "https://www.camara.leg.br/deputados/178835",
            "https://www.camara.leg.br/deputados/160527",
            "https://www.camara.leg.br/deputados/204495",
            "https://www.camara.leg.br/deputados/204549",
            "https://www.camara.leg.br/deputados/178836",
            "https://www.camara.leg.br/deputados/160559",
            "https://www.camara.leg.br/deputados/204413",
            "https://www.camara.leg.br/deputados/204501",
            "https://www.camara.leg.br/deputados/160511",
            "https://www.camara.leg.br/deputados/178972",
            "https://www.camara.leg.br/deputados/204571",
            "https://www.camara.leg.br/deputados/105534",
            "https://www.camara.leg.br/deputados/204544",
            "https://www.camara.leg.br/deputados/160545",
            "https://www.camara.leg.br/deputados/204503",
            "https://www.camara.leg.br/deputados/178833",
            "https://www.camara.leg.br/deputados/141431",
            "https://www.camara.leg.br/deputados/92699",
            "https://www.camara.leg.br/deputados/204427",
            "https://www.camara.leg.br/deputados/204411",
            "https://www.camara.leg.br/deputados/141434",
            "https://www.camara.leg.br/deputados/191923",
            "https://www.camara.leg.br/deputados/204392",
            "https://www.camara.leg.br/deputados/204510",
            "https://www.camara.leg.br/deputados/204494",
            "https://www.camara.leg.br/deputados/204393",
            "https://www.camara.leg.br/deputados/74200",
            "https://www.camara.leg.br/deputados/115746",
            "https://www.camara.leg.br/deputados/160669",
            "https://www.camara.leg.br/deputados/204473",
            "https://www.camara.leg.br/deputados/204484",
            "https://www.camara.leg.br/deputados/204527",
            "https://www.camara.leg.br/deputados/74374",
            "https://www.camara.leg.br/deputados/204394",
            "https://www.camara.leg.br/deputados/74383",
            "https://www.camara.leg.br/deputados/204575",
            "https://www.camara.leg.br/deputados/204491",
            "https://www.camara.leg.br/deputados/74270",
            "https://www.camara.leg.br/deputados/204365",
            "https://www.camara.leg.br/deputados/160673",
            "https://www.camara.leg.br/deputados/178996",
            "https://www.camara.leg.br/deputados/198783",
            "https://www.camara.leg.br/deputados/161550",
            "https://www.camara.leg.br/deputados/207309",
            "https://www.camara.leg.br/deputados/132504",
            "https://www.camara.leg.br/deputados/204537",
            "https://www.camara.leg.br/deputados/160640",
            "https://www.camara.leg.br/deputados/204482",
            "https://www.camara.leg.br/deputados/178871",
            "https://www.camara.leg.br/deputados/178930",
            "https://www.camara.leg.br/deputados/178953",
            "https://www.camara.leg.br/deputados/211866",
            "https://www.camara.leg.br/deputados/141428",
            "https://www.camara.leg.br/deputados/68720",
            "https://www.camara.leg.br/deputados/178969",
            "https://www.camara.leg.br/deputados/141427",
            "https://www.camara.leg.br/deputados/171623",
            "https://www.camara.leg.br/deputados/204368",
            "https://www.camara.leg.br/deputados/160587",
            "https://www.camara.leg.br/deputados/66828",
            "https://www.camara.leg.br/deputados/204477",
            "https://www.camara.leg.br/deputados/72442",
            "https://www.camara.leg.br/deputados/204398",
            "https://www.camara.leg.br/deputados/204371",
            "https://www.camara.leg.br/deputados/160666",
            "https://www.camara.leg.br/deputados/212504",
            "https://www.camara.leg.br/deputados/109429",
            "https://www.camara.leg.br/deputados/141335",
            "https://www.camara.leg.br/deputados/204358",
            "https://www.camara.leg.br/deputados/178948",
            "https://www.camara.leg.br/deputados/204388",
            "https://www.camara.leg.br/deputados/141513",
            "https://www.camara.leg.br/deputados/204561",
            "https://www.camara.leg.br/deputados/204397",
            "https://www.camara.leg.br/deputados/160538",
            "https://www.camara.leg.br/deputados/74052",
            "https://www.camara.leg.br/deputados/204551",
            "https://www.camara.leg.br/deputados/204502",
            "https://www.camara.leg.br/deputados/93083",
            "https://www.camara.leg.br/deputados/204352",
            "https://www.camara.leg.br/deputados/204572",
            "https://www.camara.leg.br/deputados/178829",
            "https://www.camara.leg.br/deputados/204531",
            "https://www.camara.leg.br/deputados/178924",
            "https://www.camara.leg.br/deputados/204487",
            "https://www.camara.leg.br/deputados/141401",
            "https://www.camara.leg.br/deputados/204361",
            "https://www.camara.leg.br/deputados/178962",
            "https://www.camara.leg.br/deputados/178993",
            "https://www.camara.leg.br/deputados/204460",
            "https://www.camara.leg.br/deputados/74262",
            "https://www.camara.leg.br/deputados/204516",
            "https://www.camara.leg.br/deputados/178927",
            "https://www.camara.leg.br/deputados/178937",
            "https://www.camara.leg.br/deputados/178881",
            "https://www.camara.leg.br/deputados/204356",
            "https://www.camara.leg.br/deputados/178831",
            "https://www.camara.leg.br/deputados/74471",
            "https://www.camara.leg.br/deputados/204423",
            "https://www.camara.leg.br/deputados/133439",
            "https://www.camara.leg.br/deputados/178882",
            "https://www.camara.leg.br/deputados/204515",
            "https://www.camara.leg.br/deputados/74212",
            "https://www.camara.leg.br/deputados/160553",
            "https://www.camara.leg.br/deputados/73433",
            "https://www.camara.leg.br/deputados/141391",
            "https://www.camara.leg.br/deputados/204414",
            "https://www.camara.leg.br/deputados/160541",
            "https://www.camara.leg.br/deputados/160600",
            "https://www.camara.leg.br/deputados/159237",
            "https://www.camara.leg.br/deputados/74090",
            "https://www.camara.leg.br/deputados/74459",
            "https://www.camara.leg.br/deputados/160665",
            "https://www.camara.leg.br/deputados/160512",
            "https://www.camara.leg.br/deputados/69871",
            "https://www.camara.leg.br/deputados/178975",
            "https://www.camara.leg.br/deputados/74060",
            "https://www.camara.leg.br/deputados/178916",
            "https://www.camara.leg.br/deputados/204367",
            "https://www.camara.leg.br/deputados/204454",
            "https://www.camara.leg.br/deputados/204409",
            "https://www.camara.leg.br/deputados/160528",
            "https://www.camara.leg.br/deputados/62881",
            "https://www.camara.leg.br/deputados/160552",
            "https://www.camara.leg.br/deputados/116379",
            "https://www.camara.leg.br/deputados/73891",
            "https://www.camara.leg.br/deputados/205548",
            "https://www.camara.leg.br/deputados/204511",
            "https://www.camara.leg.br/deputados/204451",
            "https://www.camara.leg.br/deputados/178908",
            "https://www.camara.leg.br/deputados/204512",
            "https://www.camara.leg.br/deputados/204569",
            "https://www.camara.leg.br/deputados/164359",
            "https://www.camara.leg.br/deputados/204542",
            "https://www.camara.leg.br/deputados/213856",
            "https://www.camara.leg.br/deputados/160588",
            "https://www.camara.leg.br/deputados/178929",
            "https://www.camara.leg.br/deputados/160599",
            "https://www.camara.leg.br/deputados/143632",
            "https://www.camara.leg.br/deputados/160758",
            "https://www.camara.leg.br/deputados/204450",
            "https://www.camara.leg.br/deputados/204426",
            "https://www.camara.leg.br/deputados/141398",
            "https://www.camara.leg.br/deputados/204499",
            "https://www.camara.leg.br/deputados/204370",
            "https://www.camara.leg.br/deputados/178876",
            "https://www.camara.leg.br/deputados/204488",
            "https://www.camara.leg.br/deputados/141405",
            "https://www.camara.leg.br/deputados/73441",
            "https://www.camara.leg.br/deputados/204496",
            "https://www.camara.leg.br/deputados/204504",
            "https://www.camara.leg.br/deputados/205476",
            "https://www.camara.leg.br/deputados/204490",
            "https://www.camara.leg.br/deputados/141439",
            "https://www.camara.leg.br/deputados/204476",
            "https://www.camara.leg.br/deputados/204440",
            "https://www.camara.leg.br/deputados/74537",
            "https://www.camara.leg.br/deputados/141408",
            "https://www.camara.leg.br/deputados/204376",
            "https://www.camara.leg.br/deputados/204378",
            "https://www.camara.leg.br/deputados/204514",
            "https://www.camara.leg.br/deputados/178963",
            "https://www.camara.leg.br/deputados/135054",
            "https://www.camara.leg.br/deputados/204355",
            "https://www.camara.leg.br/deputados/141411",
            "https://www.camara.leg.br/deputados/74467",
            "https://www.camara.leg.br/deputados/213854",
            "https://www.camara.leg.br/deputados/204518",
            "https://www.camara.leg.br/deputados/212625",
            "https://www.camara.leg.br/deputados/204481",
            "https://www.camara.leg.br/deputados/213679",
            "https://www.camara.leg.br/deputados/204439",
            "https://www.camara.leg.br/deputados/204351",
            "https://www.camara.leg.br/deputados/178830",
            "https://www.camara.leg.br/deputados/204412",
            "https://www.camara.leg.br/deputados/204562",
            "https://www.camara.leg.br/deputados/141417",
            "https://www.camara.leg.br/deputados/134812",
            "https://www.camara.leg.br/deputados/74655",
            "https://www.camara.leg.br/deputados/204541",
            "https://www.camara.leg.br/deputados/92346",
            "https://www.camara.leg.br/deputados/204552",
            "https://www.camara.leg.br/deputados/204500",
            "https://www.camara.leg.br/deputados/178977",
            "https://www.camara.leg.br/deputados/141421",
            "https://www.camara.leg.br/deputados/141422",
            "https://www.camara.leg.br/deputados/154919",
            "https://www.camara.leg.br/deputados/204364",
            "https://www.camara.leg.br/deputados/160532",
            "https://www.camara.leg.br/deputados/204389",
            "https://www.camara.leg.br/deputados/178854",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # url = response.url
        nome = response.css("ul.informacoes-deputado").getall()
        dias = response.css("dd.list-table__definition-description").getall()
        numero = Selector(text=dias[0]).xpath("//dd/text()").get().strip().split(" ")
        ausen = Selector(text=dias[2]).xpath("//dd/text()").get().strip().split(" ")
        ausenj = Selector(text=dias[1]).xpath("//dd/text()").get().strip().split(" ")
        pcom = Selector(text=dias[3]).xpath("//dd/text()").get().strip().split(" ")
        ausenc = Selector(text=dias[5]).xpath("//dd/text()").get().strip().split(" ")
        ausencj = Selector(text=dias[4]).xpath("//dd/text()").get().strip().split(" ")
        nascimento = Selector(text=nome[0]).xpath("//li/text()").getall()
        gasto_total = response.css("#percentualgastocotaparlamentar").getall()
        valores = Selector(text=gasto_total[0]).xpath("//td/text()").getall()
        gasto_mensal = response.css("#gastomensalcotaparlamentar").getall()
        valoresm = Selector(text=gasto_mensal[0]).xpath("//td/text()").getall()
        gasto_total_gab = response.css("#percentualgastoverbagabinete").getall()
        valores_gab = Selector(text=gasto_total_gab[0]).xpath("//td/text()").getall()
        gasto_mensal_gab = response.css("#gastomensalverbagabinete").getall()
        valores_gab_mensal = (
            Selector(text=gasto_mensal_gab[0]).xpath("//td/text()").getall()
        )
        beneficios = response.css("div.beneficio").getall()
        valores_beneficios = Selector(text=beneficios[1]).xpath("//a/text()").getall()
        valor_formatado = valores_beneficios[1].strip().split("R$")
        valor_formatado = valor_formatado[1].strip()
        qtd_viag = Selector(text=beneficios[4]).xpath("//span/text()").getall()
        nome_formatado = Selector(text=nome[0]).xpath("//li/text()").get()
        yield {
            "nome": nome_formatado if nome_formatado else "",
            "genero": "M",
            "presença_plenario": numero[0] if numero[0:] else "",
            "ausencia_plenario": ausen[0] if ausen[0:] else "",
            "ausencia_justificada_plenario": ausenj[0] if ausenj[0:] else "",
            "presenca_comissao": pcom[0] if pcom[0:] else "",
            "ausencia_comissao": ausenc[0] if ausenc[0:] else "",
            "ausencia_justificada_comissao": ausencj[0] if ausencj[0:] else "",
            "data_nascimento": nascimento[4] if nascimento[4:] else "",
            "gasto_total_par": self.to_float(valores[1]) if valores[1:] else "",
            "gasto_jan_par": self.to_float(valoresm[1]) if valoresm[1:] else "",
            "gasto_fev_par": self.to_float(valores[4]) if valores[4:] else "",
            "gasto_mar_par": self.to_float(valores[7]) if valores[7:] else "",
            "gasto_abr_par": self.to_float(valores[10]) if valores[10:] else "",
            "gasto_maio_par": self.to_float(valores[13]) if valores[13:] else "",
            "gasto_junho_par": self.to_float(valores[16]) if valores[16:] else "",
            "gasto_jul_par": self.to_float(valores[19]) if valores[19:] else "",
            "gasto_agosto_par": self.to_float(valores[22]) if valores[22:] else "",
            "gasto_set_par": self.to_float(valores[25]) if valores[25:] else "",
            "gasto_out_par": self.to_float(valores[28]) if valores[28:] else "",
            "gasto_nov_par": self.to_float(valores[31]) if valores[31:] else "",
            "gasto_dez_par": 0,
            "gasto_total_gab": self.to_float(valores_gab[1]) if valores_gab[1:] else "",
            "gasto_jan_gab": self.to_float(valores_gab_mensal[1])
            if valores_gab_mensal[1:]
            else "",
            "gasto_fev_gab": self.to_float(valores_gab_mensal[4])
            if valores_gab_mensal[4:]
            else "",
            "gasto_mar_gab": self.to_float(valores_gab_mensal[7])
            if valores_gab_mensal[7:]
            else "",
            "gasto_abr_gab": self.to_float(valores_gab_mensal[10])
            if valores_gab_mensal[10:]
            else "",
            "gasto_maio_gab": self.to_float(valores_gab_mensal[13])
            if valores_gab_mensal[13:]
            else "",
            "gasto_junho_gab": self.to_float(valores_gab_mensal[16])
            if valores_gab_mensal[16:]
            else "",
            "gasto_jul_gab": self.to_float(valores_gab_mensal[19])
            if valores_gab_mensal[19:]
            else "",
            "gasto_agosto_gab": self.to_float(valores_gab_mensal[22])
            if valores_gab_mensal[22:]
            else "",
            "gasto_set_gab": self.to_float(valores_gab_mensal[25])
            if valores_gab_mensal[25:]
            else "",
            "gasto_out_gab": self.to_float(valores_gab_mensal[28])
            if valores_gab_mensal[28:]
            else "",
            "gasto_nov_gab": self.to_float(valores_gab_mensal[31])
            if valores_gab_mensal[31:]
            else "",
            "gasto_dez_gab": self.to_float(valores_gab_mensal[34])
            if valores_gab_mensal[34:]
            else "",
            "salario_bruto_par": self.to_float(valor_formatado)
            if valor_formatado
            else "",
            "quant_viagem": qtd_viag[0] if qtd_viag[0:] else "",
        }
