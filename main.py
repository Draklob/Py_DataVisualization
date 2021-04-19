import world_population
import reading_csv_highs_lows
import dice_visual_v2
import different_dice
import eq_world_map
import python_repos_visual


# This will be a menu with several options where we can choose what we want to do.
def print_menu():
    print("[1] See world population")
    print("[2] Check temperatures for a year from Sitka in 2018")
    print("[3] Check results of rolling two dices(6) 1000 times")
    print("[4] Check results of rolling two different dices")
    print("[5] Show global earthquakes map")
    print("[6] Show most starred python projects on GitHub")


def option_1():
    world_population.run_world_population()


def option_2():
    reading_csv_highs_lows.run_script()


def option_3():
    dice_visual_v2.run_test()
    print("Check the results on a web browser.")


def option_4():
    different_dice.run_test()
    print("Remember this test creates a SVG file, open it to check the results.")


def option_5():
    print("Showing on web browser the global earthquakes.")
    eq_world_map.run_script()


def option_6():
    python_repos_visual.run_script()

print_menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        option_1()
    elif option == 2:
        option_2()
    elif option == 3:
        option_3()
    elif option == 4:
        option_4()
    elif option == 5:
        option_5()
    elif option == 6:
        option_6()
    else:
        print("Invalid option")

    print()
    print_menu()
    option = int(input("Enter your option: "))
