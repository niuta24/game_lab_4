import random
import game_lviv


kozelnytska_street = game_lviv.Street("вул. Козельницька")
kozelnytska_street.set_description("Свого роду Alma Mater для студентів УКУ.")

stryiska_street = game_lviv.Street("вул. Стрийська")
stryiska_street.set_description("Одна з найдовших вулиць Львова. Веде вас від Сокільників до центру")

franka_street = game_lviv.Street("вул. І.Франка")
franka_street.set_description("Прекрасна вулиця на честь одного з найвидатніших українських культурних діячів")

rustaveli_street = game_lviv.Street("вул. Шота Руставелі")
rustaveli_street.set_description("Ходять плітки, що лише 2% населення Львова знає, на честь кого названа ця вулиця)")

krakivska_street = game_lviv.Street("вул. Краківська")
krakivska_street.set_description("Ви йдете по вулиці, названій на честь польсокого міста. А ви знали, що у Кракові є вулиця Львівська!")

kozelnytska_street.link_street
kozelnytska_street.link_street(stryiska_street, "захід")
kozelnytska_street.link_street(franka_street, "схід")
stryiska_street.link_street(kozelnytska_street, "схід")
stryiska_street.link_street(rustaveli_street, "північ")
franka_street.link_street(rustaveli_street, "північ")
franka_street.link_street(kozelnytska_street, "захід")
rustaveli_street.link_street(stryiska_street, "південь")
rustaveli_street.link_street(franka_street, "захід")
rustaveli_street.link_street(krakivska_street, "північ")
krakivska_street.link_street(rustaveli_street, "південь")

hopnik = game_lviv.Enemy("Гопнік", "Чоловік у характерних спротівках, який може віджати у вас телефон(ймовірно, він з Троєщини)")
hopnik.set_conversation("Привіт! Як справи?")
hopnik.set_weakness("семочки")
franka_street.set_character(hopnik)

romu = game_lviv.Enemy("Роми", "Маленькі дітки-роми, які співають 'Ой у лузі червона калина' і просять грошей.")
romu.set_conversation("Мені потрібні гроші!")
romu.set_weakness("гроші")
rustaveli_street.set_character(romu)

bar = game_lviv.Enemy("Бар", "Львів - гастрономічна столиця України. Є шанс, що тобі доведеться витратити усі гроші тут.")
bar.set_conversation("Що бажаєте випити?")
bar.set_weakness("мізки")
krakivska_street.set_character(bar)

money = game_lviv.Item("гроші")
money.set_description("Трохи грошей ще ніколи нікому не завадили")
stryiska_street.set_item(money)

semochki = game_lviv.Item("семочки")
semochki.set_description("Солоні семочки з прекрасних полів Херсонщини! Якщо ти їх з'їш, то зможеш віджати у гопника телефон")
kozelnytska_street.set_item(semochki)

brain = game_lviv.Item("мізки")
brain.set_description("Візьми мізки, вони тобі точно стануть у нагоді!")
rustaveli_street.set_item(brain)

current_street = kozelnytska_street
backpack = []

dead = False
print("Привіт! Твоя задача у цій грі перемогти 2х з 3х захованих небезпек. Ти можеш перемогти їх, якщо маєш при собі предемети, необхідні для перемоги. Якщо ти обрав неправильний предмет для бою із монстром - ти програв і маєш почати спочатку")
defeated = 0
while dead == False:
    print("\n")
    current_street.get_details()
    
    item = current_street.get_item()
    if item is not None:
        item.describe()
        print("Що ти зробиш з " + item.get_name() + "? (взяти/покинути)")
        command = input("> ")
        if command == "взяти":
            print("Ти поклав " + item.get_name() + " у свій рюкзак")
            backpack.append(item.get_name())
            current_street.set_item(None)
        else:
            print("Ти нічого не взяв! Йди далі...")

    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        print("Ти зустрів монстра: будеш битись чи спробуєш втекти?")
        command = input("> ")
        if command == "битись":
            # Fight with the inhabitant, if there is one
            print("Що ти візьмеш з собою в бій?")
            fight_with = input()
            if backpack == []:
                print("Мені шкода, але ти програв, бо твій рюкзак пустий.")
                print("Кінець гри!")
                dead = True
                quit()

            # Do I have this item?
            if fight_with in backpack:
                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    defeated += 1 
                    print("Ти переміг і можеш продовжити свою прогулянку!")
                    current_street.character = None
                    if defeated == 2:
                        print("Вітання! Ви змогли перемогти усіх негідників на вулицях міста Лева")
                        dead = True
                        quit()
                else:
                    # What happens if you lose?
                    print("Мені шкода, але ти програв і не можеш продовжити свою прогулянку.")
                    print("Кінець гри!")
                    dead = True
                    quit()
            else:
                print("У тебе немає " + fight_with)
        elif command == "втекти":
            print("Щоб втекти, на кубіку тобі має випасти 4 або 5, інакше, ти програв")
            point = random.randint(1, 6)
            if point == 4 or point == 5:
                print("Ти втек з місця події")
                current_street.character = None
            else:
                print("Мені шкода, але ти програв і не можеш продовжити свою прогулянку.")
                print("Кінець гри!")
                dead = True 
                quit()      
    command = input("> ")

    if command in ["північ", "південь", "захід", "схід"]:
        # Move in the given direction
        current_street = current_street.move(command)      
    else:
        print("Я не знаю, що таке " + command)