class Usuario:
    def __init__(self, nome, email, senha):
        """
        __init__ é a inicialização. Ela que vai definir os
        atributos internos
        """
        self.nome = nome
        self.email = email
        self.senha = senha

    def login(self, email, senha):
        """
        essa função faz o login do usuário
        """
        return self.email == email and self.senha == senha

    def __str__(self):
        """
        essa função retorna a representação de string de um usuário
        """
        return f"<Usuário: {self.email}>"


class Admin(Usuario):  # A classe admin HERDA do usuário

    # Ou seja, ela é capaz de fazer tudo o que o usuário faz

    def __init__(self, nome, email, senha):
        # Essa sintaxe esquisita é para chamar o __init__ da classe mãe, Usuario
        super().__init__(nome, email, senha)

    def administra(self):
        print("Usuário é admin!!")


# Uma classe é uma definição, uma receita parada
# Um objeto é quando uma classe é iniciada e se torna uma coisa "ativa"
# Usuario e Admin são classes

# User é um objeto da classe Usuario
user = Usuario("user", "user@gmail.com", "potato123")
print(user)

# User pode fazer login
if user.login("user@gmail.com", "potato123"):
    print("User fez login!")


admin = Admin("adm", "adm@gmail.com", "adm123")
# Ele tem o mesmo print de user pq herda dele
print(admin)

# Admin pode fazer login! Ele herda do usuario
if admin.login("adm@gmail.com", "adm123"):
    print("Admin fez login")

# E ele pode administrar tbm
admin.administra()
