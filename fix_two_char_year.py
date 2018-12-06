import datetime.datetime as dt
def fix_two_char_year(dat):
    '''Use when dates have format mm/dd/yy MM:SS'''
    last2_digits_this_yr = int(str(dt.now().year)[-2:])
    try:
        splt = str(dat).split('/')
        if int(splt[2].split(' 0')[0]) > last2_digits_this_yr: 
            new_dat = splt[0] + '/' + splt[1] + '/19' + splt[2]
        else:
            new_dat = splt[0] + '/' + splt[1] + '/20' + splt[2]
        return new_dat
    except:
        return '1/1/1801 0:00'
