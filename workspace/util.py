def path_and_name(path, name, num, tp):
    l = []
    for i in range(1, num+1):
        # fname = path.rstrip('/')+ '/' + name + '{:02}'.format(i) + "." + tp.lstrip('.')
        fname = path.rstrip('/')+ '/' + name + '{:02}'.format(i) + tp
        l.append(fname)
    return l

def name_file(path, name, num, tp):
    return path.rstrip('/')+ '/' + name + '{:02}'.format(num) + "." + tp.lstrip('.')

if __name__ == '__main__':
    print(name_file('path/','fn', 10,'.txt'))