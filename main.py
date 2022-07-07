import color
from pygame_stuff import start_pygame


def main():
    # generate colors
    col = color.rand_color()
    complement = col.complementary_color()

    analogous = [col.analogous_color(0), col.analogous_color(1), col.analogous_color(-1)]

    # split_complement = [col, col.split_complementary_color(1), col.split_complementary_color(-1)]
    split_complement = []
    split_complement.append(col)
    split_complement.append(col.split_complementary_color(1))
    split_complement.append(col.split_complementary_color(-1))

    # triad = [col, col.triad_color(1), col.triad_color(-1)]
    triad = []
    triad.append(col)
    triad.append(col.triad_color(1))
    triad.append(col.triad_color(-1))

    # tetradic = [col.tetradic_color(0), col.tetradic_color(1), col.tetradic_color(3), col.tetradic_color(-2)]
    tetradic = []
    tetradic.append(col.tetradic_color(0))
    tetradic.append(col.tetradic_color(1))
    tetradic.append(col.tetradic_color(3))
    tetradic.append(col.tetradic_color(-2))

    print("Color: ", col)
    print("Complement: ", complement)
    print("Analogous: ", analogous)
    print("Split complement: ", split_complement)
    print("Triad: ", triad)
    print("Tetradic: ", tetradic)

    colors = [col] + [complement] + analogous + split_complement + triad + tetradic
    start_pygame(colors)


if __name__ == '__main__':
    main()
