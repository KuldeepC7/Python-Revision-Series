# 24. Cloud infrastructure config parsing: You receive a nested tuple config = ("dyno", ("web", 5)). Write a match/case block that matches this nested structure, extracts the integer 5 into a variable count, and uses a guard to trigger a "Scale Warning" if count > 3.

config = ('dyno', ('web', 5))

match config:
    case (vps_type, (platform, count)):
        if count > 3:
            print('Scale Warning')
        
        else:
            print('Continue')
        
    case _:
        print('Malformed tuple')