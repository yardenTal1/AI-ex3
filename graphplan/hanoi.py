import sys


def create_domain_file(domain_file_name, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))] + ['d_E']  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))] # [p_0,..., p_(m_ - 1)]
    domain_file = open(domain_file_name, 'w')  # use domain_file.write(str) to write to domain_file
    domain_file.write("Propositions:\n")
    for p in pegs:
        for d in disks:
            if d != 'd_E':
                domain_file.write(d + "_in_" + p + " ")
            domain_file.write(p + "_top_" + d + " ")

    for idx, d in enumerate(disks):
        for j in range(idx + 1, n_ + 1):
            domain_file.write(d + "_on_" + disks[j] + " ")

    domain_file.write("\nActions:\n")
    for p1 in pegs:
        for p2 in pegs:
            if p1 != p2:
                for idx1, d1 in enumerate(disks[:-1]):
                    for idx2 in range(idx1+1, n_ + 1):
                        for idx3 in range(idx1+1, n_ + 1):
                            if (idx2 == n_ and idx3 == n_) or idx2 != idx3:
                                domain_file.write("Name: " + p1+p2+d1+disks[idx2]+disks[idx3] + "\n")
                                domain_file.write("pre: " + d1 + "_in_" + p1 + " "
                                                  + p1 + "_top_" + d1 + " "
                                                  + p2 + "_top_" + disks[idx3] + " "
                                                  + d1 + "_on_" + disks[idx2] + " ")
                                if idx2 != n_:
                                    domain_file.write(disks[idx2] + "_in_" + p1 + " ")
                                if idx3 != n_:
                                    domain_file.write(disks[idx3] + "_in_" + p2 + " ")
                                domain_file.write("\n")
                                domain_file.write("add: " + d1 + "_in_" + p2 + " "
                                                  + p2 + "_top_" + d1 + " "
                                                  + p1 + "_top_" + disks[idx2] + " "
                                                  + d1 + "_on_" + disks[idx3] + "\n")
                                domain_file.write("delete: " + d1 + "_in_" + p1 + " "
                                                  + d1 + "_on_" + disks[idx2] + " "
                                                  + p1 + "_top_" + d1 + " "
                                                  + p2 + "_top_" + disks[idx3] + "\n")
    domain_file.close()


def create_problem_file(problem_file_name_, n_, m_):
    disks = ['d_%s' % i for i in list(range(n_))] + ['d_E']  # [d_0,..., d_(n_ - 1)]
    pegs = ['p_%s' % i for i in list(range(m_))]  # [p_0,..., p_(m_ - 1)]
    problem_file = open(problem_file_name_, 'w')  # use problem_file.write(str) to write to problem_file
    problem_file.write("Initial state: ")
    for p in pegs[1:]:
        problem_file.write(p + '_top_d_E ')
    for i in range(n_):
        problem_file.write(disks[i] + "_in_p_0 ")
        problem_file.write(disks[i] + "_on_" + disks[i+1] + " ")
    problem_file.write('p_0_top_d_0')
    problem_file.write("\n")
    problem_file.write("Goal state: ")
    for i in range(n_):
        problem_file.write(disks[i] + "_in_p_" + str(m_ - 1) + " ")
        problem_file.write(disks[i] + "_on_" + disks[i + 1] + " ")
    problem_file.write("\n")
    problem_file.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: hanoi.py n m')
        sys.exit(2)

    n = int(float(sys.argv[1]))  # number of disks
    m = int(float(sys.argv[2]))  # number of pegs

    domain_file_name = 'hanoi_%s_%s_domain.txt' % (n, m)
    problem_file_name = 'hanoi_%s_%s_problem.txt' % (n, m)

    create_domain_file(domain_file_name, n, m)
    create_problem_file(problem_file_name, n, m)
