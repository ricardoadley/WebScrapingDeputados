import pandas as pd
import scrapy
from scrapy.selector import Selector


class GetInfosSpider(scrapy.Spider):
    name = "infos_deputadas"
    custom_settings = {"FEEDS": {"deputadas.csv": {"format": "csv"}}}

    def to_float(self, num):
        return float(num.replace(".", "").replace(",", ".").strip())

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
        print("--------------aaaaaaaaaaaaaaaaaaa----------")
        print(valores[1])
        print("-------------------bbbbbbbbbbbb------------------")
        yield {
            "nome": nome_formatado if nome_formatado else "",
            "genero": "F",
            "presença_plenario": numero[0] if numero[0:] else "",
            "ausencia_plenario": ausen[0] if ausen[0:] else "",
            "ausencia_justificada_plenario": ausenj[0] if ausenj[0:] else "",
            "presenca_comissao": pcom[0] if pcom[0:] else "",
            "ausencia_comissao": ausenc[0] if ausenc[0:] else "",
            "ausencia_justificada_comissao": ausencj[0] if ausencj[0:] else "",
            "data_nascimento": nascimento[4] if nascimento[4:] else "",
            "gasto_total_par": self.to_float(valores[1]) if valores[1:] else "",
            "gasto_jan_par": self.to_float(valoresm[1]) if valoresm[1:] else "",
            "gasto_fev_par": self.to_float(valoresm[4]) if valoresm[4:] else "",
            "gasto_mar_par": self.to_float(valoresm[7]) if valoresm[7:] else "",
            "gasto_abr_par": self.to_float(valoresm[10]) if valoresm[10:] else "",
            "gasto_maio_par": self.to_float(valoresm[13]) if valoresm[13:] else "",
            "gasto_junho_par": self.to_float(valoresm[16]) if valoresm[16:] else "",
            "gasto_jul_par": self.to_float(valoresm[19]) if valoresm[19:] else "",
            "gasto_agosto_par": self.to_float(valoresm[22]) if valoresm[22:] else "",
            "gasto_set_par": self.to_float(valoresm[25]) if valoresm[25:] else "",
            "gasto_out_par": self.to_float(valoresm[28]) if valoresm[28:] else "",
            "gasto_nov_par": self.to_float(valoresm[31]) if valoresm[31:] else "",
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


import pandas as pd
import scrapy
from scrapy.selector import Selector


class GetInfosSpider(scrapy.Spider):
    name = "infos_deputadas"
    custom_settings = {"FEEDS": {"deputadas.csv": {"format": "csv"}}}

    def to_float(self, num):
        return float(num.replace(".", "").replace(",", ".").strip())

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
        print("--------------aaaaaaaaaaaaaaaaaaa----------")
        print(valores[1])
        print("-------------------bbbbbbbbbbbb------------------")
        yield {
            "nome": nome_formatado if nome_formatado else "",
            "genero": "F",
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
