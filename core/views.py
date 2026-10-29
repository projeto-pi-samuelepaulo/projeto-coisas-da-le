from django.shortcuts import render


def home(request):
    produtos = [
        {
            "id": 1,
            "nome": "Camiseta Básica",
            "categoria": "Casual",
            "preco": "89.90",
            "tamanho": "M",
            "descricao": "Camiseta confortável, ideal para o dia a dia com um corte moderno.",
            "cor": "Preta",
            "imagem": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=900&q=80",
        },
        {
            "id": 2,
            "nome": "Jaqueta Denim",
            "categoria": "Outerwear",
            "preco": "249.90",
            "tamanho": "G",
            "descricao": "Jaqueta em denim com acabamento sofisticado e visual versátil.",
            "cor": "Azul",
            "imagem": "https://images.unsplash.com/photo-1529139574466-a303027c1d8b?auto=format&fit=crop&w=900&q=80",
        },
        {
            "id": 3,
            "nome": "Calça Slim",
            "categoria": "Calças",
            "preco": "139.90",
            "tamanho": "P",
            "descricao": "Modelagem slim, elastano leve e caimento confortável para qualquer ocasião.",
            "cor": "Cinza",
            "imagem": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=900&q=80",
        },
    ]
    return render(request, "index.html", {"produtos": produtos})


def produto(request, produto_id):
    produtos = [
        {
            "id": 1,
            "nome": "Camiseta Básica",
            "categoria": "Casual",
            "preco": "89.90",
            "tamanho": "M",
            "descricao": "Camiseta confortável, ideal para o dia a dia com um corte moderno.",
            "cor": "Preta",
            "imagem": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=900&q=80",
        },
        {
            "id": 2,
            "nome": "Jaqueta Denim",
            "categoria": "Outerwear",
            "preco": "249.90",
            "tamanho": "G",
            "descricao": "Jaqueta em denim com acabamento sofisticado e visual versátil.",
            "cor": "Azul",
            "imagem": "https://images.unsplash.com/photo-1529139574466-a303027c1d8b?auto=format&fit=crop&w=900&q=80",
        },
        {
            "id": 3,
            "nome": "Calça Slim",
            "categoria": "Calças",
            "preco": "139.90",
            "tamanho": "P",
            "descricao": "Modelagem slim, elastano leve e caimento confortável para qualquer ocasião.",
            "cor": "Cinza",
            "imagem": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=900&q=80",
        },
    ]

    produto_selecionado = next(
        (item for item in produtos if item["id"] == produto_id),
        produtos[0],
    )

    return render(request, "product.html", {"produto": produto_selecionado})
