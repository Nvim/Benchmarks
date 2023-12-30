# $@ = nom cible
# $< = nom premiere dépendance
# $^ = liste des dépendances
# $? = liste des dépendances plus récentes que la cible (? pas capté)
# $* = nom du fichier dans extension

# --------------------------------------------- VARIABLES -------------------------------------------

project_path := $(CURDIR)

CC=gcc
FLAGS=-O3
LINK_FLAGS=$(project_path)/lib/*.so
SRC=src
OBJ=obj
LIB=lib
BIN=bin/main

#tous les fichiers .c dans le dossier src:
SRCS=$(wildcard $(SRC)/*.c)

#tous les fichiers .c dans le dossier src/sort:
SORT_SRCS=$(wildcard $(SRC)/sort/*.c)

#remplace les occurences d'un src/fichier.c par un obj/fichier.o, pour tous les fichiers du dossier src
# => Dans le dossier obj, fichiers ayant le même nom que les fichiers du dossier src, mais avec l'extension .o
OBJS=$(patsubst $(SRC)/%.c, $(OBJ)/%.o, $(SRCS)) 
SORT_OBJS=$(patsubst $(SRC)/sort/%.c, $(OBJ)/%.o, $(SORT_SRCS))

LIBS=$(patsubst $(SRC)/sort/%.c, $(LIB)/lib%.so, $(SORT_SRCS)) 

all: $(BIN) #on veut créer l'éxécutable ./bin/debug/main
libs: $(LIBS) 
objs: $(OBJS) $(SORT_OBJS)

# --------------------------------------------- COMMANDS -------------------------------------------

#	~3e COMMANDE: 
#Création de l'éxécutable BIN à partir de OBJS: fichiers.o de ./obj, ayant les mêmes noms que les fichiers.c de ./src (linking)

#gcc obj/*.o -o bin/main -(link flags)
$(BIN): $(OBJS) $(SORT_OBJS) $(LIBS)
	$(CC) $(FLAGS) $(OBJ)/*.o -o $@ $(LINK_FLAGS)

#-Wl,-rpath,./lib
# Création des bibliothèques partagées à partir des fichiers.c du dossier ./src/sort 
#gcc -shared -O3 -o lib/lib%.so src/sort/%.c
$(LIB)/lib%.so: $(OBJ)/%.o
	$(CC) -shared $(FLAGS) -o $@ $< 

#	~2e COMMANDE: 
#Création des fichiers objets à partir des fichiers.c du dossier ./src (compiling)
#gcc -c src/%.c -O3 -o obj/%.o
$(OBJ)/%.o: $(SRC)/%.c
	$(CC) -c $< $(FLAGS) -o $@	

# ~1e COMMANDE:
# Création des fichiers objets à partir des fichiers.c du dossier ./src/sort (compiling)
#gcc -c src/sort/%.c -O3 -o obj/%.o
$(OBJ)/%.o: $(SRC)/sort/%.c
	$(CC) -c $< $(FLAGS) -o $@


#	~Nettoyage:
clean:
	rm $(OBJ)/*.o
	rm $(LIB)/*.so
	rm bin/*
