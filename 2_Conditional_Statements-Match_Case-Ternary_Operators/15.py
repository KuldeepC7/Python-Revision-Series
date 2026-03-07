# 15. A webhook sends deployment events as a tuple: event = ("deploy", branch_name). Write a match/case block that unpacks the tuple, but use an if guard inside the case so that it only sets trigger_build = True if the action is "deploy" AND the branch is "main".



# ste = 'someone, me, 7, x, 4.0'
# tup = tuple(ste.split(','))
# print(tup)

event = ('deploy', 'main')
action, branch = event
trigger_build = None

match action:
    case 'deploy':
        if branch == 'main':
            trigger_build = True
        else:
            trigger_build = False
    
    case _:
        trigger_build = False


print(trigger_build)