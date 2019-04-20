import opcode_33
exec(open("/src/external-vcs/bitbucket/maynard/maynard/stackeffect.py", 'r').read())
for i in range(255):
    my_effect = opcode_33.oppush[i] - opcode_33.oppop[i]
    if my_effect != opcode_stack_effect[i]:
        if my_effect <= -8 or opcode_stack_effect[i] == -9:
            continue
        print("%s should have effect %d, got %d" % (opcode_33.opname[i],
                                                    opcode_stack_effect[i],
                                                    my_effect))
