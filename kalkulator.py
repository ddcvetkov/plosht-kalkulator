def izchisli_plosht(dulzhina, shirochina):
    return dulzhina * shirochina

def main():
    print("Калкулатор за площ на правоъгълник")
    d = float(input("Въведи дължина: "))
    s = float(input("Въведи широчина: "))
    plosht = izchisli_plosht(d, s)
    print(f"Площта е: {plosht} кв. единици")

if __name__ == "__main__":
    main()
