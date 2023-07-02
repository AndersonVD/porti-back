from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from spiders.g1 import g1
from spiders.justwatch import justwatch
from spiders.mercadolivre import mercadoLivre

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/g1")
def get_g1(busca: str):
    return g1(busca)
    # return dummy_g1


@app.get("/meli")
def get_meli(busca: str):
    # return dummy_meli
    return mercadoLivre(busca)


@app.get("/filmes")
def get_filmes(busca: str):
    # return dummy_filmes
    return justwatch(busca)


dummy_g1 = [
    {
        "id": 1,
        "title": "'BBB': Relembre participantes que já foram desclassificados do reality",
        "time_ago": "há 2 dias",
        "image": "https://s2.glbimg.com/G_rpmSVflbgS-JzPNB3LlqY4fwQ=/346x195/smart/http%3A//i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2022/3/J/euR4BaTmqdVopgq1dlLQ/balde-2.jpeg",
        "link": "https://g1.globo.com/busca/click?q=bbb&p=2&r=1679288041708&u=https%3A%2F%2Fg1.globo.com%2Fpop-arte%2Ftv-e-series%2Fnoticia%2F2023%2F03%2F17%2Fbbb-relembre-participantes-que-ja-foram-desclassificados-do-reality.ghtml&syn=False&key=f889ed01e6ac4825fb7e393a20cc72b9"
    },
    {
        "id": 2,
        "title": "‘Pessoas que menstruam’ x ‘mulheres que menstruam’: entenda polêmica que levou ex-BBB a ser denunciada por transfobia na UFMG",
        "time_ago": "há 1 dia",
        "image": "https://s2.glbimg.com/UjV-RLCLJZZG_V89GVdrBd1KBaw=/346x195/smart/http%3A//i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2023/F/B/HCjj2OTvAWhzk8IJeiRg/microsoftteams-image-25-.png",
        "link": "https://g1.globo.com/busca/click?q=bbb&p=3&r=1679288041712&u=https%3A%2F%2Fg1.globo.com%2Feducacao%2Fnoticia%2F2023%2F03%2F18%2Fpessoas-que-menstruam-x-mulheres-que-menstruam-entenda-polemica-que-levou-ex-bbb-a-ser-denunciada-por-transfobia-na-ufmg.ghtml&syn=False&key=20e305c1c7e1bb2caa5fd0c9977c0f0d"
    },
    {
        "id": 3,
        "title": "De festa do líder a investigação por importunação sexual: entenda o caso que levou à eliminação de Guimê e Cara de Sapato do 'BBB 23'",
        "time_ago": "há 1 dia",
        "image": "https://s2.glbimg.com/riVijrL7znXl9e5sO9FVKy7M5w4=/346x195/smart/http%3A//i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2023/8/z/tJArVXRJiJzJo5H6lzzw/expulsos.jpg",
        "link": "https://g1.globo.com/busca/click?q=bbb&p=4&r=1679288041716&u=https%3A%2F%2Fg1.globo.com%2Fpop-arte%2Ftv-e-series%2Fnoticia%2F2023%2F03%2F18%2Fde-festa-do-lider-a-investigacao-por-importunacao-sexual-entenda-o-caso-que-levou-a-eliminacao-de-guime-e-cara-de-sapato-do-bbb-23.ghtml&syn=False&key=2d8cc5eda67843a8c78d3edc97e16835"
    },
    {
        "id": 5,
        "title": "Ex-BBB e professora, Mara Telles critica expressão 'pessoas que menstruam' e é denunciada por transfobia na UFMG",
        "time_ago": "há 1 dia",
        "image": "https://s2.glbimg.com/UjV-RLCLJZZG_V89GVdrBd1KBaw=/346x195/smart/http%3A//i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2023/F/B/HCjj2OTvAWhzk8IJeiRg/microsoftteams-image-25-.png",
        "link": "https://g1.globo.com/busca/click?q=bbb&p=6&r=1679288041722&u=https%3A%2F%2Fg1.globo.com%2Feducacao%2Fnoticia%2F2023%2F03%2F16%2Fex-bbb-e-professora-mara-telles-critica-expressao-pessoas-que-menstruam-e-e-denunciada-por-transfobia-na-ufmg.ghtml&syn=False&key=280f6e675e53501eb62a2c34e3b3fa55"
    },
    {
        "id": 6,
        "title": "'BBB 23': Dania Mendez, participante mexicana, deixa casa",
        "time_ago": "há 2 dias",
        "image": "https://s2.glbimg.com/freS5QC4BzX6Xiwu0TPThFQrqbI=/346x195/smart/http%3A//i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2023/l/I/BVT2qxTZOoOsKQ59saVg/bbb23-dania5.jpg",
        "link": "https://g1.globo.com/busca/click?q=bbb&p=7&r=1679288041727&u=https%3A%2F%2Fg1.globo.com%2Fpop-arte%2Ftv-e-series%2Fnoticia%2F2023%2F03%2F17%2Fbbb-23-dania-mendez-participante-mexicana-deixa-casa.ghtml&syn=False&key=cfffcab5f3aa516fde20646d16120034"
    },
    {
        "id": 7,
        "title": "'BBB 23': Famosos repercutem eliminação de Guimê e Cara de Sapato",
        "time_ago": "há 2 dias",
        "image": "https://s2.glbimg.com/SSAG2GWc0eoGhD3eVdIIc7qfx6A=/346x195/smart/http%3A//i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2023/w/Y/Tx6I8oSjeAHD8aUbBkxQ/sapatoeguime.jpg",
        "link": "https://g1.globo.com/busca/click?q=bbb&p=8&r=1679288041731&u=https%3A%2F%2Fg1.globo.com%2Fpop-arte%2Fnoticia%2F2023%2F03%2F17%2Fbbb-23-famosos-repercutem-eliminacao-de-guime-e-cara-de-sapato.ghtml&syn=False&key=30b991dc2f98e36ac8e859d6d0ff79c9"
    },
    {
        "id": 8,
        "title": "Resumão diário #507: Consignado suspenso, e eliminação no BBB",
        "time_ago": "há 2 dias",
        "image": "https://s2.glbimg.com/-8APOHU933wSlRTSKE_BaW1uaHY=/346x195/smart/http%3A//i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2019/Z/P/3DBiGATciJvvQc3jv7iw/podcasts-3000x1688-sem-logo-14.png",
        "link": "https://g1.globo.com/busca/click?q=bbb&p=9&r=1679288041736&u=https%3A%2F%2Fg1.globo.com%2Fpodcast%2Fresumao-diario%2Fnoticia%2F2023%2F03%2F17%2Fresumao-diario-507-consignado-suspenso-e-eliminacao-no-bbb.ghtml&syn=False&key=82800d0cf1f77e9c378bce5c9bc1cb35"
    },
    {
        "id": 9,
        "title": "MC Guimê volta a falar sobre eliminação do BBB e pede desculpas a Lexa, Dania e Bruna",
        "time_ago": "há 2 dias",
        "image": "https://s2.glbimg.com/riVijrL7znXl9e5sO9FVKy7M5w4=/346x195/smart/http%3A//i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2023/8/z/tJArVXRJiJzJo5H6lzzw/expulsos.jpg",
        "link": "https://g1.globo.com/busca/click?q=bbb&p=10&r=1679288041740&u=https%3A%2F%2Fg1.globo.com%2Fpop-arte%2Ftv-e-series%2Fnoticia%2F2023%2F03%2F17%2Fmc-guime-volta-a-falar-sobre-eliminacao-do-bbb-e-pede-desculpas-a-lexa-dania-e-bruna.ghtml&syn=False&key=02f94b5ec57fd9f8c49b13722a84a0c8"
    }
]


dummy_filmes = [
    {
        "id": 0,
        "title": "Vingadores: Endgame",
        "image": "https://www.justwatch.com/images/poster/121475856/s166/vingadores-endgame",
        "link": "https://www.justwatch.com/br/filme/vingadores-endgame"
    },
    {
        "id": 1,
        "title": "Vingadores: Guerra do Infinito",
        "image": "https://www.justwatch.com/images/poster/72283477/s166/vingadores-guerra-do-infinito",
        "link": "https://www.justwatch.com/br/filme/vingadores-guerra-do-infinito"
    },
    {
        "id": 2,
        "title": "Vingadores: A Era de Ultron",
        "image": "https://www.justwatch.com/images/poster/243496298/s166/vingadores-era-de-ultron",
        "link": "https://www.justwatch.com/br/filme/vingadores-era-de-ultron"
    },
    {
        "id": 3,
        "title": "Os Vingadores",
        "image": "https://www.justwatch.com/images/poster/176276653/s166/marvels-the-avengers",
        "link": "https://www.justwatch.com/br/filme/marvels-the-avengers"
    },
    {
        "id": 4,
        "title": "Vingadores: Guerras Secretas",
        "image": "https://www.justwatch.com/images/poster/293933922/s166/avengers-secret-wars",
        "link": "https://www.justwatch.com/br/filme/avengers-secret-wars"
    }
]

dummy_meli = [
    {
        "id": 1,
        "title": "Salgadinho de Milho Queijo Nacho Doritos Pacote 300g",
        "price": "22",
        "image": "https://http2.mlstatic.com/D_NQ_NP_675263-MLU48286472961_112021-V.webp",
        "link": "https://www.mercadolivre.com.br/salgadinho-de-milho-queijo-nacho-doritos-pacote-300g/p/MLB18407378?pdp_filters=category:MLB1403#searchVariation=MLB18407378&position=2&search_layout=stack&type=product&tracking_id=f9c11da6-ed45-4eba-ac56-0b35bf400c6b"
    },
    {
        "id": 2,
        "title": "Macarrão Instantâneo Queijo Cheddar Cup Noodles Copo 69g",
        "price": "4",
        "image": "https://http2.mlstatic.com/D_NQ_NP_654666-MLA46811227415_072021-V.webp",
        "link": "https://www.mercadolivre.com.br/macarro-instantneo-queijo-cheddar-cup-noodles-copo-69g/p/MLB18310345?pdp_filters=category:MLB1403#searchVariation=MLB18310345&position=3&search_layout=stack&type=product&tracking_id=f9c11da6-ed45-4eba-ac56-0b35bf400c6b"
    },
    {
        "id": 3,
        "title": "Pão De Frigideira Proteico Queijo E Ervas My Dream 350g",
        "price": "59",
        "image": "https://http2.mlstatic.com/D_NQ_NP_679045-MLB50502963425_062022-V.webp",
        "link": "https://produto.mercadolivre.com.br/MLB-2697181463-po-de-frigideira-proteico-queijo-e-ervas-my-dream-350g-_JM#position=14&search_layout=stack&type=item&tracking_id=f9c11da6-ed45-4eba-ac56-0b35bf400c6b"
    },
    {
        "id": 4,
        "title": "Queijo Parmesão Ralado Tirolez Pacote 100g",
        "price": "13",
        "image": "https://http2.mlstatic.com/D_NQ_NP_749285-MLB47797138724_102021-V.webp",
        "link": "https://produto.mercadolivre.com.br/MLB-2048408470-queijo-parmeso-ralado-tirolez-pacote-100g-_JM#position=15&search_layout=stack&type=item&tracking_id=f9c11da6-ed45-4eba-ac56-0b35bf400c6b"
    },
    {
        "id": 5,
        "title": "Snack de Arroz Kalassi queijo sem glúten 100 g",
        "price": "16",
        "image": "https://http2.mlstatic.com/D_NQ_NP_816205-MLU48285780787_112021-V.webp",
        "link": "https://www.mercadolivre.com.br/snack-de-arroz-kalassi-queijo-sem-gluten-100-g/p/MLB17849758?pdp_filters=category:MLB1403#searchVariation=MLB17849758&position=4&search_layout=stack&type=product&tracking_id=f9c11da6-ed45-4eba-ac56-0b35bf400c6b"
    },
    {
        "id": 6,
        "title": "Snack de Arroz Kalassi queijo e cebola sem glúten 100 g",
        "price": "16",
        "image": "https://http2.mlstatic.com/D_NQ_NP_900260-MLU48286347839_112021-V.webp",
        "link": "https://www.mercadolivre.com.br/snack-de-arroz-kalassi-queijo-e-cebola-sem-gluten-100-g/p/MLB17850056?pdp_filters=category:MLB1403#searchVariation=MLB17850056&position=5&search_layout=stack&type=product&tracking_id=f9c11da6-ed45-4eba-ac56-0b35bf400c6b"
    },
    {
        "id": 7,
        "title": "Queijo Parmesão Ralado Faixa Azul Vigor Pacote 100g",
        "price": "16",
        "image": "https://http2.mlstatic.com/D_NQ_NP_801889-MLB47797138763_102021-V.webp",
        "link": "https://produto.mercadolivre.com.br/MLB-2048291749-queijo-parmeso-ralado-faixa-azul-vigor-pacote-100g-_JM#position=16&search_layout=stack&type=item&tracking_id=f9c11da6-ed45-4eba-ac56-0b35bf400c6b"
    },
    {
        "id": 8,
        "title": "Snack de Trigo Eqlibri Panetini queijo suave 105 g",
        "price": "8",
        "image": "https://http2.mlstatic.com/D_NQ_NP_833842-MLU48321596355_112021-V.webp",
        "link": "https://www.mercadolivre.com.br/snack-de-trigo-eqlibri-panetini-queijo-suave-105-g/p/MLB17849836?pdp_filters=category:MLB1403#searchVariation=MLB17849836&position=6&search_layout=stack&type=product&tracking_id=f9c11da6-ed45-4eba-ac56-0b35bf400c6b"
    },
    {
        "id": 9,
        "title": "Salgadinho de Milho Doritos queijo nacho 210 g",
        "price": "20",
        "image": "https://http2.mlstatic.com/D_NQ_NP_927020-MLU48286071504_112021-V.webp",
        "link": "https://www.mercadolivre.com.br/salgadinho-de-milho-doritos-queijo-nacho-210-g/p/MLB17850052?pdp_filters=category:MLB1403#searchVariation=MLB17850052&position=7&search_layout=stack&type=product&tracking_id=f9c11da6-ed45-4eba-ac56-0b35bf400c6b"
    }
]
