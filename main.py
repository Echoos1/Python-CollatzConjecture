import winsound

def main():
    #start = int(input("Start Number: "))
    #op = start
    max_steps = 50000
    max_opmain = 10000000
    result_txt = open("results.txt", "w")
    opmain = int(0)

    max_num_test = 0
    max_stat_test = 0

    step_max_stat = 0
    step_max_op = 0
    step_max_num = 0
    num_max_stat = 0
    num_max_op = 0
    num_max_num = 0

    total_comps = 0

    for i1 in range(max_opmain):
        if max_stat_test > step_max_stat:
            step_max_stat = max_stat_test
            step_max_op = opmain
            step_max_num = max_num_test
        else:
            pass
        if max_num_test > num_max_num:
            num_max_num = max_num_test
            num_max_op = opmain
            num_max_stat = max_stat_test
        else:
            pass

        opmain = int(opmain + 1)
        op = opmain
        max_num = 0

        for i2 in range(max_steps):
            if op > max_num:
                max_num = op
            else:
                pass

            if op == 1:
                # 1 is the end of the sequence. Any number here will loop between 4, 2, and 1.
                # print(f'Done! {int(opmain)} finished the sequence after {i2} steps!')
                max_stat_test = i2
                max_num_test = max_num
                total_comps = total_comps + i2
                result_txt.write(f'{int(opmain)}:\t\t {i2} steps;\t\t {max_num} reached\n')
                break
            elif (op % 2) == 0:
                # operation for even number
                op = op / 2
            elif (op % 2) != 0:
                # operation for odd number
                op = (3 * op) + 1
            else:
                # operation does not complete in 50000 steps
                # print(f'Failed! {int(opmain)} did not finish the sequence within {max_steps} steps.')
                result_txt.write(f'{int(opmain)}:\t FAILED!;\t {max_num} reached\n')
    result_txt.close()
    stat_txt = open("stats.txt", "w")
    stat_txt.write(f'Max Steps Reached: {int(step_max_op)}: {step_max_stat} steps; {int(step_max_num)} reached\n'
                   f'Max Number Reached: {int(num_max_op)}: {num_max_stat} steps; {int(num_max_num)} reached\n'
                   f'Total Computations Performed: {total_comps}')
    winsound.Beep(4000, 100)


if __name__ == '__main__':
    main()
