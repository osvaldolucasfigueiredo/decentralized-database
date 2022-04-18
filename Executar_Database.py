#  If the program does terminal interaction, make it output a short
#notice like this when it starts in an interactive mode:
#
#    decentralized-database Copyright (C) 2022 Osvaldo Lucas da Silva Figueiredo
#    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; type `show c' for details.
#
#The hypothetical commands `show w' and `show c' should show the appropriate
#parts of the General Public License.  Of course, your program's commands
#might be different; for a GUI interface, you would use an "about box".
#
#  You should also get your employer (if you work as a programmer) or school,
#if any, to sign a "copyright disclaimer" for the program, if necessary.
#For more information on this, and how to apply and follow the GNU GPL, see
#<https://www.gnu.org/licenses/>.
#
#  The GNU General Public License does not permit incorporating your program
#into proprietary programs.  If your program is a subroutine library, you
#may consider it more useful to permit linking proprietary applications with
#the library.  If this is what you want to do, use the GNU Lesser General
#Public License instead of this License.  But first, please read
#<https://www.gnu.org/licenses/why-not-lgpl.html>.


from Gerador_de_Blocos import*

def principal():
#Primeiro Grupo de Blocos
    x = Criador_de_Blocos()
    x.criar()
    x.novo_bloco("Primeirosso")
    x.novo_bloco("O céu resplandece ao meu redor, ao meu redor, vou vuar e as estrelas")
    w = 0
    c = len(x.arquivo)
    while(w < c):
        print(x.descriptar_bloco(x.arquivo[w]))
        w = w + 1
    print(x.chave_cripto, " - ", x.chave_criacao)

#Segundo Grupo de Blocos
    xy = Criador_de_Blocos()
    xy.criar()
    xy.novo_bloco("Primeirosso")
    xy.novo_bloco("O céu resplandece ao meu redor, ao meu redor, vou vuar e as estrelas")
    wy = 0
    cy = len(xy.arquivo)
    while(wy < cy):
        print(xy.descriptar_bloco(xy.arquivo[wy]))
        wy = wy + 1
    print(xy.chave_cripto, " - ", xy.chave_criacao)

if __name__ == '__main__':
    principal()