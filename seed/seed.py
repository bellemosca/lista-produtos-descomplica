from apps.products.models import Product

products_seed = [
    {
        "name": "Caneta Bic Azul",
        "description": "Caneta esferográfica azul, corpo transparente.",
        "price": 1.50,
    },
    {
        "name": "Lápis HB",
        "description": "Lápis preto HB, madeira resistente.",
        "price": 2.00,
    },
    {
        "name": "Borracha Branca",
        "description": "Borracha escolar branca, macia.",
        "price": 1.20,
    },
    {
        "name": "Caderno 96 folhas",
        "description": "Caderno universitário, capa dura, 96 folhas.",
        "price": 15.90,
    },
    {
        "name": "Marcador de Texto",
        "description": "Marcador de texto amarelo, ponta chanfrada.",
        "price": 4.50,
    },
    {
        "name": "Régua 30cm",
        "description": "Régua plástica transparente, 30cm.",
        "price": 3.00,
    },
    {
        "name": "Apontador Simples",
        "description": "Apontador plástico simples, diversas cores.",
        "price": 1.00,
    },
    {
        "name": "Cola Branca 90g",
        "description": "Cola branca escolar, tubo de 90g.",
        "price": 3.80,
    },
    {
        "name": "Tesoura Escolar",
        "description": "Tesoura escolar sem ponta, cabo colorido.",
        "price": 6.50,
    },
    {
        "name": "Papel Sulfite A4",
        "description": "Pacote com 100 folhas de papel sulfite A4.",
        "price": 12.00,
    },
    {
        "name": "Caneta Gel Preta",
        "description": "Caneta gel preta com escrita suave.",
        "price": 3.50,
    },
    {
        "name": "Caneta Marca-CD",
        "description": "Caneta permanente para CD/DVD.",
        "price": 4.20,
    },
    {
        "name": "Bloco de Notas 100 folhas",
        "description": "Bloco para anotações com 100 folhas.",
        "price": 7.90,
    },
    {
        "name": "Caderno 200 folhas",
        "description": "Caderno universitário com 200 folhas.",
        "price": 22.50,
    },
    {"name": "Envelope A4", "description": "Envelope pardo tamanho A4.", "price": 0.80},
    {"name": "Envelope A5", "description": "Envelope pardo tamanho A5.", "price": 0.60},
    {
        "name": "Pasta L Plástica",
        "description": "Pasta transparente tipo L.",
        "price": 2.50,
    },
    {
        "name": "Pasta Catálogo 50 plásticos",
        "description": "Pasta catálogo com 50 plásticos.",
        "price": 18.00,
    },
    {
        "name": "Grampeador Pequeno",
        "description": "Grampeador metálico pequeno.",
        "price": 9.90,
    },
    {
        "name": "Caixa de Grampos 26/6",
        "description": "Caixa com 1000 grampos padrão 26/6.",
        "price": 4.00,
    },
    {
        "name": "Clipes nº 2",
        "description": "Caixa com 100 clipes número 2.",
        "price": 3.50,
    },
    {
        "name": "Post-it Amarelo",
        "description": "Bloco adesivo 76x76mm amarelo.",
        "price": 9.00,
    },
    {
        "name": "Pincel Atômico Preto",
        "description": "Marcador permanente ponta média.",
        "price": 5.50,
    },
    {
        "name": "Lapiseira 0.5mm",
        "description": "Lapiseira mecânica 0.5mm.",
        "price": 8.50,
    },
    {
        "name": "Grafite 0.5mm HB",
        "description": "Tubo com grafites HB 0.5mm.",
        "price": 3.00,
    },
    {
        "name": "Corretivo Líquido",
        "description": "Corretivo líquido com pincel aplicador.",
        "price": 6.90,
    },
    {
        "name": "Corretivo em Fita",
        "description": "Corretivo em fita de 5mm x 6m.",
        "price": 8.90,
    },
    {
        "name": "Marca Texto Rosa",
        "description": "Marcador de texto rosa fluorescente.",
        "price": 4.50,
    },
    {
        "name": "Papel Cartão Colorido",
        "description": "Pacote com 10 folhas de papel cartão.",
        "price": 10.00,
    },
    {
        "name": "Estojo Escolar Simples",
        "description": "Estojo escolar com zíper.",
        "price": 12.50,
    },
]

for p in products_seed:
    Product.objects.create(**p)

print(f"{len(products_seed)} produtos criados!")
